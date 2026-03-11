# Put your code here
#This is a comment.
bits = input(str("Enter a string of bits: "))
end = len(bits)

if len(bits) > 1:
    finalBits = bits[1:(end)] + bits[0]
print(finalBits)
