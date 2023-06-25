#import modules
import os
import csv

#set data path
csv_path = os.path.join( r"C:\Users\LabUser\Desktop\Classwork\Challenges\Python-Challenge\PyBank\Resources\budget_data.csv") 
# read csv
with open(csv_path, encoding='UTF-8') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")

    
    header = next(budget_data)
    firstrow = next(budget_data)
    total_net = int(firstrow[1])
    months = 1
    profitlosslist =[]
    for row in budget_data:
        months =months + 1
        profitloss = int(row[1])
        profitlosslist = total_net
        total_net = total_net + profitloss
        
       


    print(months)
    print(total_net)
    


