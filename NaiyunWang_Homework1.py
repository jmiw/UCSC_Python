#pythonForBeginnerCourse_HW1
#A order of ShopOnline

'''
Create a Python file that shows examples of assignment statements, using a total of 16 variables
4 integers
4 floats (numbers with a decimal point)
4 strings
4 booleans
'''

#customerDetail:
nameOfcustomer = "Jamie"                      #string
membership = False                            #boolean
getPromoCode = membership and True            #boolean
OrderNumber = "#1345321"                      #string

#orderDetails:
item1 = "Shoes"                               #string
numOfshoes = 1                                #int
priceOfshoes = 19.99                          #float

item2 = "Tops"                                #string
numOftops = 2                                 #int
priceOftops = 12.99                           #float

item3 = "Pants"                               #string
numOfpants = 4                                #int
priceOfpants = 15.99                          #float

totalAmount = (numOfshoes * priceOfshoes) + (numOftops * priceOftops) + (numOfpants * priceOfpants)   #float
totalItems = (numOfpants + numOfshoes + numOftops)       #int

freeShipping = (totalAmount > 50) and (totalItems > 5)   #boolean
freeToJoinMembership = totalAmount > 100                 #boolean



#Print out the order
print 'Order Number: %s' %(OrderNumber)
print 'Customer Name: %s' %(nameOfcustomer)
print '\n'
print'Customer Info:'
print 'Our Member :', membership
print 'Use PromoCode :', getPromoCode
print 'Free Shipping :', freeShipping
print 'Qualified for Membership :', freeToJoinMembership
print '\n'
print 'Total Items:', totalItems
print item1,':', numOfshoes
print item2, ':', numOftops
print item3, ':' , numOfpants
print 'Shipment Total :', '$', totalAmount


