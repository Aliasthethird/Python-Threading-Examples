# Base on
# https://realpython.com/intro-to-python-threading/
import logging
import threading
import time
import concurrent.futures
import random

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
        random.seed()

    def locked_update(self, name):
        random_sleep_time = random.random()        
        logging.info("Thread %s: starting update, Sleep time is %f", name, random_sleep_time)
        time.sleep(random_sleep_time) # randomize thread execution time
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1       
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for index in range(10):
            executor.submit(database.locked_update, index)
    logging.info("Testing update. Ending value is %d.", database.value)