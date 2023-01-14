import csv
import os

print("Financial Analysis")
print("----------------------------")

total_months = 0
greatest_decrease = 0
greatest_increase = 0
last_profit = 0
#total_
with open('Resources/budget_data.csv') as data_file:
    csvreader = csv.reader(data_file)
    next(csvreader)

    for row in csvreader:
        total_months += 1
        
        if int(row[1]) > last_profit and int(row[1]) - last_profit > greatest_increase:
            greatest_increase = (int(row[1]) - last_profit)
        if int(row[1]) < last_profit and last_profit - int(row[1]) < greatest_decrease:
            greatest_decrease = (last_profit - int(row[1]))
        #print(row[1])
        last_profit = int(row[1])



print(f"Total Months: {total_months}" )
print(f"Greatest Increase in Profits: {greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease}")





