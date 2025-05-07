def computescore (score):
    if score > 1.0 :
        return ("Score invalid.")
    elif score < 0.0:
        return ("Score invalid.")
    elif score >= 0.9 :
        return ('A')
    elif score >= 0.8 :
        return ('B')
    elif score >= 0.7 :
        return("C")
    elif score >= 0.6 :
        return('D')
    elif score <0.6:
        return('F')

iscore = input('Enter Score: ')
try:
    vscore=float(iscore)
    print ("Computing...")    
    grade = computescore(vscore)
    print ("your grade is:", grade)

except:
    print ('Numeral Score is not valid. Please enter a score between 0.0 and 1.0')
    #print('All done')
    
