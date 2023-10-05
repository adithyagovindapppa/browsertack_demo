# from appium import webdriver
# import pytest
# @pytest.fixture()
# def setup():
#     desired_caps = {
#         'platformName': 'Android',  # Change to 'iOS' for iOS testing
#         'platformVersion': '13.0',  # Replace with the target platform version
#         'deviceName': '2B101JEGR10785',  # Replace with the target device name
#         # 'appPackage': 'your_app_package',  # Replace with your app's package name
#         'app': "/home/adithya/Downloads/mobile.apk",# Replace with your app's main activity name"/home/adithya/Downloads/mobile.apk"
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
            "app": "bs://f49ee8f13e2cb17fe25c074f7de0532d3e4caec5",
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


