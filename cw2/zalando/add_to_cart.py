import sys, os, time

sys.path.insert(0, os.path.abspath('..'))

from logger import log


def add_to_cart_test_zalando(driver):
    try:
        log(20, "Starting zalando add to cart test for " + driver.name)

        log(20, "Zalando add to cart test for " + driver.name + ' entering site')
        driver.get("https://www.zalando.pl/usha-torebka-black-1us51h02p-q11.html")

        time.sleep(4)
        log(20, "Zalando add to cart test for " + driver.name + ' accept cookies')
        driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]').click()

        log(20, "Zalando add to cart test for " + driver.name + ' adding to cart')
        driver.find_element_by_xpath(
            '/html/body/div[4]/div/div[1]/div/div[2]/div[1]/x-wrapper-re-1-5/div[2]/button').click()

        log(20, "Zalando add to cart test for " + driver.name + ' moving to cart')
        driver.find_element_by_xpath(
            '//*[@id="z-navicat-header-root"]/header/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div[3]/a').click()

        log(20, "Zalando add to cart test for " + driver.name + ' checking cart')
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div[1]/div[1]/h2').text

        assert '1 art.' in element

        driver.stop_client()
        driver.quit()

    except Exception as e:
        log(40, 'Error occured while running test for zalando add to cart for ' + driver.name + ' ' + str(e))
    finally:
        log(20, 'Finished test for zalando add to cart for ' + driver.name)
