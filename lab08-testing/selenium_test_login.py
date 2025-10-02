from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()   # cần cài ChromeDriver
    driver.get("http://localhost:5000/login")  # URL form login
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "login").click()
    time.sleep(1)
    assert "Welcome" in driver.page_source

def test_login_fail(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.ID, "login").click()
    time.sleep(1)
    assert "Invalid" in driver.page_source

def test_login_empty_input(driver):
    driver.find_element(By.ID, "login").click()
    time.sleep(1)
    assert "Required" in driver.page_source
