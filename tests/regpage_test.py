import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from elements import RegisterLocators
from values import RegValue
from selenium.common import exceptions


reg_url = "https://koshelek.ru/authorization/signup"
@pytest.fixture(autouse=True,scope='session')
def driver():
   options = Options()
   #options.add_argument('--headless') # Убрать решётку,что бы запускать тесты в фоновом режиме (no UI)
   driver = webdriver.Firefox(options)
   driver.get(reg_url)
   driver.implicitly_wait(10)
   yield driver
   driver.quit()
@pytest.fixture(autouse=True,scope='function')
def clear_fields(driver): # Сбросит поля перед тестом (быстрее,чем обновление страницы)
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root # clear() не работает
   root.find_element(*RegisterLocators.name_field).send_keys(Keys.CONTROL + "a" + Keys.DELETE) 
   root.find_element(*RegisterLocators.mail_field).send_keys(Keys.CONTROL + "a" + Keys.DELETE)
   root.find_element(*RegisterLocators.pass_field).send_keys(Keys.CONTROL + "a" + Keys.DELETE)
   root.find_element(*RegisterLocators.referral_field).send_keys(Keys.CONTROL + "a" + Keys.DELETE)
   root.find_element(*RegisterLocators.check_box).click()

# Только негативные тесты. Пройденный тест = система корректно реагирует на ошибку и не пропускает пользователя

def test_small_name(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.small_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.correct_pass)
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url # Проверяем,что система не допустила нас до следующего шага
def test_big_name(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.big_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.correct_pass)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_bad_name(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.bad_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.correct_pass)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_num_name(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.num_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.correct_pass)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_ru_name(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.ru_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.correct_pass)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_small_pass(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.correct_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.small_pass)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_big_pass(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.correct_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.big_pass)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_low_pass(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.correct_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.low_pass)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_num_pass(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.correct_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.num_pass)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_text_pass(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.correct_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.text_pass)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_bad_mail(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.correct_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.bad_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.correct_pass)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_small_referral(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.correct_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.correct_pass)
   root.find_element(*RegisterLocators.referral_field).send_keys(*RegValue.small_ref)
   root.find_element(*RegisterLocators.check_box).click()
   try: # Кнопка неактивна,когда реферальный код некорретного формата
      root.find_element(*RegisterLocators.continue_btn).click()
   except exceptions.ElementClickInterceptedException:
      assert driver.current_url == reg_url
   else:
      assert driver.current_url == reg_url
def test_big_referral(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.correct_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.correct_pass)
   root.find_element(*RegisterLocators.referral_field).send_keys(*RegValue.big_ref)
   root.find_element(*RegisterLocators.check_box).click()
   try: # Кнопка неактивна,когда реферальный код некорретного формата
      root.find_element(*RegisterLocators.continue_btn).click()
   except exceptions.ElementClickInterceptedException:
      assert driver.current_url == reg_url
   else:
      assert driver.current_url == reg_url
def test_without_name(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.correct_pass)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_without_mail(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.correct_name)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.correct_pass)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_without_pass(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.correct_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_only_name(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.correct_name)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_only_mail(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_only_pass(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.correct_pass)
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_empty_fields(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.check_box).click()
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url
def test_without_checkbox(driver):
   shadowhost = driver.find_element(*RegisterLocators.shadowHost)
   root = shadowhost.shadow_root
   root.find_element(*RegisterLocators.name_field).send_keys(*RegValue.correct_name)
   root.find_element(*RegisterLocators.mail_field).send_keys(*RegValue.correct_mail)
   root.find_element(*RegisterLocators.pass_field).send_keys(*RegValue.correct_pass)
   root.find_element(*RegisterLocators.continue_btn).click()
   assert driver.current_url == reg_url