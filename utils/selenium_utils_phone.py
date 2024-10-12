from interface_selenium_utils import InterfaceSeleniumUtils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class SeleniumUtilsPhone(InterfaceSeleniumUtils):
    def __init__(self, device) -> None:
        super().__init__()
        self.device = device
    
    def set_up(self):
        self.set_options()
        self.set_services()
        self.driver = webdriver.Chrome(service=self.chrome_service, options=self.chrome_options)
        return self.driver
    
    def set_options(self):
        self.chrome_options = Options()
        mobile_emulation = {
            "deviceName": self.device
        }
        self.chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.chrome_options.add_argument("window-size=600,900")
    
    def set_services(self):
        self.chrome_service = Service(self.driver_path)

