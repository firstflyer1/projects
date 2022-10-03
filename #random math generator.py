#random math generator


#functions

def addition():
    count = 0
    correctCount = 0

    while True:    
        import random

        num1 = random.randint(0,50)
        num2 = random.randint(0,50)
        aoperation = '+'
        addsolution = eval(str(num1) + aoperation + str(num2))


        print('What is',num1, '+',num2)
        a = int(input('Please enter your answer. '))
        
        if a == addsolution :
            count = count +1
            correctCount = correctCount +1
            print('You are correct! Would you like to solve another? ')
            aChoice = input()
            if aChoice == 'yes' or aChoice == 'Yes':
                continue

            elif aChoice == 'no' or aChoice == 'No':
                print('Goodbye you got ' + str(correctCount) + ' out of ' + str(count) + ' correct.')
                main()
                break

            else:
                print('Please select yes or no.')
                
        else:
            count = count +1
            print('You are incorrect. The correct answer is ' + str(addsolution) + '. Would you like to solve another? ')
            aChoice = input()
            if aChoice == 'yes' or aChoice == 'Yes':
                continue

            elif aChoice == 'no' or aChoice == 'No':
                print('Goodbye you got ' + str(correctCount) + ' out of ' + str(count) + ' correct.')
                main()
                break

            else:
                print('Please select yes or no.')
                


def subtraction() :
    count = 0
    correctCount = 0

    while True:    
        import random

        num1 = random.randint(50,100)
        num2 = random.randint(0,50)
        aoperation = '-'
        solution = eval(str(num1) + aoperation + str(num2))


        print('What is',num1, '-',num2)
        a = int(input('Please enter your answer. '))
        
        if a == solution :
            count = count +1
            correctCount = correctCount +1
            print('You are correct! Would you like to solve another? ')
            aChoice = input()
            if aChoice == 'yes' or aChoice == 'Yes':
                continue

            elif aChoice == 'no' or aChoice == 'No':
                print('Goodbye you got ' + str(correctCount) + ' out of ' + str(count) + ' correct.')
                main()
                break

            else:
                print('Please select yes or no.')
               
        else:
            count = count +1
            print('You are incorrect. The correct answer is ' + str(solution) + '. Would you like to solve another? ')
            aChoice = input()
            if aChoice == 'yes' or aChoice == 'Yes':
                continue

            elif aChoice == 'no' or aChoice == 'No':
                print('Goodbye you got ' + str(correctCount) + ' out of ' + str(count) + ' correct.')
                main()
                break

            else:
                print('Please select yes or no.')
                


def division():

    count = 0
    correctCount = 0

    while True:    
        import random

        num1 = random.randint(25,50)
        num2 = random.randint(1,20)
        aoperation = '/'
        solution = eval(str(num1) + aoperation + str(num2))


        print('What is',num1, '/',num2)
        a = int(input('Please enter your answer. '))
        
        if a == solution :
            count = count +1
            correctCount = correctCount +1
            print('You are correct! Would you like to solve another? ')
            aChoice = input()
            if aChoice == 'yes' or aChoice == 'Yes':
                continue

            elif aChoice == 'no' or aChoice == 'No':
                print('Goodbye you got ' + str(correctCount) + ' out of ' + str(count) + ' correct.')
                main()
                break

            else:
                print('Please select yes or no.')
                
        else:
            count = count +1
            print('You are incorrect. The correct answer is ' + str(solution) + '. Would you like to solve another? ')
            aChoice = input()
            if aChoice == 'yes' or aChoice == 'Yes':
                continue

            elif aChoice == 'no' or aChoice == 'No':
                print('Goodbye you got ' + str(correctCount) + ' out of ' + str(count) + ' correct.')
                main()
                break

            else:
                print('Please select yes or no.')
                



def multiplication():


    count = 0
    correctCount = 0

    while True:    
        import random

        num1 = random.randint(0,12)
        num2 = random.randint(0,12)
        aoperation = '*'
        solution = eval(str(num1) + aoperation + str(num2))


        print('What is',num1, '*',num2)
        a = int(input('Please enter your answer. '))
        
        if a == solution :
            count = count +1
            correctCount = correctCount +1
            print('You are correct! Would you like to solve another? ')
            aChoice = input()
            if aChoice == 'yes' or aChoice == 'Yes':
                continue

            elif aChoice == 'no' or aChoice == 'No':
                print('Goodbye you got ' + str(correctCount) + ' out of ' + str(count) + ' correct.')
                main()
                break

            else:
                print('Please select yes or no.')
                
        else:
            count = count +1
            print('You are incorrect. The correct answer is ' + str(solution) + '. Would you like to solve another? ')
            aChoice = input()
            if aChoice == 'yes' or aChoice == 'Yes':
                continue

            elif aChoice == 'no' or aChoice == 'No':
                print('Goodbye you got ' + str(correctCount) + ' out of ' + str(count) + ' correct.')
                main()
                break

            else:
                print('Please select yes or no.')
               




def main():
    myList = []
    while True:
        operation = input('''
    Please select the operator you would like to solve.
[1] Addition
[2] Subtraction
[3] Division
[4] Multiplication
[5] Exit
    
''')
    
        if operation == '1':
            addition()
       
        elif operation == '2':
            subtraction()
        
        elif operation == '3':
            division()
        
        elif operation == '4':
            multiplication()
       
        elif operation == '5':
            exit()

        else:
            print('Please select a menu option. ')





#main block

print('Welcome to my random math generator! What is your name? ')
userName = input()

print('Hi ' + userName + '! Would you like to solve some math questions? ')
userChoice = input()

while True:
    if userChoice == 'yes' or userChoice == 'Yes':
        main()
        break
    elif userChoice == 'no' or userChoice == 'No' :
        print('Goodbye!')
        exit()

    else: 
        print('Please select yes or no.')
        