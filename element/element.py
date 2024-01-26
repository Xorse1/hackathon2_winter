"""Hackathon 2024
"""

import json   # import the json module
import time   # import the time module

# get the the current timestamp
unix_timestamp = int(time.time())
<<<<<<< HEAD:app.py
#We define the list data as a global variable
data=[]
=======

data = []   # empty list for data
>>>>>>> a5b6b45bfa7742af802e1c83bb9a2dbf5960d353:element/element.py

def process_input(u):
    """Program prepares the numbers
    """
    return [int(x.strip()) for x in u]



def analyze_list_elements(input_list):
<<<<<<< HEAD:app.py
    
=======
    """Funtion add numbers to the data list
       and return the sum of the elements of the list
    """

>>>>>>> a5b6b45bfa7742af802e1c83bb9a2dbf5960d353:element/element.py
    for element in input_list:
        
        if element % 2 == 0:
            print(f"{element} is an even number.")
        else:
            print(f"{element} is an odd number.")
        
        data.append(element)

    sum_of_elements = sum(input_list)
<<<<<<< HEAD:app.py
    # Commented out data.remove element in order for data to be equal to sum of elements
    #data.remove(element)
    print("Data :" + str(data))
    
=======
    # data.remove(element)   -> avoid removing last element
    return sum_of_elements  # return the value of sum element
>>>>>>> a5b6b45bfa7742af802e1c83bb9a2dbf5960d353:element/element.py
    print(f"The sum of all elements in the list is: {sum_of_elements}")
    #return the sum of elemnts added
    return sum_of_elements
#Introduced a check if number Function that returns True or False
def check_if_number(input_list_by_user):
    for input in input_list_by_user:
        if input.isnumeric() ==False:
            
            return False        
    return True
        


def main():
<<<<<<< HEAD:app.py
    #Loop an error handling to validate input
    while True:
        try:
            user_input_list = input("Enter a list of numbers separated by commas: ").split(',')
            my_list=process_input(user_input_list)
            break
        except ValueError:
            print("Error: Please Try Again.")        




    #my_list = process_input(user_input_list)
=======
    """This is the driver function
    """
    user_input_list = input("Enter a list of numbers separated by commas: ").split(',')
    my_list = process_input(user_input_list)
>>>>>>> a5b6b45bfa7742af802e1c83bb9a2dbf5960d353:element/element.py

    
    total = analyze_list_elements(my_list)
    print(sum(data))

    if total == sum(data):

        group_name = input("Enter the name of your group: ")

        timestamp_group_name = group_name + str(unix_timestamp)
        
        file_path = f"{timestamp_group_name}_GROUP.json"

        
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)
    else:
        print('Failed')



if __name__ == "__main__":
    main()







