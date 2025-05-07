
def computepay(hours,rate,):
    if hours <= 40.0:
        pay = hours*rate
    else:
        pay = ((vhour-40)*1.5 + 40)*vrate
    return pay

eh = input ("enter the amount of hours worked: ")
vhour = float(eh)
er = input ("enter the rate per hour: ")
vrate = float(er)



vpay= computepay(vhour, vrate)
print("your payment is: ", vpay)