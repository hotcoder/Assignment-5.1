'''
Created on Nov 20, 2017

@author: z002krv
'''
'''
Divided by Zero Error handling with Try and Except
'''

def testTryExcept():
    try:
        5/0
    except ZeroDivisionError:
        print("Please provide valid number as second argument in the division operation")
        
        
testTryExcept()