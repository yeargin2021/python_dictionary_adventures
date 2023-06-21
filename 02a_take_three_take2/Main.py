import csv

sample_dict = dict()

with open('text.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        sample_dict.update({row[0]: ({row[1]: row[2]})})

def menu_text():
    print("\nMenu Options")
    print("-"*len("Menu Options"))
    for i in sample_dict.keys():
        for j in sample_dict[i].keys():
            print(f"{i}. {j}")
    print("\n")

menu_text()
