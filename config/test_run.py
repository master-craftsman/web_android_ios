import os
from selene import config as _selene_config

from . import env

ONE_SESSION = env.get_bool('ONE_SESSION', 'False')
BROWSER_LOGS = env.get_bool('BROWSER_LOGS', 'False')

_selene_config.timeout = int(env.get('UI_TIMEOUT', 15))
APPIUM_TIMEOUT = int(env.get('APPIUM_TIMEOUT', 60))

PLATFORM = env.get('PLATFORM', 'IOS')
# shortcuts
IS_WEB = PLATFORM == 'WEB'
IS_MOBILE = PLATFORM in ('IOS', 'ANDROID')
IS_ANDROID = PLATFORM == 'ANDROID'
IS_IOS = PLATFORM == 'IOS'

APPIUM_SERVER = env.get('APPIUM_SERVER', 'http://localhost:4723/wd/hub')

APP_NAME = {
    'IOS': env.get('IOS_APP_NAME', 'Runner.ipa'),
    'ANDROID': env.get('ANDROID_APP_NAME', 'app-release.apk')
}.get(PLATFORM)

_DEFAULT_APP_PATH = str(os.path.join(os.getcwd(), fr"mobile_app/{APP_NAME}"))
MOBILE_APP = env.get('MOBILE_APP', _DEFAULT_APP_PATH) if IS_MOBILE else None

ANDROID_VERSION = env.get('ANDROID_VERSION', '12.0')
ANDROID_DEVICE_NAME = env.get('ANDROID_DEVICE_NAME', 'Pixel_4_API_31')

IOS_VERSION = env.get('IOS_VERSION', '16.2')
IOS_DEVICE_NAME = env.get('IOS_DEVICE_NAME', 'iPhone 14')
