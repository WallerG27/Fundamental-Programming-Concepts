# Put your code here
#This is a comment.
def main():
    inFile = input("Enter the input file name: ")
    sum, amount = 0,0
    with open(inFile, 'r') as f:
        for line in f:
            for num in line.strip().split():
                sum += float(num)
                amount += 1
        print("\nThe average is " + str(sum / amount))

main()
