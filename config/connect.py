#!/usr/bin/python

import configparser

import pymongo
import sentry_sdk
from sentry_sdk import capture_exception


class SmartMeterConfig:
    # global variables

    # sentry
    sentry_url: str

    # Database credentials
    database_address: str
    database_user: str
    database_port: int
    database_password: str
    database_dbname: str

    # MQTT credentials
    mqtt_address: str
    mqtt_id: str
    mqtt_user: str
    mqtt_password: str
    mqtt_port: int

    def __init__(self):
        parser = configparser.ConfigParser()
        try:
            parser.read('config/config.ini')
            if len(parser) == 1:
                raise "Failed to open/find all files"

            # sentry
            self.sentry_url = parser.get('sentry', 'url')

            # db
            self.database_address = parser.get('database', 'address')
            self.database_user = parser.get('database', 'user')
            self.database_port = parser.getint('database', 'port')
            self.database_password = parser.get('database', 'password')
            self.database_dbname = parser.get('database', 'dbname')

            # mqtt
            self.mqtt_address = parser.get('MQTT', 'address')
            self.mqtt_id = parser.get('MQTT', 'id')
            self.mqtt_user = parser.get('MQTT', 'username')
            self.mqtt_password = parser.get('MQTT', 'password')
            self.mqtt_port = parser.getint('MQTT', 'port')
        except Exception as e:
            self.errorHandler.report(e)

    def sentry_reporter(self, exception):
        sentry_sdk.init(self.sentry_url, traces_sample_rate=1.0,)
        return capture_exception(exception)
