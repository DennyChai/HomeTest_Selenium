import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'screenshots')))
from pages.page_twitch import PageTwitch
from utils.devices import Devices
from utils.selenium_utils_phone import SeleniumUtilsPhone
from datetime import datetime
import pytest

TEST_DEVICE = Devices.IPHONE_X.value

@pytest.fixture(scope="session")
def browser():
    selenium_utils_phone_init = SeleniumUtilsPhone(TEST_DEVICE)
    driver = selenium_utils_phone_init.set_up()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def page_twitch(browser):
    page_twitch = PageTwitch(browser)
    return page_twitch

def test_open_page(page_twitch, stop_at, request):
    expected_title = "Twitch"
    page_twitch.open_page()
    assert page_twitch.driver.title == expected_title
    if request.node.name == stop_at:
        pytest.exit(f"Stopped at {request.node.name} as requested")

def test_search_on_page(page_twitch, stop_at, request):
    expected_value = "StarCraft II"
    page_twitch.search_on_page(expected_value)
    element = page_twitch.wait_get_element('//div[p and count(p) = 3]/p', "Game name") 
    assert element.text == expected_value
    if request.node.name == stop_at:
        pytest.exit(f"Stopped at {request.node.name} as requested")

def test_expand_the_video_list(page_twitch, stop_at, request):
    page_twitch.expand_the_video_list()
    element = page_twitch.wait_get_element('//ul/li[@role="presentation"]/a[@data-index="1"]', "Tab") 
    assert element.get_attribute("aria-selected") == "true"
    if request.node.name == stop_at:
        pytest.exit(f"Stopped at {request.node.name} as requested")

def test_page_scroll_down(page_twitch, stop_at, request):
    scroll_times = 2
    cur_height = page_twitch.driver.execute_script("return document.documentElement.scrollTop")
    page_twitch.page_scroll_down(scroll_times)
    final_height = page_twitch.driver.execute_script("return document.documentElement.scrollTop")
    assert cur_height+(scroll_times*100) == final_height
    if request.node.name == stop_at:
        pytest.exit(f"Stopped at {request.node.name} as requested")

def test_select_streamers(page_twitch, stop_at, request):
    page_twitch.select_streamers()
    element = page_twitch.wait_get_element('//div[contains(@class, "secondaryContent")]', "Live Stream Page") 
    assert element is not None
    if request.node.name == stop_at:
        pytest.exit(f"Stopped at {request.node.name} as requested")

def test_take_screeshot(page_twitch, stop_at, request):
    file_name = f"TestTwitch-{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}"
    page_twitch.take_screenshot(file_name)
    assert os.path.isfile(f"./screenshots/{file_name}.png")
    