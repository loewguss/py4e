'''Write a programm that calculate payments asking for 
hours and rates, but the hours can't exceed 45 and rates 10.5. 
Conditionate rates to be nultiplied by 1.5 if the hours exceed 40.'''


hour = input ('Enter the amount of hours ')
vhour = float(hour)

if vhour>45.0:
    print('The amount cannot be over 45')
          #add killswitch
rate = input ('Enter the rate ')
vrate = float(rate)

if vrate > 10.5:
    print('The rate cannot be over 10.5')
     #add killswitch

#payment
if vhour <= 40.0:
    pay = vhour*vrate

else:
    pay = 40*vrate + (1.5*vrate*(vhour-40))

print('Your payment will be: ', pay, '$')
