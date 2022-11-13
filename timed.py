import time
def timeme(func):
    def wrapper():
        x = time.time()
        func()
        y = time.time()
        print("Total time ",y-x)
    return wrapper
