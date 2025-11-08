# The 'page' parameter here is the Playwright fixture automatically 
# provided by pytest because 'conftest.py' exists.
def test_user_can_login(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    
    # Assert successful login
    assert page.url == "https://www.saucedemo.com/inventory.html"
