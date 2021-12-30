import json
import time
import requests
import redis
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


connection = redis.Redis("pythonfinalproject_redis_1")


def get_data(base_url, id):
    URL = base_url + f"/{id}"
    try:
        response = requests.get(URL)
    except requests.exceptions.RequestException as e:
        logger.error("Connection error %s", e)
    else:
        data = response.json()
        data["timestamp"] = time.time()
        connection.lpush(f"patient_{id}", json.dumps(data))
