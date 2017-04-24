#!/usr/bin/python3


import math
import sys
#import re.macth
import re

def main() :
    GecerliSifre = False
    SifreKalite = False

    while (GecerliSifre and SifreKalite) != True :
        password1 = input("Enter your password: ")

        print ("")

        password2 = input("Re-enter your password: ")

        GecerliSifre = isValidPassword(password1,password2)
        SifreKalite = passwordEqual(password1,password2)

        if GecerliSifre == True and SifreKalite == True :

            print("----------")
            print("That pair of passwords will work.")
            return

        elif GecerliSifre == False :

            print ("----------")
            print ("Your password must be at least 8 chars long")
            print("That password did not have the required properties.")
            print ("-----------")
        else :

            print("----------")
            print("Entered Passwords Don't Match.")
            print("----------")
def isValidPassword(password1,password2) :

      #if password1 >= "a" and password1 <= "z" : hasLower = True:

    #if password1 >= "a" and password1 <= "z" : hasUpper = True:

    #if password1 >= "0" and password1 <= "9" : hasDigit = True:

  #if re.match("(?=.*[A-Za-z]?=.*\d[A-Za-z\d]{8,}$)", password1):


 #if re.match("(?=.*[A-Za-z1-9]?=.*\d[A-Za-z1*-9*\d]{8,1}{8,0}{8,}$)", password2):

    if re.match("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password1) :

        return True

       # re.match(password1)
    else:
        return False


def passwordEqual(password1, password2) :

     if password1 == password2 :
        return True

     else:
        return False
main()



