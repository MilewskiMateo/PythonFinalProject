from data_collector import data_collector
from app import app
from threading import Thread

if __name__ == "__main__":
    dash_app_process = Thread(target=app.run_server)
    data_collector_process = Thread(target=data_collector.run)
    data_collector_process.start()
    dash_app_process.start()
    data_collector_process.join()
    dash_app_process.join()
