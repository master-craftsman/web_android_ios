from .. import by, ui

page = ui.element({
    'IOS': by.accessibility_id('uptick.DrawerMenu'),
    'WEB': by.css('[data-testid="menu-toggler-block"]'),
    'ANDROID': by.xpath(
        '//android.view.View[@content-desc="Total Balance"]'
    )
})
