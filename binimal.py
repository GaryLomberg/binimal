#! /usr/bin/python3


choice = (Binary to Decimal = B2D, Decimal to Binary = D2B)

if choice == "B2D":
	binary = input("Please input your binary number: ")
	binary_list = []
	decimal = 22
	
	for i in binary:
		binary_list.append(int(i))

def bin2dec(binary_num):
	binary_num = binary_num[::-1]
	decimal = 0
	for i, j in enumerate(binary_num):
		if j == 1:
			decimal += 2**(i)
	return decimal

def dec2bin(dec_num):
	bin_list = []
	while dec_num >= 1:
		if dec_num % 2 == 1:
			bin_list.append(1)
		else:
			bin_list.append(0)
		dec_num = dec_num // 2
	return bin_list[::-1]

# print(bin2dec(binary_list))
print(dec2bin(decimal))
