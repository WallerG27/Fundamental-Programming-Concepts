# Put your code here
#input
price = float(input("Enter the puchase price: "))

#math stuff/output
downPayment = .1
annIntRate = .12
monthPayment = .05

print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")
#month
month = 1

#Starting Balance
StartBal = price * downPayment
price = price - StartBal
#Payment
monthPay = price * monthPayment
toPay = price
while toPay > 0:    
    #Interest to Pay
    IntToPay= price * annIntRate / 12
    #Principal to Pay
    PrinToPay = monthPay - IntToPay
    #Ending Balance
    if price < monthPay:
        PrinToPay = price
        monthPay = PrinToPay
        IntToPay = 0
        EndBal = price - PrinToPay
        toPay = EndBal
    else:
        EndBal = price - PrinToPay
        toPay = EndBal

    #output stuff
    print("%2d%15.2f%15.2f%17.2f%17.2f%17.2f" % (month, price, IntToPay, PrinToPay, monthPay, EndBal))
    price = EndBal
    month += 1
