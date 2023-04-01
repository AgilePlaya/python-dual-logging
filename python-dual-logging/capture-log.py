import subprocess
import os
from pprint import pprint
import multiprocessing
import time
import inspect


path_file = os.path.join(os.getcwd(), 'python-dual-logging')


def trigger_python(application, arguments, stop):
    print("Triggering {} ...".format(arguments))
    os.system("{} {}".format(application, arguments))
    if stop():
        print("  Exiting loop.")
        return


func = trigger_python
stop_threads = False

# stop_event= threading.Event()
t1 = multiprocessing.Process(target=func, args=(
    "python3", "{}/log_generator_1.py".format(path_file), lambda: stop_threads))
t2 = multiprocessing.Process(target=func, args=(
    "python3", "{}/log_generator_2.py".format(path_file), lambda: stop_threads))

t1.daemon = True
t2.daemon = True

t1.start()
t2.start()
# thread.join()

print(f'Thread 1 still alive? {t1.is_alive()}')
print(f'Thread 2 still alive? {t2.is_alive()}')
time.sleep(12)
pprint(inspect.getmembers(t2))
stop_threads = True
print(f'Thread 1 still alive? {t1.is_alive()}')
print(f'Thread 2 still alive? {t2.is_alive()}')
stop_threads = True


print("End of program.")

# stop_event.set()
os.system("kill -9 {}".format(t2.pid))
print(t2.pid)
