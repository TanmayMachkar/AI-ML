import time
import threading

def calc_square(numbers):
    print("Calculate square of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Square: ", n*n)
        
def calc_cube(numbers):
    print("Calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Cube: ", n*n*n)
        
arr = [2, 3, 8, 9]

t = time.time()
t1 = threading.Thread(target = calc_square, args = (arr, ))
t2 = threading.Thread(target = calc_cube, args = (arr, ))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done in: ", time.time() - t)