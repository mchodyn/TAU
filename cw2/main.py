from drivers import drivers
from logger import create_logger

from pepper.best_sellers import best_sellers_test_pepper
from pepper.navigation import navigation_test_pepper
from pepper.search import search_test_pepper
from zalando.search import search_test_zalando
from zalando.navigation import navigation_test_zalando
from zalando.add_to_cart import add_to_cart_test_zalando

create_logger()
for driver in drivers:
    # best_sellers_test_pepper(driver)
    # navigation_test_pepper(driver)
    # search_test_pepper(driver)
    # search_test_zalando(driver)
    navigation_test_zalando(driver)
    # add_to_cart_test_zalando(driver)
