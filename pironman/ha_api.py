
import requests
from utils import log

class HomeAssistantSupervisorAPI:

    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }


    def request(self, endpoint, data=None):
        try:
            url = f"{self.url}/{endpoint}"
            r = requests.post(url, headers=self.headers)
            log(msg="home assistant request: " + r.text, level='DEBUG')
            return r.json()
        except Exception as e:
            log(msg="home assistant request error: " + e, level='DEBUG')


    def get_ip(self):
        IPs = {}
        data = self.request("network/info")
        interfaces = data["data"]["interfaces"]
        for interface in interfaces:
            name = interface['interface']
            ip = interface['ipv4']['ip_address']
            IPs[name] = ip
        return IPs

    def shutdown(self):
        '''shutdown homeassistant host'''
        log(msg="Shutdown home assistant host", level='DEBUG')
        self.request("host/shutdown")

