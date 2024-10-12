from abc import abstractmethod, ABC

class InterfaceSeleniumUtils(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.driver = None
        self.driver_path = "chromedriver.exe"
        self.chrome_services = None
        self.chrome_options = None
    
    @abstractmethod
    def set_up(self):
        pass
    
    @abstractmethod
    def set_options(self):
        pass

    @abstractmethod
    def set_services(self):
        pass