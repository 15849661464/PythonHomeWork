
def do_twice(func,value):
    func(value)
    func(value)

def func(value):
    print(value)

do_twice(func,'zuoyan')

