import sys, os, time

sys.path.insert(0, os.path.abspath('..'))


from logger import log


def navigation_test_pepper(driver):
    try:
        log(20, "Starting pepper navigation test for " + driver.name)

        log(20, "Pepper navigation test for " + driver.name + ' entering site')
        driver.get("https://www.pepper.pl/")

        time.sleep(3)

        log(20, "Pepper navigation test for " + driver.name + ' choosing first group')
        el1 = driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/section/div[1]/div[3]/div/div/div/div/div[2]/div/ol/li[1]/div/div/a')
        name = el1.text
        el1.click()
        title = driver.find_element_by_xpath('//*[@id="main"]/div[1]/section[1]/header/div[4]/div/div/div[1]/div[2]/h1').text
        print(name, title)
        assert name in title
        driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/header/div/div/div[1]/a').click()
        time.sleep(1)

        log(20, "Pepper navigation test for " + driver.name + ' choosing second group')
        el2 = driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/section/div[1]/div[3]/div/div/div/div/div[2]/div/ol/li[2]/div/div/a')
        name = el2.text
        el2.click()
        title = driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/section[1]/header/div[4]/div/div/div[1]/div[2]/h1').text
        print(name, title)
        assert name in title
        driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/header/div/div/div[1]/a').click()
        time.sleep(1)

        log(20, "Pepper navigation test for " + driver.name + ' choosing third group')
        el3 = driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/section/div[1]/div[3]/div/div/div/div/div[2]/div/ol/li[3]/div/div/a')
        name = el3.text
        el3.click()
        title = driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/section[1]/header/div[4]/div/div/div[1]/div[2]/h1').text
        print(name, title)
        assert name in title
        driver.find_element_by_xpath(
            '//*[@id="main"]/div[1]/header/div/div/div[1]/a').click()
        time.sleep(1)

    except Exception as e:
        log(40, 'Error occurred while running test for pepper navigation for ' + driver.name + ' ' + str(e))
    finally:
        log(20, 'Finished test for pepper navigation for ' + driver.name)


