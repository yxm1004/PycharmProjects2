import unittest
import requests
import json

from interfaceTest.common.ApiConstants import ApiConstants
from interfaceTest.common.GetToken import Token
from interfaceTest import readConfig
from interfaceTest.testCase.mycase.testcomponentsave import testcomponentsave

localReadConfig = readConfig.ReadConfig()
class processPlan(unittest.TestCase ):
