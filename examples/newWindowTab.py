from libs import *



URL = 'https://www.wikipedia.org'
languages = ['ch', 'en', 'de']

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get(URL)


for i in range(len(languages)):
    driver.execute_script('window.open()')
    driver.switch_to.window(driver.window_handles[i+1])
    language_URL = 'https://' + languages[i] + '.wikipedia.org/'
    driver.get(language_URL)


if (len(driver.window_handles) > 0):
    print('opened new tab')