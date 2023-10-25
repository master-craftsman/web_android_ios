import time

from .. import by, ui
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder

finder = FlutterFinder()

user_email = ui.element({
    'IOS': by.accessibility_id('emailInput'),
    'WEB': by.css('[type=login]'),
    'ANDROID': by.xpath('(//android.widget.EditText)[1]')
})

user_password = ui.element({
    'IOS': by.accessibility_id('passwordInput'),
    'WEB': by.css('[type=password]'),
    'ANDROID': by.xpath('//android.widget.EditText')
})

submit_button = ui.element({
    'IOS': by.accessibility_id('signin-button'),
    'WEB': by.css('[type="submit"]'),
    'ANDROID': by.xpath('(//android.widget.Button)[1]')
})
sing_in_button = ui.element({
    'IOS': by.accessibility_id('signin-button'),
    'WEB': by.css('[type="submit"]'),
    'ANDROID': by.xpath('(//android.widget.Button)[3]')
})
set_password = ui.element({
    'IOS': by.accessibility_id('signin-button'),
    'WEB': by.css('[type="submit"]'),
    'ANDROID': finder.by_value_key("5")
})


def login_with(email,password):
    user_email.click()
    user_email.set(email)
    submit_button.click()
    user_password.click()
    user_password.set(password)
    sing_in_button.click()
    for i in range(5):
        set_password.click()




