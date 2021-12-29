from time import sleep
from const import BASE_URL
import requests
import logging
import redis

redis_connection = redis.Redis()
logger = logging.getLogger(__name__)


class DataCollector:
    def __init__(self, base_url, connection):
        logger.info("Data collector init")
        print("Data collector init")
        self.base_url = base_url
        self.connection = connection

    def run(self):
        logger.info("Data collector started running")
        while True:
            for id in range(1, 7):
                self.get_data(id)
            self.delete_data()
            sleep(2)

    def get_data(self, id):
        URL = self.base_url + f"/{id}"
        try:
            data = requests.get(URL)
        except requests.exceptions.RequestException as e:
            logger.warning("Connection error", e)
        else:
            logger.debug(data.json())

    def delete_data(self):
        pass


if __name__ == "__main__":
    data_collector = DataCollector(base_url=BASE_URL, connection=redis_connection)
    data_collector.run()
