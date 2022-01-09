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
        if is_anomaly(data):
            connection.lpush(f"patient_{id}_anomaly", json.dumps(data))
        connection.lpush(f"patient_{id}", json.dumps(data))


def is_anomaly(data: dict):
    sensors_anomaly_values = [
        sensor_data["anomaly"] for sensor_data in data["trace"]["sensors"]
    ]
    return any(sensors_anomaly_values)
