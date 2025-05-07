'''
Write a program to prompt for a score between 0.0 and 1.0.
If the score is out of range, print an error.
If the score is between 0.0 and 1.0, print a grade using the
following table:
'''

score = input('Enter Score: ')
try:
    iscore=float(score)
    
except:
    print ('Numeral Score is not valid. Please enter a score between 0.0 and 1.0')
    print('All done')
    

if iscore > 1.0 :
    print ("Score invalid.")
elif iscore < 0.0:
    print ("Score invalid.")
elif iscore >= 0.9 :
    print('A')
elif iscore >= 0.8 :
    print ('B')
elif iscore >= 0.7 :
    print("C")
elif iscore >= 0.6 :
    print('D')
elif iscore <0.6:
    print('F')

print ("All Done")
