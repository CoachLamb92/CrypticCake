import csv

# clues.csv seemed to encompass times.csv, so times.csv has been omitted
# train.csv only has questions and answers, and shall be left aside for the time being
filename_1 = "CrypticClueDataSets/big_dave.csv"
filename_2 = "CrypticClueDataSets/clues.csv"

# initializing the titles and rows list
fields = []
rows = []

with open(filename_1, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)[1:5]
    for row in csvreader:
        rows.append(row[1:5])

with open(filename_2, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row[1:5])

with open("filtered_clues.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)