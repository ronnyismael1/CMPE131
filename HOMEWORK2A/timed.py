import time

def count(func):
    def wrapper(*args, **kwargs):
        stri = "Total time "
        temp = func(*args, **kwargs)
        print (stri,temp)
    return wrapper

@count
def timeme(t):
    # time.sleep(2)
    t = time.time() - t
    return (t)
    
timeme(time.time())