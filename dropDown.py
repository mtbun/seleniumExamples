from libs import *

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
mail_field = wait.until(EC.presence_of_element_located((By.ID,'email_create')))
x = random.randint(10000,9999999)
mail_field.send_keys(str('hello' + str(x) + '@gmail.com'))
mail_field.submit()

radio_btn = wait.until(EC.presence_of_element_located((By.ID, 'id_gender2')))
radio_btn.click()

#handle dropdown
driver.execute_script('window.scrollBy(0,740)','')