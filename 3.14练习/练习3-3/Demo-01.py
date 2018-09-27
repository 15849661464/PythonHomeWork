'''
    打印图案 
    +----+----+
    |
    |
    |
    |
    +----+

'''


def print_table():
    for i in range(11):
        if(i==0 or i == 5 or i==10):
            print("+----+----+")
        else:
            print("|    |    |")

print_table()
