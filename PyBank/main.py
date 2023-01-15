import csv
import os

print("Financial Analysis")
print("----------------------------")

total_months = 0
greatest_decrease = 0
greatest_increase = 0
last_profit = 0
total_profit = 0
Cumulative_PnL_change = []
starter = False

with open('Resources/budget_data.csv') as data_file:
    csvreader = csv.reader(data_file)
    next(csvreader)

    for row in csvreader:
        total_months += 1
        total_profit = total_profit + int(row[1])
        if int(row[1]) > last_profit and int(row[1]) - last_profit > greatest_increase:
            date_greatest_increase = row[0]
            greatest_increase = (int(row[1]) - last_profit)
        if int(row[1]) < last_profit and last_profit - int(row[1]) > greatest_decrease:
            date_greatest_decrease = row[0]
            greatest_decrease = (last_profit - int(row[1]))
        if starter == True:
            Cumulative_PnL_change.append(int(row[1])-last_profit)
        last_profit = int(row[1])
        starter = True

Average_PnL_change = sum(Cumulative_PnL_change)/(len(Cumulative_PnL_change))
greatest_decrease = -greatest_decrease 
print(f"Total Months: {total_months}" )
print(f"Total: {total_profit}")
print(f"Average Change: {Average_PnL_change}")
print(f"Greatest Increase in Profits: {date_greatest_increase} ({greatest_increase})")
print(f"Greatest Decrease in Profits: {date_greatest_decrease} ({greatest_decrease})")