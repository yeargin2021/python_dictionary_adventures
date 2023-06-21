import csv

sample_dict = dict()

with open('text.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        sample_dict.update({row[0]: row[1]})

print(sample_dict)
