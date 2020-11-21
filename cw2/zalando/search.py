import sys, os, time

sys.path.insert(0, os.path.abspath('..'))

from selenium.webdriver.common.keys import Keys

from logger import create_logger, log


def search_test_zalando(driver):
    try:
        create_logger("Starting zalando search test")
        driver.get("https://www.zalando.pl/mezczyzni-home/")
        driver.find_element_by_xpath(
            '//*[@id="z-navicat-header-root"]/header/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[3]/form/div/input').send_keys(
            'jeansy')
        driver.find_element_by_xpath(
            '//*[@id="z-navicat-header-root"]/header/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[3]/form/div/input').send_keys(
            Keys.ENTER)
        time.sleep(5)
        element = driver.find_element_by_xpath('//*[@id="z-nvg-cognac-root"]/div[1]/div[1]/div[2]/div/div/div/div/div/span/h1').text

        assert 'jeansy' in element

        driver.stop_client()
        driver.quit()

    except Exception as e:
        log(40, 'Error occured while running test for zalando search for ' + driver.name + ' ' + str(e))
    finally:
        log(20, 'Finished test for zalando search for ' + driver.name)
