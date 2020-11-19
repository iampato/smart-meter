#!/usr/bin/python
from config.connect import SmartMeterConfig

class SmartMeterErrorHandler():
    config: SmartMeterConfig

    def __init__(self):
        smartMeterConfig = SmartMeterConfig()
        self.config = smartMeterConfig

    @staticmethod
    def report(self,message):
        print("An exception occurred: "+str(message))
        config.errorHandler(message)