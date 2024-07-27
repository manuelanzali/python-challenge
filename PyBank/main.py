
import os
import csv


# Path to collect data from Resources folder
budgetdata_csv = os.path.join('Resources', 'budget_data.csv')
file_to_create = os.path.join('analysis', 'budget_analysis.text')

# Define the function and have it accept the 'budget_data' as the sole parameter
def print_records(budget_data) :

    date = str(budget_data[0])
    profit_and_losses = int(budget_data[1])

    split_date = date.split("-")
    month = split_date[0]
    day = split_date[1]

    profit = profit_and_losses if profit_and_losses > 0 else 0
    loss = -profit_and_losses if profit_and_losses < 0 else 0

    # return all variables
    return(month)
    return(date)
    return(profit_and_losses)
    return(day)
    return(profit)
    return(loss)

# Calculate the Total Number of Months included in the data set: define file, open, skip header
def total_number_months(csv_file) :
    with open(csv_file,'r') as csv_file :
        csvreader = csv.reader(csv_file)
        next(csvreader)
        total_months = sum(1 for row in csvreader)
    return total_months

total_months = total_number_months(budgetdata_csv)


# Calculate the net total amount of profit_and_losses: define file, open, skip header
with open(budgetdata_csv, 'r') as csvfile :
    csvreader = csv.reader(csvfile)
    next(csvreader)

    # Define variables for calculation
    total_profit_and_losses = 0
    past_profit_and_losses = None
    changes = []
    dates = []

    # Use loop to calculate the net total
    for row in csvreader :
        date = row [0]
        profit_and_losses = int(row[1])

        total_profit_and_losses = total_profit_and_losses + profit_and_losses 

    # Calculate the changes in profit_and_losses over the entire period
        if past_profit_and_losses is not None:
            change = profit_and_losses - past_profit_and_losses
            changes.append(change)
            dates.append(date)

        past_profit_and_losses = profit_and_losses

# Calculate the average of these changes
average_of_changes = round(sum(changes)/len(changes),2) if len(changes) > 0 else 0

# Calculate the greatest increase and decrease in profits (show date and amount) over entire period
greatest_increase = max(changes) if changes else 0
greatest_decrease = min(changes) if changes else 0

# create variables for greatest increase and decrease
date_of_greatest_increase = dates[changes.index(greatest_increase)] if changes else None
date_of_greatest_decrease = dates[changes.index(greatest_decrease)] if changes else None

# Print to text file
with open(file_to_create, "w") as txt_file:

    # Print "Total", "Average change", "Greatest Increase in Profits", and "Greatest Decrease in Profits"
        print("Financial Analysis")
        txt_file.write("Financial Analysis\n")

        print("----------------------------")
        txt_file.write("----------------------------\n")

        total_months_text = f"Total Months: {total_months}"
        print(total_months_text)
        txt_file.write(total_months_text + "\n")
  

        total_profit_text = f"Total: ${total_profit_and_losses}"
        print(total_profit_text)
        txt_file.write(total_profit_text + "\n")
   

        average_change_text = f"Average Change: ${average_of_changes}"
        print(average_change_text)
        txt_file.write(average_change_text + "\n")
  



        if date_of_greatest_increase is not None:
            greatest_increase_text = f"Greatest Increase in Profits: {date_of_greatest_increase} (${greatest_increase})"
            print(greatest_increase_text)
            txt_file.write(greatest_increase_text + "\n")



        if date_of_greatest_decrease is not None:
            greatest_decrease_text = f"Greatest Decrease in Profits: {date_of_greatest_decrease} (${greatest_decrease})"
            print(greatest_decrease_text)
            txt_file.write(greatest_decrease_text + "\n")



