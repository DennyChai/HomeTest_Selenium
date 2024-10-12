import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'pages')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils')))

from utils.selenium_utils_phone import SeleniumUtilsPhone
from utils.devices import devices
from pages.page_twitch import PageTwitch


selenium_utils_phone = SeleniumUtilsPhone(devices.GALAXY_NOTE_3.value)
driver = selenium_utils_phone.set_up()

twitch = PageTwitch(driver)
twitch.testflow()