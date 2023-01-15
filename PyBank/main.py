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

Average_PnL_change = round(sum(Cumulative_PnL_change)/(len(Cumulative_PnL_change)),2)
greatest_decrease = -greatest_decrease 

output_path = os.path.join("analysis", "financial_analysis.csv")

with open(output_path, 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(["Total Months", "Total", "Average Change","Greatest Increase in Profits", "Greatest Decrease in Profits"])
    csv_writer.writerow([total_months, total_profit, Average_PnL_change, (date_greatest_increase, greatest_increase), (date_greatest_decrease, greatest_decrease)])
    #csv_writer.writerow("a", "B", "c", "d", "d")
print(f"Total Months: {total_months}" )
print(f"Total: ${total_profit}")
print(f"Average Change: ${Average_PnL_change}")
print(f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})")