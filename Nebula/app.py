import json #import the json module
import time #imported the time module

data = [] #defined an empty list "data" as was indicated in the original code to store elements

unix_timestamp = int(time.time())



def process_input(u):
    return [int(x.strip()) for x in u] #takes a list of strings as inputs and converts them to integers



def analyze_list_elements(input_list): #Takes a list of integers as input and iterates over each element in the list

    for element in input_list:
        
        if element % 2 == 0: #Condition to check if number is an even number or odd number
            print(f"{element} is an even number.")
        else:
            print(f"{element} is an odd number.")

        data.append(element) #corrected the indentation to be in the condition
        print(data)

    sum_of_elements = sum(input_list) #Corrected the indentation error properly to be inside the analyze_list_elements 
    #removed the data.remove because it is unnecssary
    print(f"The sum of all elements in the list is: {sum_of_elements}")




def main():
    user_input_list = input("Enter a list of numbers separated by commas: ").split(',') #prompts user to enter a list of numbers
    my_list = process_input(user_input_list)

    
    analyze_list_elements(my_list) #call the analyze function to analyze the elements in "my_list"

    if sum(my_list) == sum(data): #check if sum of original list is equal to sum of processed elements in "data"

        group_name = input("Enter the name of your group: ")

        timestamp_group_name = group_name + str(unix_timestamp)
        
        file_path = f"{timestamp_group_name}_GROUP.json"

        
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)
    else:
        print('Failed')



if __name__ == "__main__":
    main()







