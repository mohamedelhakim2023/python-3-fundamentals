# Get details of loan from user and calculate the monthly payment

money_owed = float(input("How much money do you owe? \n")) # 50,000
apr = float(input("What is the annual percentage rate? \n")) # 3.5
payment = float(input("What is the monthly payment? \n")) # 1,000
months = int(input("How many months do you want to see results for? \n")) # 24

money_rate = apr/100/12

for i in range(months):
    
    interest_paid = money_owed * money_rate

    money_owed = money_owed + interest_paid
    
    if (money_owed - payment < 0):
        print("The last payment is", payment)
        break

    money_owed = money_owed - payment

    print("Paid", payment, "of which", interest_paid, "was interest.", end=' ')
    print("Now I owe", money_owed)


