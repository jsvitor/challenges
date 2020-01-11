'''
what is the output of the following code?
'''
def usingAll(num_list):
    if all([i > 10 for i in num_list]):
        print("True")
    else:
        print("False")

num_list = [25, 16, 35, 42, 87]
usingAll(num_list)