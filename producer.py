from threading import Thread
import random, time

class Producer(Thread):

    def __init__(self, queue, condition):
        super(Producer, self).__init__()
        self.queue = queue
        self.condition = condition

    def run(self):
        nums = range(5)
        while True:
            self.condition.acquire()
            num = random.choice(nums)
            print "Produced", num
            self.queue.append(num)
            self.condition.notify()
            self.condition.release()
            time.sleep(random.random())