import cm as pt
import time

# practicing using a context manager

def main():
    with pt.pointless_tasks(10) as tasks:
        tasks_to_run = tasks.jobs
        print(tasks_to_run)
        for i in tasks_to_run:
            time.sleep(i)

if __name__ == "__main__":
    main()
