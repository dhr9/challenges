a = 1000
b = 1000
c = 1000
d = 1000

def main():
    global a,b,c,d
    print("=======================")
    username = input("Welcome to the banking service.\nEnter the user name:\n")
    if(username not in ["a","b","c","d"]):
        print("Unknown User. Terminating Operation")
        return
    if(username=="a"):
        a += get_operation_result(a)
    if(username=="b"):
        b += get_operation_result(b)
    if(username=="c"):
        c += get_operation_result(c)
    if(username=="d"):
        d += get_operation_result(d)
    print("a =>",a,", b =>",b,", c =>",c,", d =>",d)

def get_float_input(prompt):
    a = input(prompt)
    try:
        return float(a)
    except:
        print("Please enter a valid Number.")
        return get_float_input(prompt)

def do_with_operation(operation, prefix="Enter"):
    if(operation=="1"):
        amount = get_float_input(prefix+" the amount to be deposited:\n")
        return amount
    if(operation=="2"):
        amount = get_float_input(prefix+" the amount to be withdrawal:\n")
        if(amount>a):
            print("Withdrawal amount cannot be greater than bank balance. Terminating Operation")
            return 0
        return -amount
    return None

def get_operation_result(a):
    operation = input("Enter 1 for deposit and 2 for withdrawal:\n")
    o = do_with_operation(operation)
    if(o is None):
        print("This operation code does not exist. Terminating Operation")
        return 0
    p = do_with_operation(operation, "Re-enter")
    if(p is not None) and (p==o):
        return p
    print("The amounts did not match. Terminating Operation")
    return 0

while(True):
    main()
