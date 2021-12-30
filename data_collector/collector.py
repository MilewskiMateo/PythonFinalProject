import json
import time
import requests
import redis
import logging
from rq import Queue

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def get_data(base_url, id):
    pass


class DataCollector:
    def __init__(self, base_url, connection: redis.Redis):
        self.base_url = base_url
        self.connection = connection
        self.queue = Queue(name="patient_data", connection=connection)

    def run(self):
        logger.info("Data collector started running")
        while True:
            for id in range(1, 7):
                self.queue.enqueue(get_data, self.base_url, id, result_ttl=0)
            self.delete_data()
            time.sleep(1)

    def delete_data(self):
        for id in range(1, 7):
            last_element = self.connection.lindex(f"patient_{id}", -1)
            while self._is_element_expired(last_element):
                self.connection.rpop(f"patient_{id}")
                last_element = self.connection.lindex(f"patient_{id}", -1)

    def _is_element_expired(self, element):
        if element is None:
            return False
        data = json.loads(element)
        return data["timestamp"] < (time.time() - 10 * 60)
