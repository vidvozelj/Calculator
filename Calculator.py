chosen_operation = input('''Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
Pleas enter the operation here:  ''')

chosen_first_number = input('Input first number: ')
chosen_second_number = input('Input second number: ')

def Calculator(operation, first_number, second_number):
    operations = ['+', '-', '*', '/']
    if operation not in operations:
        output  = 'invalid operation input'
    elif not first_number.isdigit():
        output  = 'invalid first number input'
    elif not second_number.isdigit():
        output  = 'invalid second number input'   
    else:
        first_number_int = int(first_number)
        second_number_int = int(second_number)
        if operation == '+':
            output  = first_number_int + second_number_int
        elif operation == '-':
            output   = first_number_int - second_number_int
        elif operation == '*':
            output   = first_number_int * second_number_int
        elif operation == '/':
            if second_number_int == 0:
                output  = "Can't devide by zero"
            else:
                output  = first_number_int / second_number_int
    return output

print(Calculator(chosen_operation, chosen_first_number, chosen_second_number))