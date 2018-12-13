import os
import csv

pybank_path = os.path.join("documents","pybank.csv")

#Set variables for Financial Analysis
total_months = 0
total_profit_loss = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_inc = ['', 0]
greatest_dec = ['', 99999999999]


with open(pybank_path,newline="") as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:
        #Sum of All Months
        total_months += 1
        #Find Profit/Loss Total
        total_profit_loss += int(row["Profit/Losses"])

        #Determine average change in profit/losses between months
        rev_change = int(row["Profit/Losses"])- prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [rev_change]
        month_of_change = month_of_change + [row["Date"]]

        #The greatest increase in revenue 
        if rev_change > greatest_inc[1]:
            greatest_inc[1]= rev_change
            greatest_inc[0] = row['Date']

        #Greatest decrease in revenue 
        if rev_change < greatest_dec[1]:
            greatest_dec[1]= rev_change
            greatest_dec[0] = row['Date']


#Print Results
rev_avg = sum(revenue_change_list)/len(revenue_change_list)


print('Average Change in Revenue: $ ' + str(rev_avg))
print("Total Months: " + str(total_months))
print("Total Revenue: $ " + str(total_profit_loss))
print(greatest_inc)
print(greatest_dec)

#Write for Text File
output_file = os.path.join("documents","pybank.txt")

with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_profit_loss)
    file.write("Average Revenue Change $%d\n" % rev_avg)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_inc[0], greatest_inc[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_dec[0], greatest_dec[1]))


