import pprint
import urllib.request, urllib.parse, urllib.error

from .utils import Backend

class Urllib2Backend(Backend):
    def send(self, url, data):
        urllib.request.urlopen(urllib.request.Request(url, data=urllib.parse.urlencode(data)))

class RequestsBackend(Backend):
    def __init__(self):
        # Lazily import to avoid dependency
        import requests

        self.session = requests.Session()

    def send(self, url, data):
        result = self.session.post(url, data=data, verify=False).json()

        if not result['ok']:
            raise ValueError(result['error'])

class ConsoleBackend(Backend):
    def send(self, url, data):
        print("I: Slack message:")
        pprint.pprint(data, indent=4)
        print("-" * 79)

class DisabledBackend(Backend):
    def send(self, url, data):
        pass
