import sys, os, time

sys.path.insert(0, os.path.abspath('..'))


from logger import log


def navigation_test_pepper(driver):
    try:
        log(20, "Starting pepper navigation test for " + driver.name)

        log(20, "Pepper navigation test for " + driver.name + ' entering site')
        driver.get("https://www.pepper.pl/")

        log(20, "Pepper navigation test for " + driver.name + ' choosing first group')
        driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/section/div[1]/div[3]/div/div/div/div/div[2]/div/ol/li[1]/div/div/a').click()
        assert "Elektronika" in driver.title
        driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/header/div/div/div[1]/a').click()
        time.sleep(1)

        log(20, "Pepper navigation test for " + driver.name + ' choosing second group')
        driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/section/div[1]/div[3]/div/div/div/div/div[2]/div/ol/li[2]/div/div/a').click()
        assert "Gaming" in driver.title
        driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/header/div/div/div[1]/a').click()
        time.sleep(1)

        log(20, "Pepper navigation test for " + driver.name + ' choosing third group')
        driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/section/div[1]/div[3]/div/div/div/div/div[2]/div/ol/li[3]/div/div/a').click()
        assert "Dom" in driver.title
        driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/header/div/div/div[1]/a').click()
        time.sleep(1)

        driver.stop_client()
        driver.quit()

    except Exception as e:
        log(40, 'Error occured while running test for pepper navigation for ' + driver.name + ' ' + str(e))
    finally:
        log(20, 'Finished test for pepper navigation for ' + driver.name)


