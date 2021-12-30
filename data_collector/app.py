from const import BASE_URL
import redis

from collector import DataCollector

if __name__ == "__main__":
    redis_connection = redis.Redis(host="pythonfinalproject_redis_1")
    data_collector = DataCollector(base_url=BASE_URL, connection=redis_connection)
    data_collector.run()
