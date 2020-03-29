# import in dependencies
import csv
import os

input_file = os.path.join('Resources', 'budget_data.csv')

# initialize variables
total_months = 0
net_profit_loss = 0
net_change = []
net_change_months = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999999]

# open data file
with open(input_file, 'r') as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
    
    first_data_row = next(reader)
    total_months = total_months + 1
    prev_profit_loss = int(first_data_row[1])
    net_profit_loss = net_profit_loss + prev_profit_loss

    for record in reader:
        # The total number of months included in the dataset
        total_months = total_months + 1

        # The net total amount of "Profit/Losses" over the entire period
        current_profit_loss = int(record[1])
        net_profit_loss = net_profit_loss + current_profit_loss 
        
        # The average of the changes in "Profit/Losses" over the entire period
        current_net = current_profit_loss - prev_profit_loss
        prev_profit_loss = current_profit_loss
        net_change.append(current_net)
        net_change_months = net_change_months + 1

        # The greatest increase in profits (date and amount) over the entire period
        if current_net > greatest_increase[1]:
            greatest_increase[0] = record[0]
            greatest_increase[1] = current_net

        # The greatest decrease in losses (date and amount) over the entire period
        if current_net < greatest_decrease[1]:
            greatest_decrease[0] = record[0]
            greatest_decrease[1] = current_net

output_path = "analysis.txt"


def print_output(txt_file = None):
    print(total_months, file=txt_file)
    print(net_profit_loss, file=txt_file)
    print(sum(net_change) / net_change_months, file=txt_file)
    print(f"Greatest Increase: {greatest_increase[0]} ${greatest_increase[1]}", file=txt_file)
    print(f"Greatest Decrease: {greatest_decrease[0]} ${greatest_decrease[1]}", file=txt_file)


txt_file = open('analysis.txt', 'w')

print_output()
print_output(txt_file)
