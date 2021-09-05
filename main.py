import os
import shutil
import random
import time

class ATM(object):
    def __init__(self, pin, number, name):
        self.pin = pin
        self.number = number
        self.name = name
        

    def atmUse(self):
        
        
        print(self.number)
        verify = input("If the digits above is your card number please say 'yes' or 'no': ")
        
        if(verify == "yes"):
            use = input("What would you like to do (Please type exactly either 'withdraw' or 'deposit': ")
            if(use == "withdraw"):
                amountW = input("Enter the amount you would like to withdraw: ")
                print("You have deposited " + amountW + ".")
            elif(use == "deposit"):
                amountD = input("Enter the amount you would like to deposit: ")
                print("You have deposited " + amountD + ".")
            else:
                print("Incorrect input.")
       
        else:
            print("Error please try again.")
        
            
ATM1 = ATM(1015,12345678,"Araf")

print(ATM1.atmUse())