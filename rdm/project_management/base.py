from abc import ABC, abstractmethod


class BaseBackend(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def pull(self):
        ...
