#NAME OF PROGRAM: JamEx Limited Commission Information
#Author: Nashay Kelly
#Date Created: April 27, 2022
#Course: ITT103
#Purpose: This program describes the commission of each sales person of each class.
    
check=int(1)

while check > 0:
    saleID_Num=int(input("What is the special salesperson ID number? "))
    comm_class=int(input("Indicate the salesperson's class. "))
    sales_amount=float(input("What is the total amount of sales? "))

    if comm_class == 1:
        if sales_amount == 1000 or sales_amount< 1000:
            commission_rate = 6/100
        elif sales_amount > 1000 and sales_amount < 2000:
                commission_rate = 7/100
        else:
                commission_rate = 10/100        

    if comm_class == 2:
        if sales_amount < 1000:
            commission_rate = 4/100
        else:
            commission_rate = 6/100

    if comm_class == 3:
            commission_rate = 4.5/100
    elif comm_class !=3 and comm_class != 2 and comm_class !=1:
            print("The class entered does not have an allocated commission rate.")

    if comm_class > 0 and comm_class < 4:
        commission=float(commission_rate * sales_amount)
        print("Saleperson number", saleID_Num, "in class", comm_class, "has earned commission of", commission, "with commission rate of", commission_rate)
    
    check=int(input("To terminate the program, please enter the number zero. To continue, enter a number greater than zero. ")) 

print("The program has now been terminated.")

