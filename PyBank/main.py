
import os
import csv
from pathlib import Path
input_file = Path("classrepo","python-challenge", "Pybank", "budget_data.csv")

# Create empty lists to

total_months = []
total_profit = []
monthly_profit_change = []
 
with open ('PyBank/budget_data.csv') as csv_file:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(csv_file,delimiter=",") 

    # Skip the header labels 
    header = next(csvreader)  

    # Iterate through the rows in the stored file contents
    for row in csvreader: 

        # append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# i plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output_file = Path("python-challenge","PyBank", "Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

    
