import time

iterations = 1
while True:
    print("Iteration 1_{} : Program 1 running".format(iterations))
    time.sleep(2)
    if iterations >= 5:
        break
    else:
        iterations += 1

print("Program 1 completed !!!")
