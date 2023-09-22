import configparser
import csv
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import webdriver, options

config = configparser.RawConfigParser()
config.read("/home/adithya/PycharmProjects/Quest/Configurations/config.ini")


class ReadConfig:

    @staticmethod
    def getusername():
        username = config.get('common_info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common_info', 'password')
        return password

    @staticmethod
    def get_logs_directory():
        current_directory = os.path.dirname(__file__)
        current_directory = current_directory.replace("utilities", "")
        logs_directory = os.path.join(current_directory, 'Logs')
        return logs_directory

    @staticmethod
    def read_credentials_from_csv():
        credentials = []
        details = []
        filename = "/home/adithya/Documents/Appiumlocal/Testdata/credentials.csv"
        with open(filename, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                email = row['email']
                password = row['password']
                credentials.append({'email': email, 'password': password})
        credentials_data = credentials
        for data in credentials_data:
            details.append(data['email'])
            details.append(data['password'])
        return details

