
def do_four(func,arg):
    func(arg)
    func(arg)

def print_twice(arg):
    print(arg)
    print(arg)

do_four(print_twice,'test')

