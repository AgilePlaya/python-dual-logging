import time

iterations = 1
while True:
    print("Iteration 2_{} : Program 2 running".format(iterations))
    time.sleep(3)
    if iterations >= 10:
        break
    else:
        iterations += 1

print("Program 2 completed !!!")
