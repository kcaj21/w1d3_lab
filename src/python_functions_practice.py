def return_10():
    return 10

def add(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

def length_of_string(a_string):
    result = len(a_string)
    return result

def join_string(string_1, string_2):
    result = string_1 + string_2
    return result

def add_string_as_number(num1, num2):
    result = int(num1) + int(num2)
    return result

def number_to_full_month_name(number):
    month = [  
                "January", 
                "February", 
                "March", 
                "April", 
                "May", 
                "June",
                "July",
                "August",
                "September",
                "October"]

    return month[number-1]

def number_to_short_month_name(number):
    month = [  
                "Jan", 
                "Feb", 
                "Mar", 
                "Apr", 
                "May", 
                "Jun",
                "Jul",
                "Aug",
                "Sept",
                "Oct"]

    return month[number-1]
