import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import readConfig

localReadConfig = readConfig.ReadConfig()
proDir = os.path.split(os.path.realpath(__file__))[0]
report_file = os.path.join(proDir, "test.html")


class EmailSender:
    def __init__(self):
        global smtp_host, smtp_port, smtp_user, smtp_password, from_addr, to_addrs, subject, report_file
        self.smtp_host = localReadConfig.get_email("mail_host")
        self.smtp_port = localReadConfig.get_email("mail_port")
        self.smtp_user = localReadConfig.get_email("mail_user")
        self.smtp_password = localReadConfig.get_email("mail_pass")
        self.from_addr = localReadConfig.get_email("sender")
        # self.to_addrs = to_addrs if isinstance(to_addrs, list) else [to_addrs]
        self.to_addrs = localReadConfig.get_email("receiver")
        self.receiver = []
        # get receiver list
        for n in str(self.to_addrs).split("/"):
            self.receiver.append(n)
        self.subject = localReadConfig.get_email("subject")
        self.report_file = report_file

    def send_email(self, resultPath):
        # 构造邮件
        self.report_file = resultPath
        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        msg['To'] = ','.join(self.to_addrs)
        msg['Subject'] = self.subject


        # 添加测试报告邮件正文
        with open(self.report_file, 'r', encoding='utf-8') as f:
            report_content = f.read()
            text = MIMEText(report_content, 'html', 'utf-8')
            msg.attach(text)

        # 添加测试报告附件
        with open(self.report_file, 'rb') as f:
            attach = MIMEApplication(f.read(), _subtype='html')
            attach.add_header('Content-Disposition', 'attachment', filename="result.html")
            msg.attach(attach)

        # 发送邮件
        try:
            smtp_obj = smtplib.SMTP(self.smtp_host, self.smtp_port)
            smtp_obj.starttls()
            smtp_obj.login(self.smtp_user, self.smtp_password)
            smtp_obj.sendmail(self.from_addr, self.receiver, msg.as_string())
            smtp_obj.quit()
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print('邮件发送失败：', e)
