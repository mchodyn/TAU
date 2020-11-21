import sys, os

sys.path.insert(0, os.path.abspath('..'))

from logger import log


def sellers_test_pepper(driver):
    try:
        log(20, "Starting pepper seller test for " + driver.name)

        log(20, "Pepper seller test for " + driver.name + ' entering site')
        driver.get("https://www.pepper.pl/")

        log(20, "Pepper seller test for " + driver.name + ' opening menu and choosing seller')
        driver.find_element_by_xpath('//*[@id="main"]/div[1]/header/div/div/div[2]/div').click()
        driver.find_element_by_xpath('/html/body/section/div/nav/ul[3]/li[1]/a').click()

        log(20, "Pepper seller test for " + driver.name + ' checking seller page')
        assert 'Empik' in driver.title
        assert 'Empik' in driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/section[1]/header/div[2]/div[1]/div/div[2]/h1').text

    except Exception as e:
        log(40, 'Error occurred while running test for pepper seller for ' + driver.name + ' ' + str(e))
    finally:
        log(20, 'Finished test for pepper seller for ' + driver.name)
