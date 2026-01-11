# task
number = int(input("Enter a number "))
bit_size = int(input("Enter the bit size "))
# get the base binary. Looked online, and you have things like bin() but thats fine
def convertToBinary(bit_size,number):
    res_str = ""
    for i in range(bit_size):
        if number & 1 << i != 0:
            res_str += '1'
            continue
        res_str += '0'
    return res_str[::-1]


res_str = convertToBinary(bit_size,number)
print(res_str)
res_str2 = ""
for i in res_str:
    if i == '1': res_str2 += '0'
    else: res_str2 += '1'
print(res_str2)
number = int(res_str2, 2) + 1
print(convertToBinary(bit_size,number))
