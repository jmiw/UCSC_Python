#calculatePay
def calculatePay(rate, workHours):
    if workHours <= 40 :
        totalPay = workHours * rate

    elif workHours > 40 and workHours <= 60:
        extraHours = workHours - 40

        regularPay = 40 * rate
        extraPay = extraHours * (rate * 1.50)
        totalPay = regularPay + extraPay
    else:
        extraHours = workHours - 60

        regularPay = 40 * rate
        extraPay = extraHours * (rate * 2.00) + 20 * (rate * 1.50)
        totalPay = regularPay + extraPay

    return totalPay

#main

pay1 = calculatePay(30,20)
pay2 = calculatePay(15.5,50)
pay3 = calculatePay(11,70.25)

print 'You worked 20 hours at a rate of 30 per hour, you will be paid $', pay1
print 'You worked 50 hours at a rate of 15.5 per hour, you will be paid $', pay2
print 'You worked 70.25 hours at a rate of 11 per hour, you will be paid $', pay3


rate = raw_input('Please enter the rate per hour:')
rate = float(rate)
hours = raw_input('Please enter the number of hours:')
hours = float(hours)

totalPay = calculatePay(rate, hours)
print 'You worked', hours, 'hours at a rate of', rate, 'per hour, you will be paid $', totalPay
