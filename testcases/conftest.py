# from appium import webdriver
# import pytest
# @pytest.fixture()
# def setup():
#     desired_caps = {
#         'platformName': 'Android',  # Change to 'iOS' for iOS testing
#         'platformVersion': '13.0',  # Replace with the target platform version
#         'deviceName': '2B101JEGR10785',  # Replace with the target device name
#         # 'appPackage': 'your_app_package',  # Replace with your app's package name
#         'app': "/home/adithya/Downloads/newtest.apk",# Replace with your app's main activity name
#         # 'noReset': True,
#         # 'autoGrantPermissions': True,
#         # 'autoAcceptAlerts': True,
#         # # Add other desired capabilities as needed
#         # 'newCommandTimeout' : 600
#     }
#
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#     print("Launching Appium app")
#     return driver


import pytest
from appium import webdriver

@pytest.fixture()
def setup():
    username = 'tanu_t8LQSO'
    key = 'Y44vg1NNsJABQb4fJnTp'
    desired_caps = {
            "app": "bs://9598d32930c02c1816e3e428f980b06473487f88",
            "browserName": "Chrome",
            "deviceName": "Google Pixel 6 Pro",
            "os_version": "13.0",
            "realMobile": "true",
            "autoGrantPermissions": "true",
            "autoAcceptAlerts": "true",
            "platformName": "Android",
            "debug": " true",
    }
    print(username, key)
    url = f'https://' + username + ':' + key + '@hub-cloud.browserstack.com/wd/hub'
    print(url)
    driver = webdriver.Remote(url, desired_caps)
    yield driver
    driver.quit()  # This ensures that the WebDriver is closed after the test is executed

# You can use the fixture in your test functions like this:
def test_example(setup):
    driver = setup
    # Your test code using the 'driver' goes here


