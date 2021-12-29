from time import sleep
from const import BASE_URL
import requests


class DataCollector:
    def __init__(self, base_url):
        self.base_url = base_url

    def run(self):
        while True:
            for id in range(1, 7):
                self.get_data(id)
            self.delete_data()
            sleep(2)

    def get_data(self, id):
        URL = self.base_url + f"/{id}"
        data = requests.get(URL)
        print(data.json())

    def delete_data(self):
        pass


data_collector = DataCollector(base_url=BASE_URL)
