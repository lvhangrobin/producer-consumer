from consumer import Consumer
from producer import Producer
from threading import Condition
import signal, os

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    os._exit(0)

def main():

    queue = []
    condition = Condition()


    producer = Producer(queue, condition)
    consumer1 = Consumer(queue, condition, "A")
    consumer2 = Consumer(queue, condition, "B")

    producer.start()
    consumer1.start()
    consumer2.start()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
    signal.pause()
