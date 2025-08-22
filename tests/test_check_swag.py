from pages.swag_labs import SwagLabs

def test_case_1(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    swag_labs_page.find_element('div.login_logo')

def test_case_2(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    swag_labs_page.find_element('#user-name')

def test_case_3(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    swag_labs_page.find_element('#password')