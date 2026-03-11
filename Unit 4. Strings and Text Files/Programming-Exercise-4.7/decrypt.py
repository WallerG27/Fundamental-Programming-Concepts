#Implementation of bits2string method 

def bits2String (b=''):
    return chr (int (b,2) - 1)
#Implementation of shift method 
def shift (n=''):
    temp = list (n)
    new = (temp [-1:] + temp[0:-1])
    ret = ''
    for i in new:
        ret += i
    return ret

#Get the input from user
coded = input('Enter the coded text: ')
#split the code
process = coded.split()
decoded = ''
for q in process:
    decoded += bits2String (shift (q))
#Display the decoded message print (decoded)
print(decoded)
