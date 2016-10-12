from threading import Thread
import random, time

class Consumer(Thread):
    def __init__(self, queue, condition, id):
        super(Consumer, self).__init__()
        self.queue = queue
        self.condition = condition
        self.id = id

    def run(self):
        while True:
            self.condition.acquire()
            if not self.queue:
                print "Nothing is in the queue, waiting to be notified..."
                self.condition.wait()
                print "Consumer %s got notified by the producer" % self.id

            num = self.queue.pop(0)
            print "Consumed %d by consumer %s" % (num, self.id)
            self.condition.release()
            time.sleep(random.random())