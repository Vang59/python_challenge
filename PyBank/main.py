# Create a Python script that analyzes the records to calculate each of the following values:
    # Total number of months included in the dataset
    # Net total amount of "Profit/Losses" over the entire period
    # Changes in "Profit/Losses" over the entire period and average of changes
    # Greatest increase in profits (date and amount) over the entire period
    # Greatest decrease in profits (date and amount) over the entire period

# import os and csv
import os
import csv

# Path to collect data 
csvpath=os.path.join("C:/Users/msmar/OneDrive/Desktop/python_challenge/PyBank/Resources/budget_data.csv")

# Lists to store data
date =[]
profits = []
profit_changes=[]
change=[]

# Variables
previous_profit=0
profit_total=0

# Read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        #Add months
        date.append(row[0])
        
        #Add profit
        profits.append(int(row[1]))
          
    # Total number of months in the dataset
    total_months=len(date)
    
    # Net total amount of "Profit/Losses" 
    profit_total=sum(profits)
    
    # Change in "Profit/Losses" and the average of those changes
    for i in range(len(profits)-1):
        change=profits[i+1]-profits[i]
        profit_changes.append(change)
    avg_change=round(sum(profit_changes)/len(profit_changes),2)
    
    # Greatest increase in profits (date and amnount)
    gip=max(profit_changes)
    gip_month=date[profit_changes.index(gip)+1]
    
    # Greatest decrease in profits (date and amount)
    gdp=min(profit_changes)
    gdp_month=date[profit_changes.index(gdp)+1]
    
    # Print results:
    print("Financial Analysis")
    print("-------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${profit_total}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {gip_month} (${gip})")
    print(f"Greatest Decrease in Profits: {gdp_month} (${gdp})")

# Write Analysis file
with open("C:/Users/msmar/OneDrive/Desktop/python_challenge/PyBank/analysis/financial_analysis.txt", "w") as text:
    text.write("Financial Analysis\n")
    text.write("--------------------------------------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Total: ${profit_total}\n")
    text.write(f"Average Change: ${avg_change}\n")
    text.write(f"Greatest Increase in Profits: {gip_month} (${gip})\n")
    text.write(f"Greatest Decrease in Profits: {gdp_month} (${gdp})")