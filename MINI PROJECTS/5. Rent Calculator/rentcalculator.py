#A rent calculator for bachelers where the rent,electricity,water and food amounts will be calculated 
def getValidInt(prompt):
    while True:
        try: 
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please Enter a valid Number. ")

rent = getValidInt("Enter the rent amount: ")
electricityBill = getValidInt("Enter the electricity Bill: ")
waterBill = getValidInt("Enther the Water Bill: ")
foodCost = getValidInt("Enter the Cost of Food: ")

totalAmount = rent + electricityBill + waterBill + foodCost
print("The total cost on this month is : ",totalAmount)

numofBachelors = getValidInt("Number of Persons in Room/Flat : ")
amountToPay = totalAmount / numofBachelors

print("The amount per person is : ", amountToPay)