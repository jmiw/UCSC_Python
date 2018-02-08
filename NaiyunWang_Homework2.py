#pythonForBeginnerCourse_HW2
#Cost of A order

def calculateBill(num1, num2, num3):
    subtotal = (3.00 *num1) +\
               (2.00 *num2) +\
               (3.00 *num3)
    tax = subtotal *.10
    totalAmount = subtotal + tax
    return totalAmount

#customer1

bill1 = calculateBill(3, 2, 1)
print 'For customer1, your bill is: $', bill1

#customer2

bill2 = calculateBill(8, 8, 8)
print 'For customer2, your bill is: $', bill2

#customer33
userBurgers = input('How many burgers?')
userBurgers = int(userBurgers)

userDogs = input('How many dogs?' )
userDogs = int(userDogs)

userShakes = input('How many shakes?')
userShakes = int(userShakes)

bill3 = calculateBill(userBurgers, userDogs, userShakes)
print 'For customer3, your bill is: $', bill3

