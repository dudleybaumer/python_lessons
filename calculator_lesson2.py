#Instructions: prompt the user for hours and rate per hour to compute gross pay
#PM intructions: get hours, get rate, get pay

hours = raw_input('Enter Hours: ')
rate = raw_input('Enter Rate: ')

pay = float(hours) * float(rate)


print 'Your Gross Pay:', pay



############### updated with regular hours and overtime ############

try:
    hours = raw_input('Enter Hours: ')
    hours = float(hours)
    rate = raw_input('Enter Rate: ')
    rate = float(rate)
except:
    print "Error, please enter numberic input"
    quit()


regularhrs = 40
if hours > 40:
    overhrs = hours - regularhrs
    otrate = rate * 1.5
    otpay = overhrs * otrate
    regpay = 40 * rate
    pay = otpay + regpay
    print 'Regular Pay: ', regpay
    print 'Overtime Pay: ', otpay
    print '-' * 20
    print 'Total Pay: ', pay
else:
    pay = hours * rate
    print 'Regular Pay: ', pay
    print 'You didnt work overtime'


####### excersize 3 in lesson 4 -- add tax ######

try:
    hours = raw_input('Enter Hours: ')
    hours = float(hours)
    rate = raw_input('Enter Rate: ')
    rate = float(rate)
except:
    print "Error, please enter numberic input"
    quit()

def regular_pay(hours, rate):
    return hours * rate

def overtime_pay(othours, rate):
    rate = rate * 1.5
    return othours * rate

def calc_othours(hours):
    return hours - 40

fullweek = 40
if hours > 40:
    othours = calc_othours(hours)
    overtime = overtime_pay(othours, rate)
    regpay = regular_pay(40, rate)
    print 'Regular Pay: ', regpay
    print 'Overtime Pay: ', overtime
    print '---' * 10
    print 'Total Pay: ', regpay + overtime
else:
    print 'Total Pay: ', regular_pay(hours, rate)
