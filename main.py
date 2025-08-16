import time
import random

# practicing using a context manager

class DoSomething:
    def __init__(self, nums):
        self.jobs = [0] * nums
        self.start = 0
        self.end = 0

    def __enter__(self):
        self.start = time.perf_counter()
        print(f'Entering time: {self.start}')
        for i in range(len(self.jobs)):
            self.jobs[i] = random.randint(1,11) / 10

        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        print(f'Exiting time: {self.end}')
        t = self.duration_calculator(self.start, self.end) * 1000
        print(f'Program ran for {t:.5f} ms')

        if exc_type:
            print(f'There was an error')
            return True
        
        return False

    @staticmethod
    def duration_calculator(s, e):
        return e - s


def main():
    with DoSomething(5) as tasks:
        tasks_to_run = tasks.jobs
        print(tasks_to_run)
        for i in tasks_to_run:
            time.sleep(i)

if __name__ == "__main__":
    main()
