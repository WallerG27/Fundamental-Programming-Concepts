
str=input("Enter a message: ")

#converting int to binarydef B2D(binary):	
def B2D(binary):	
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
	    dec = binary % 10
	    decimal = decimal + dec * pow(2, i)
	    binary = binary//10
	    i += 1
    return (decimal)
str_data =' '

#binary to de
for i in range(0, len(str), 7):
	temp_data = int(str[i:i + 7])
	decimal_data = B2D(temp_data)
	str_data = str_data + chr(decimal_data)


end = len(str_data)

if len(str_data) > 1:
    finalBits = str_data[-1] + str_data[0:(end - 1)]
print(finalBits)
