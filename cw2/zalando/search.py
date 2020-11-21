import sys, os, time

sys.path.insert(0, os.path.abspath('..'))

from selenium.webdriver.common.keys import Keys

from logger import log


def search_test_zalando(driver):
    try:
        log(20, "Starting zalando search test for " + driver.name)

        log(20, "Zalando search test for " + driver.name + ' entering site')
        driver.get("https://www.zalando.pl/mezczyzni-home/")

        log(20, "Zalando search test for " + driver.name + ' passing search query')
        driver.find_element_by_xpath(
            '//*[@id="z-navicat-header-root"]/header/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[3]/form/div/input').send_keys(
            'jeansy')
        driver.find_element_by_xpath(
            '//*[@id="z-navicat-header-root"]/header/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[3]/form/div/input').send_keys(
            Keys.ENTER)
        time.sleep(5)

        log(20, "Zalando search test for " + driver.name + ' checking searched term')
        element = driver.find_element_by_xpath('//*[@id="z-nvg-cognac-root"]/div[1]/div[1]/div[2]/div/div/div/div/div/span/h1').text
        assert 'jeansy' in element

        driver.stop_client()
        driver.quit()

    except Exception as e:
        log(40, 'Error occured while running test for zalando search for ' + driver.name + ' ' + str(e))
    finally:
        log(20, 'Finished test for zalando search for ' + driver.name)
