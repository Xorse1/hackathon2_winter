import json
import time
 
unix_timestamp = int(time.time())
 
def process_input(u):
    return [int(x.strip()) for x in u]
 
data = [] #Initialize an empty list to store data
 
def analyze_list_elements(input_list):
    for element in input_list:
        if element % 2 == 0:
            print(f"{element} is an even number.")
        else:
            print(f"{element} is an odd number.")
 
        data.append(element) #The empty list sorted this
 
    sum_of_elements = sum(input_list)
    print(f"The sum of all elements in the list is: {sum_of_elements}")
 
def main():
    user_input_list = input("Enter a list of numbers separated by commas: ").split(',')
    my_list = process_input(user_input_list)
 
    analyze_list_elements(my_list)
 
    group_name = input("Enter the name of your group: ")
    timestamp_group_name = group_name + str(unix_timestamp)
    file_path = f"{timestamp_group_name}_GROUP.json"
 
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)
 
    print(f"Data saved to {file_path}")
 
if __name__ == "__main__":
    main()