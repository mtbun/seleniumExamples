from libs import *

login = {
    'username' : '',
    'pass' : ''
}

paths = {
    'login' : 'nav-link-accountList',
    'username_f' : 'ap_email',
    'pass_f' : 'ap_password',
    'signin' : 'signInSubmit'
}

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.get('https://www.amazon.com.tr')

login_field = wait.until(EC.presence_of_element_located((By.ID, paths['login'])))
login_field.click()

username_field = wait.until(EC.presence_of_element_located((By.ID,paths['username_f'])))
username_field.send_keys(login['username'])
username_field.submit()

password_field = wait.until(EC.presence_of_element_located((By.ID, paths['pass_f'])))
password_field.send_keys(login['pass'])
password_field.submit()



#driver.quit()