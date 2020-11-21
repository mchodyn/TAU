import sys, os, time

sys.path.insert(0, os.path.abspath('..'))

from selenium.webdriver.common.keys import Keys

from logger import log


def search_test_pepper(driver):
    try:
        log(20, "Starting pepper search test for " + driver.name)

        log(20, "Pepper search test for " + driver.name + ' entering site')
        driver.get("https://www.pepper.pl/")

        log(20, "Pepper search test for " + driver.name + ' passing search query')
        driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/header/div/div/div[3]/form/div/input').send_keys('patelnie')
        driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/header/div/div/div[3]/form/div/input').send_keys(Keys.ENTER)
        time.sleep(3)

        log(20, "Pepper search test for " + driver.name + ' checking searched term')
        assert 'patelnie' in driver.title

        driver.stop_client()
        driver.quit()

    except Exception as e:
        log(40, 'Error occurred while running test for pepper search for ' + driver.name + ' ' + str(e))
    finally:
        log(20, 'Finished test for pepper search for ' + driver.name)
