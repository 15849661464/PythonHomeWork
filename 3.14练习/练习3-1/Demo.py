
def right_justify(s):
    temp = '';
    for i in range(70-len(s)):
        temp +=" "
    print(temp+s)
right_justify('monty')
