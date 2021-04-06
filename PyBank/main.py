import os
import csv
#Resource file
budget_csv = os.path.join("Resources", "budget_data.csv")

#Initial Lists
date = []
profit = []


#Variable to calcualte profit/change
total_profit = 0.0
count_avg = 0.0
avg_c =0.0
profit_change_total = 0.0

greatest_decrease_profits = 0.0
greatest_increase_profits = 0.0
greatest_increase_counter = 0
greatest_decrease_counter = 0

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
# Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
#Print the header row
    print(f"Header: {csv_header}")

   
    
    # Read through each row of data after the header
    for row in csv_reader:

    # Create list of date and profit
        
        date.append(row[0])
        profit.append(int(row[1]))  
 
    #loop through profit to find out profit change and identify the highest and lowest profit
    for each_profit in range (1, (len(profit))):
        profit_change = (profit[each_profit]) -  (profit[each_profit-1])

        if profit_change > greatest_increase_profits:
            greatest_increase_profits = profit_change
            greatest_increase_counter = each_profit
        elif profit_change < greatest_decrease_profits:
            greatest_decrease_profits = profit_change
            greatest_decrease_counter = each_profit
        #count of profit change
        count_avg = count_avg+1
        #total profit change
        profit_change_total = profit_change_total + profit_change
     
        #Avereage Change
        avg_c = profit_change_total /count_avg
#Start writing the file.
output_path = "Analysis/Financial_Analysis.txt"
with open(output_path, 'w') as text:

    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n")
    text.write("    Total Months: " + str(len(profit)) + "\n")
    text.write("    Total : " + "$" + str(sum(profit)) +"\n")
    text.write("    Average Change: " + '$' + str(round(float(avg_c),2)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(date[greatest_increase_counter]) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(date[greatest_decrease_counter]) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")
   


#print on console/terminal
print("----------------------------------------------------------\n")
print("  Financial Analysis"+ "\n")
print("----------------------------------------------------------\n")
print("    Total Months: " + str(len(profit)) + "\n")
print("    Total : " + "$" + str(sum(profit)) +"\n")
print("    Average Change: " + '$' + str(round(float(avg_c),2)) + "\n")
print("    Greatest Increase in Profits: " + str(date[greatest_increase_counter]) + " ($" + str(greatest_increase_profits) + ")\n")
print("    Greatest Decrease in Profits: " + str(date[greatest_decrease_counter]) + " ($" + str(greatest_decrease_profits) + ")\n")
print("----------------------------------------------------------\n")