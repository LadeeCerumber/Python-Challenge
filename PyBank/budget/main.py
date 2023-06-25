
import csv

# Set the path for the input file
file_path = r"C:\Users\LabUser\Desktop\Classwork\Challenges\Python-Challenge\PyBank\Resources\budget_data.csv"

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = None
profit_loss_change_list = []
greatest_increase_date = ""
greatest_increase_amount = 0
greatest_decrease_date = ""
greatest_decrease_amount = 0

# Open the input file and read the data
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        total_months += 1
        total_profit_loss += profit_loss

        if previous_profit_loss is not None:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_change_list.append(profit_loss_change)

            if profit_loss_change > greatest_increase_amount:
                greatest_increase_amount = profit_loss_change
                greatest_increase_date = date

            if profit_loss_change < greatest_decrease_amount:
                greatest_decrease_amount = profit_loss_change
                greatest_decrease_date = date

        previous_profit_loss = profit_loss

average_profit_loss_change = sum(profit_loss_change_list) / len(profit_loss_change_list)

# print("Financial Analysis")
# print("------------------")
# print(f"Total Months: {total_months}")
# print(f"Total : ${total_profit_loss}")
# print(f"Average Change: ${average_profit_loss_change:.2f}")
# print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
# print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")



# Exporting the results to a text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average Change: ${average_profit_loss_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")

# Print the results to the console
with open(output_file, "r") as file:
    print(file.read())



