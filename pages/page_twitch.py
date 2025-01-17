from page_interface import PageInterface

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from datetime import datetime
import traceback

TITLE = "Twitch"
URL = "https://m.twitch.tv/"
SCROLL_TIMES = 2

class PageTwitch(PageInterface):
    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver
        self.set_driver_wait_time()

    def set_driver_wait_time(self, seconds:int = 10) -> None:
        self.driver_wait = wait(self.driver, seconds)

    def wait_get_element(self, locator:str, err_msg:str, by=By.XPATH, ec=EC.element_to_be_clickable):
        try:
            return self.driver_wait.until(ec((by, locator)))
        except:
            print(f"Error wait_get_element: {err_msg}, {traceback.format_exc()}")
            return None

    def expand_the_video_list(self):
        self.wait_get_element('//*[@id="page-main-content-wrapper"]/div/div//section//div/a/p', "Expand Button").click()
        self.wait_get_element('//*[@id="page-main-content-wrapper"]/div/div/div//div/div//div/a/div', "Wait the elements loaded")
    
    def open_page(self):
        self.driver.get(URL)

    def search_on_page(self, value:str):
        self.wait_get_element("//a[contains(@href, '/search')]", "Search Button").click()
        search_box = self.wait_get_element("//input[@type='search']", "Search Box", ec=EC.presence_of_element_located)
        search_box.send_keys(value)
        search_box.send_keys(Keys.ENTER)

    def page_scroll_down(self, scroll_times:int) -> None:
        for _ in range(scroll_times):
            self.driver.execute_script("window.scrollBy(0, 100);")

    def select_streamers(self) -> None:
        videos = self.driver.find_elements(By.XPATH, "//div[@role='list']//div/a")
        for video in videos:
            try:
                self.driver_wait.until(EC.element_to_be_clickable(video)).click()
            except:
                continue
        self.wait_get_element('//div/p[contains(text(), "LIVE")]', "Wait Video list loaded", ec=EC.element_to_be_clickable)
        #TODO: assertion streaming video

    def take_screenshot(self, file_name:str, file_path:str = "./screenshots") -> None:
        screenshot_path = f"{file_path}/{file_name}.png"
        self.driver.save_screenshot(screenshot_path)

    def testflow(self):
        """
        TODO: 
            1. Open Url
            2. Click search button
            3. input StarCraft II
            4. Scroll down 2 times
            5. Select one streamer
            6. take screenshot after page loaded
        #! Should handle the popup dialog
        """
        self.open_page()
        self.search_on_page("StarCraft II")
        self.expand_the_video_list()
        self.page_scroll_down(SCROLL_TIMES)
        self.select_streamers()
        #TODO: find popup dialog
        self.take_screenshot(TITLE + datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))
        