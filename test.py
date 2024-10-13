import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'pages')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils')))

from utils.selenium_utils_phone import SeleniumUtilsPhone
from utils.devices import Devices
from pages.page_twitch import PageTwitch
import time
import imageio
import threading

selenium_utils_phone = SeleniumUtilsPhone(Devices.GALAXY_NOTE_3.value)
driver = selenium_utils_phone.set_up()

screenshot_dir = 'test_gif'
gif_path = 'selenium_test.gif'
os.makedirs(screenshot_dir, exist_ok=True)

class MyThread(threading.Thread):
    def __init__(self, driver, screenshot_dir):
        super().__init__()
        self.stop_flag = threading.Event()
        self.driver = driver
        self.screenshot_dir = screenshot_dir

    def run(self):
        i = 0
        while not self.stop_flag.is_set():
            print("Thread is running...")
            screenshot_path = os.path.join(self.screenshot_dir, f'{i}.png')
            self.driver.save_screenshot(screenshot_path)
            time.sleep(0.1)  # Simulate work
            i += 1
    def stop(self):
        self.stop_flag.set()

thread = MyThread(driver, screenshot_dir)
thread.start()

twitch = PageTwitch(driver)
twitch.testflow()

thread.stop()
thread.join() 


# with imageio.get_writer(gif_path, mode='I', duration=0.5) as writer:
#     for i in range(21):
#         print(i)
#         screenshot_path = os.path.join(screenshot_dir, f"{i}.png")
#         image = imageio.imread(screenshot_path)
#         writer.append_data(image)
# print(f'GIF saved at: {gif_path}')