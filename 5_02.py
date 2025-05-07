num=0
values = []
while True:
    line=input("> ")
    if line== "done":
        break
    try:
        pline=float(line)
        values.append(pline)
        
    except:
        print ("enter a valid number.")
    num=num+1

    print("next number please!")
big=max(values)
small=min(values)

print("max = " + str(big) + " min= " + str(small))



'''
sdxjfdahsdjf
ajskdnajsndjas
askdaksn
'''