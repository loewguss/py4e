##n = 10
##while True:
 ##   print(n, end=' babacoa ')
 ##   n -= 1
 ##   if n == 0:
 ##       break

num=0
tot=0.0

while True:
    line=input("> ")
    if line== "done":
        break
    try:
        pline=float(line)
        #print(pline)
    except:
        print ("enter a valid number.")
    num=num+1
    tot=tot+pline


    print("next number please!")
avg=tot/num
print("total= " + str(tot) + " count= " + str(num) + " avg= " + str(avg))