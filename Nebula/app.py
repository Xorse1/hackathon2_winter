import json
import time

data = [] #defined an empty list to store elements

unix_timestamp = int(time.time())



def process_input(u):
    return [int(x.strip()) for x in u]



def analyze_list_elements(input_list):

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
    user_input_list = input("Enter a list of numbers separated by commas: ").split(',')
    my_list = process_input(user_input_list)

    
    analyze_list_elements(my_list)

    if sum(my_list) == sum(data):

        group_name = input("Enter the name of your group: ")

        timestamp_group_name = group_name + str(unix_timestamp)
        
        file_path = f"{timestamp_group_name}_GROUP.json"

        
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)
    else:
        print('Failed')



if __name__ == "__main__":
    main()







