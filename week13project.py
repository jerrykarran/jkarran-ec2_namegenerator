"""
Jerry Karran
Name generator for departments to use to create unique names for EC2 
instances while incorporating their department name into the name
"""
import random

def generateEc2Name():
    # string with all characters and numbers to use to generate a new random string
    allCharactersAndNumbers = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*{}[]()?<>'
    
    # input for number of names needed and the department
    numberOfEc2Instances = int(input('Enter the number of EC2 instance names needed: '))
    departmentName = input('Enter your department (Marketing, Accounting, and FinOps): ')
    
    # verifying department
    lowercaseDepartmentName = departmentName.lower()
    if lowercaseDepartmentName == 'marketing' or lowercaseDepartmentName == 'accounting' or lowercaseDepartmentName == 'finops':
            newname = departmentName.capitalize() + "-" # adding the department name to the string title
            ec2NumberBeingCreated = 1       # keep track of the number of instance names needed
            print('--------------------------------')
            # create an instance name
            while (numberOfEc2Instances > 0):
                counterDigit = 0
                while (counterDigit < 10): # generate each character up to 10
                    newname += random.choice(allCharactersAndNumbers)
                    counterDigit += 1
                print('EC2', ec2NumberBeingCreated, 'Name: ', newname)
                ec2NumberBeingCreated += 1
                numberOfEc2Instances -= 1
                newname = departmentName.capitalize() + "-"
    else: # error for incorrect departments
        print('Please do not use this name generator if you are not within the correct departments.')
        
generateEc2Name()