# system imports
# self imports
# third party imports

class Module:
    def __init__(self, wakanda_api):
        from wakanda_api.wakanda_api import WakandaAPI
        self.wakanda_api: WakandaAPI = wakanda_api

