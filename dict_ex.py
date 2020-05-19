phone_dic = {}
name_lst = []
num = int(input())

# Loading the Phone book dictionary
for i in range(num):
    p, n = input().split(' ')
    phone_dic[p] = n

# Getting the input from the User for querying the phone numbers
while True:
    try:
        name = input()
        if len(name) == 0:
            break
    except EOFError: # Breaking out of the loop when EOF - eno of file has been inputted.
        break
    else:
        name_lst.append(name)

for item in name_lst:
    if item in phone_dic:
        print(f'{item}={phone_dic[item]}')
    else:
        print('Not found')
