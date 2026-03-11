# Put your code here
#This is a comment.
import os, os.path

# Example usage
def main():
    displayFiles(os.getcwd())

def displayFiles(path):
    if os.path.isfile(path):  
        print("File name: " + path)
        f = open(path, 'r')
        print(f.read())

    else: 
        print("Directory name: " + path)
        lyst = os.listdir(path)
        for element in lyst: displayFiles(element) 
    
        #print("Invalid pathname")
if __name__ == "__main__":
    main()
