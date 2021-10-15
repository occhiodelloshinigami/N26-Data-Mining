from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import locale
from datetime import datetime


def login(browser, username_str, password_str):
    try:
        username = browser.find_element_by_name('username')
        username.clear()
        username.send_keys(username_str)
        password = browser.find_element_by_name('password')
        password.clear()
        password.send_keys(password_str)
        submit = browser.find_element_by_xpath("//button")
        submit.submit()
    except:
        print("problem(s) while logging in")


def logout(browser):
    person_logo = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/header/div/div[2]/a[5]")))
    person_logo.send_keys(Keys.RETURN)
    exit_logo = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@title='Esci']")))
    exit_logo.send_keys(Keys.RETURN)


def scroll_to_bottom(browser):
    try:
        button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@title='Successivo']")))
        while button.size != 0:
            try:
                button = WebDriverWait(browser, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@title='Successivo']")))
            except:
                print("Sono arrivato alla fine")
            button.send_keys(Keys.RETURN)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except:
        print("Sono già arrivato alla fine")


def get_tags(browser):
    tags_lists = []
    jointed_tags = ""
    try:
        tags_elements = WebDriverWait(browser, 2).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='tags_container']/div[*]/a")))
        # tags_elements = browser.find_elements_by_xpath("//*[@id='tags_container']/div[*]/a")
        for i in range(tags_elements.__len__()):
            tags_lists.append(tags_elements[i].text)

        for element in tags_lists:
            jointed_tags = jointed_tags + element
        return jointed_tags
    except:
        return jointed_tags


def get_name(browser):
    name = ""
    logo = True
    try:
        logo_element = WebDriverWait(browser, 1).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[1]/div/img")))
    except:
        logo = False
    try:
        if logo:
            name = WebDriverWait(browser, 1).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/p"))).text
        else:
            name = WebDriverWait(browser, 1).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[1]/p"))).text
        return name
    except:
        return name


def get_value(browser):
    logo = True
    try:
        logo_element = WebDriverWait(browser, 1).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[1]/div/img")))
    except:
        logo = False
    if logo:
        amount = WebDriverWait(browser, 1).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[3]/p/span/span"))).text
    else:
        amount = WebDriverWait(browser, 1).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/p/span/span"))).text
    return float(re.findall(r"[-+]?\d*,\d+|\d+", amount)[0].replace(',', '.'))


def get_date(browser):
    logo = True
    try:
        logo_element = WebDriverWait(browser, 1).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[1]/div/img")))
    except:
        logo = False
    if logo:
        date_str = WebDriverWait(browser, 1).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[4]/span[1]"))).text
    else:
        date_str = WebDriverWait(browser, 1).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[3]/span"))).text
    locale.setlocale(locale.LC_TIME, 'it_IT')
    date_str = date_str.split(sep=' ·', maxsplit=1)[0]
    datetime_object = datetime.strptime(date_str, '%A %d %B %Y, %H:%M')
    return datetime_object


def get_category(browser):
    return WebDriverWait(browser, 1).until(
                    EC.visibility_of_element_located((By.XPATH,
                                                      "//*[@id='details_container']/div[2]/div/div[1]/div/div[2]/div/div/p"))).text
