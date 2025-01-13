import random
import time
import uuid
from queue import Queue


def generate_request(app_queue: "Queue") -> None:
    """Generate request and put it to the queue

    :param app_queue: queue.Queue
    """
    request_id = uuid.uuid4()
    print(f"New request created with id: {request_id}")
    app_queue.put(request_id)


def process_request(app_queue: "Queue") -> None:
    """Process request from the queue

    :param app_queue: queue.Queue
    """
    if not app_queue.empty():
        print("Queue size:", app_queue.qsize())
        request_id = app_queue.get()
        print(f"Processing request: {request_id}")
    else:
        print("Queue is empty")


if __name__ == "__main__":
    application_queue = Queue()
    while True:
        try:
            if random.choice([False, True]):
                generate_request(application_queue)
            if random.choice([False, True]):
                process_request(application_queue)
            time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting")
            break
