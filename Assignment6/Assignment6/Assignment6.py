# ----------------------------------------------------------------------
# Assignment Name: Assignment 6 - Functions 
# Name:             Chase Owens
# Date:             9/21/2021
# ----------------------------------------------------------------------



# ----------------------------------------------------------------------
# Function Name:        Display Instructions
# Function Purpose:     Displays a message
# ----------------------------------------------------------------------
def DisplayInstructions ():
    
    # printing the message
    print ("This program will demonstrate how to make and use procedures in Python...",
           " In addition it will demonstrate how to pass values and variables into",
           " a procedure as parameters.  It will demonstrate Python deals with ByRef and ByVal.\n")
    # returning it
    return



# ----------------------------------------------------------------------
# Function Name:        
# Function Purpose:     
# ----------------------------------------------------------------------
def DisplayMessage (intPrintCount):
    # local variable in function 
    intCount = 1
    # while loop, printing the message intPrintCount amount of times
    while intCount <= intPrintCount:
        # the message
        print("I Love Football\n")
        # adding 1 to intCount
        intCount += 1
    # return the message
    return



# ----------------------------------------------------------------------
# Function Name:        Get Larger Value
# Function Purpose:     Get the largest value given
# ----------------------------------------------------------------------
def GetLargerValue(intValue1, intValue2):
    # local variable in function
    intLargerNum = int(0)
    # validation
    try:
        # making sure the values passed in are integers
        intValue1 = int(intValue1)
        intValue2 = int(intValue2)
        # then making sure the values passed in are greater than 0
        if(intValue1 > 0 and intValue2 > 0):
            # finding what value is largest
            if intValue1 > intValue2:
                intLargerNum = intValue1
            else:
                intLargerNum = intValue2
            # saying strFlag is a global variable and setting it to true
            global strFlag
            strFlag = True
        else:
            # if its not greater than zero, shoots this message
            print("The Values Must Be Positive.")
    # if it is not a integer then shoots this error message
    except ValueError:
        intValue1 = 0
        intValue2 = 0
        print("The Values Must Be Numeric.")
    # all is good returns the larger value
    return intLargerNum



# ----------------------------------------------------------------------
# Function Name:        Get Largest Value
# Function Purpose:     Get the largest value given from seven
# ----------------------------------------------------------------------
def GetLargestValue(intValue1, intValue2, intValue3, intValue4, intValue5, intValue6, intValue7):
    # local variable in function
    intLargestNum = int(0)
    # validation
    try:
        # making sure the values passed in are integers
        intValue1 = int(intValue1)
        intValue2 = int(intValue2)
        intValue3 = int(intValue3)
        intValue4 = int(intValue4)
        intValue5 = int(intValue5)
        intValue6 = int(intValue6)
        intValue7 = int(intValue7)
        # then making sure the values passed in are greater than 0
        if(intValue1 > 0 and intValue2 > 0 and intValue3 > 0 and intValue4 > 0 and intValue5 > 0 and intValue6 > 0 and intValue7 > 0):
            # finding what value is largest
            if intValue1 > intValue2 and intValue3 and intValue4 and intValue5 and intValue6 and intValue7:
                intLargestNum = intValue1
            elif intValue2 > intValue3 and intValue4 and intValue5 and intValue6 and intValue7:
                intLargestNum = intValue2
            elif intValue3 > intValue4 and intValue5 and intValue6 and intValue7:
                intLargestNum = intValue3
            elif intValue4 > intValue5 and intValue6 and intValue7:
                intLargestNum = intValue4
            elif intValue5 > intValue6 and intValue7:
                intLargestNum = intValue5
            elif intValue6 > intValue7:
                intLargestNum = intValue6
            else:
                intLargestNum = intValue7
            # saying strFlag2 is a global variable and setting it to true
            global strFlag2
            strFlag2 = True
        else:
            # if its not greater than zero, shoots this message
            print("The Values Must Be Positive.")
    # if it is not a integer then shoots this error message
    except ValueError:
        intValue1 = 0
        intValue2 = 0
        intValue3 = 0
        intValue4 = 0
        intValue5 = 0
        intValue6 = 0
        intValue7 = 0
        print("The Values Must Be Numeric.")
    # all is good returns the largest value
    return intLargestNum



# ----------------------------------------------------------------------
# Function Name:        Get Largest Value
# Function Purpose:     Get the largest value given from seven
# ----------------------------------------------------------------------
def CalculateSphereVolume (intDiameter):
    # local variable in function
    intVolumeSphere = int(0)
    # validation
    try:
        # making sure the values passed in are integers
        intDiameter = int(intDiameter)
        # then making sure the values passed in are greater than 0
        if(intDiameter > 0):
            # math to get volume 
            intRadius = intDiameter / 2
            intVolumeSphere = 4 / 3 * 3.14 * (intRadius ** 3)
            # saying strFlag3 is a global variable and setting it to true
            global strFlag3
            strFlag3 = True
        else:
            # if its not greater than zero, shoots this message
            print("The Values Must Be Positive.")
    # if it is not a integer then shoots this error message
    except ValueError:
        intDiameter = 0
        print("The Values Must Be Numeric.")
    # all is good returns the volume
    return intVolumeSphere



# ----------------------------------------------------------------------
# Name:             Contorlling Main Code for App.
# Purpose:          Run all the functions 
# ----------------------------------------------------------------------

# 1
# starting the program off with the DisplayInstructions function 
DisplayInstructions()

# 2
# calling on the DisplayMessage function and passing in intPrintCount amount
DisplayMessage(10)

# 3
# variables for getlargeervalue function
intValue1 = int(0)
intValue2 = int(0)
intLargerNumber = int(0)
strFlag = bool(False)

# while loop to make sure everything is true
while strFlag is False:
    intValue1 = input("Enter Value 1: ")
    intValue2 = input("Enter Value 2: ")
    intLargerNumber = GetLargerValue(intValue1, intValue2)

# prints message and the larger value 
print("The Larger Number of the two Values is", intLargerNumber,"\n")

# 4
# variables for getlargestvalue function
intValue1 = int(0)
intValue2 = int(0)
intValue3 = int(0)
intValue4 = int(0)
intValue5 = int(0)
intValue6 = int(0)
intValue7 = int(0)
intLargestNumber = int(0)
strFlag2 = bool(False)

# while loop to make sure everything is true
while strFlag2 is False:
    intValue1 = input("Enter Value 1: ")
    intValue2 = input("Enter Value 2: ")
    intValue3 = input("Enter Value 3: ")
    intValue4 = input("Enter Value 4: ")
    intValue5 = input("Enter Value 5: ")
    intValue6 = input("Enter Value 6: ")
    intValue7 = input("Enter Value 7: ")
    intLargestNumber = GetLargestValue(intValue1, intValue2, intValue3, intValue4, intValue5, intValue6, intValue7)

# prints message and the largest value 
print("The Largest Number of the seven Values is", intLargestNumber, "\n")

# 5
# variables for calculatespherevolume function
intDiameter = int(0)
intSphereVolume = int(0)
strFlag3 = bool(False)

# while loop to make sure everything is true
while strFlag3 is False:
    intDiameter = input("Enter Diameter of Sphere: ")
    intSphereVolume = CalculateSphereVolume(intDiameter)

# prints message and the larger value 
print("The Volume of the Sphere is", intSphereVolume)