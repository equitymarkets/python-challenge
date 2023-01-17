#imports python modules
import csv
import os

#Declares and initializes working variables
total_months = 0
greatest_decrease = 0
greatest_increase = 0
last_profit = 0
total_profit = 0
Cumulative_PnL_change = []
starter = False

#Input Path is based upon running terminal session from PyBank/ folder. Adjust accordingly
with open('Resources/budget_data.csv') as input_file:
    #Sets the reader
    csvreader = csv.reader(input_file)
    #Skips the header row
    next(csvreader)
    #Determines months in set, extreme values, and PnL changes
    for row in csvreader:
        monthly_profit = int(row[1])
        total_months += 1
        total_profit = total_profit + monthly_profit
        if monthly_profit > last_profit and monthly_profit - last_profit > greatest_increase:
            date_greatest_increase = row[0]
            greatest_increase = (monthly_profit - last_profit)
        if monthly_profit < last_profit and last_profit - monthly_profit > greatest_decrease:
            date_greatest_decrease = row[0]
            greatest_decrease = (last_profit - monthly_profit)
        if starter == True:
            Cumulative_PnL_change.append(monthly_profit-last_profit)
        last_profit = monthly_profit
        starter = True

#Prevents divide by zero error and alerts user to empty set
if(total_months == 0):
    print("You have no records in the set. Please check your data.") 
    exit()
else:
    Average_PnL_change = round(sum(Cumulative_PnL_change)/(len(Cumulative_PnL_change)),2)

#turns greatest_decrease into user-friendly negative number
greatest_decrease = -greatest_decrease 

#Sets and creates output path into analysis folder. Path based upon running terminal session from PyBank/ folder. Adjust accordingly 
output_path = os.path.join("analysis", "financial_analysis.csv")
with open(output_path, 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(["Total Months", "Total", "Average Change","Greatest Increase in Profits", "Greatest Decrease in Profits"])
    csv_writer.writerow([total_months, total_profit, Average_PnL_change, (date_greatest_increase, greatest_increase), (date_greatest_decrease, greatest_decrease)])

#Terminal output = Total months of analysis (rows), Total (cumulative) profit, Average chcnge in profit or loss for each month, and extreme increase and decrease
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}" )
print(f"Total: ${total_profit}")
print(f"Average Change: ${Average_PnL_change}")
print(f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})")