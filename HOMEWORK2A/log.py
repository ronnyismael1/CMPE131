import time

def count(func):
    def wrapper(*args, **kwargs):
        print("-----------------------")
        print("Below is the timestamp:")
        print("-----------------------")
        print (func(*args, **kwargs))
    return wrapper

@count
def timestamp(t):
    return (t)
    
timestamp(time.ctime())