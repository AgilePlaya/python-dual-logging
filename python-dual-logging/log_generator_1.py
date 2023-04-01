import time

iterations = 1
while True:
    print("Program 1 running")
    time.sleep(5)
    if iterations > 30:
        break
    else:
        iterations += 1
