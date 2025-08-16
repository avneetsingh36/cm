import time
import random

class pointless_tasks:
    def __init__(self, nums):
        self.jobs = [0] * nums
        self.start = 0
        self.end = 0

    def __enter__(self):
        self.start = time.perf_counter()
        print(f'Entering time: {self.start:.5f}')
        for i in range(len(self.jobs)):
            self.jobs[i] = random.randint(1,11) / 10

        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        print(f'Exiting time: {self.end:.5f}')
        t = self.duration_calculator(self.start, self.end) * 1000
        print(f'Program ran for {t:.5f} ms')

        if exc_type:
            print("Type:", exc_type.__name__)
            print("Value:", exc)
            print("Traceback:")
            print("".join(traceback.format_exception(exc_type, exc, tb)))
            return True

        return False

    @staticmethod
    def duration_calculator(s, e):
        return e - s
