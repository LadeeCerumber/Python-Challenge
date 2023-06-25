# -*- coding: utf-8 -*-
"""t1 profit and loss.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G-cy9ihv9MdSdP-WR70rRlxf77Q_MtDs
"""

import csv

# Set the path for the input file
file_path = "C:\Users\LabUser\Desktop\Classwork\Challenges\Python-Challenge\PyBank\Resources\budget_data.csv"

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

print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Loss: ${total_profit_loss}")
print(f"Average Change: ${average_profit_loss_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")