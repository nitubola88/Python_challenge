# -*- coding: UTF-8 -*-
# Dependencies
import csv
import os

def read_two_columns(filename, col1_index, col2_index):  #using this function to read two coloumns into a list
    budget = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if it exists
        for row in reader:
            budget.append([row[col1_index], row[col2_index]])
    return budget

def calculate_average(numbers): # calculating average change
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)




# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path
filename = file_to_load
# Define variables to track the financial data
total_months = 0
net = 0
# Add more variables to track other necessary financial data
net_change_list=[]
previous_row=0
column1_index = 0  # Index of the first column you want
column2_index = 1  # Index of the second column you want

data = read_two_columns(filename, column1_index, column2_index)  #reading two columns into a list data
length=len(data)
previous=0
net_list= []
i=0 

for i in range(length):
      current=float(data[i][1])
      if previous is not None:
         change=current-previous
         net_list.append(change)  # Track the net change and store in net_list
      previous = current
      net=net+float(data[i][1]) # Track the total




# Calculate the greatest decrease in losses
# for change in net_list:
# Generate the output summary  
greatestincrease=(max(net_list)) # Calculate the greatest increase in profits 
greatestdecrease=(min(net_list)) # Calculate the greatest decrease in losses
i=0
for i in range(len(net_list)):
     if net_list[i]==greatestincrease: 
             # Calculate the index of greatest increase to extract corresponding date
             greatincindex=i
             #print(i)
     if net_list[i]==greatestdecrease:
              # Calculate the greatest decrease in losses to extract corresponding date
             greatdecindex=i
             #print(i)

  
   
net_list.pop(0)
#removing first value thst was default because of no change in first row
average = calculate_average(net_list)  # Calculate the average net change across the months

# Print the output

print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total months: {length}')
print(f'Total: {int(net)}')
print(f"Average Change: ${round(average,2)}") 
print(f'Greatest Increase in Profits:  {data[greatincindex][0] } (${int(greatestincrease)}) ')
print(f'Greatest Decrease in Profits:  {data[greatdecindex][0] } (${int(greatestdecrease)}) ')

# Write the results to a text file
with open(file_to_output, 'w') as csvfile:

    csvfile.write(f'Financial Analysis')
    csvfile.write('\n')
    csvfile.write(f'----------------------------')
    csvfile.write('\n')
    csvfile.write(f'Total months: {length}')
    csvfile.write('\n')
    csvfile.write(f'Total:  ${int(net)}')
    csvfile.write('\n')
    csvfile.write(f"Average Change: ${round(average,2)}") 
    csvfile.write('\n')
    csvfile.write(f'Greatest Increase in Profits:  {data[greatincindex][0] } (${int(greatestincrease)}) ')
    csvfile.write('\n')
    csvfile.write(f'Greatest Decrease in Profits:  {data[greatdecindex][0] } (${int(greatestdecrease)}) ')


