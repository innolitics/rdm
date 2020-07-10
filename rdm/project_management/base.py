class BaseBackend:
    def __init__(self, config):
        self.config = config

    def pull(self):
        raise NotImplementedError()
