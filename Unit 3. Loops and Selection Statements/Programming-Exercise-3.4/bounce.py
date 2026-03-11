# Put your code here:
#User Input:
height = int(input("Enter the height from which the ball is dropped: "))
bounce = float(input("Enter the bounciness index of the ball: "))
times = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

#Math stuff
totalDis = height
dropH = height * bounce
for eachPass in range(times):
    totalDis = totalDis + 2 * dropH
    dropH = dropH * bounce
totalDis = totalDis - dropH / bounce   

#
print("Total distance traveled is:", round(totalDis,3), "units.")
