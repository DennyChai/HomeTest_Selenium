from abc import abstractmethod, ABC

class PageInterface(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def testflow(self):
        pass
