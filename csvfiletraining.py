import csv

imported_list = []

with open ("test_inventory.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        imported_list.append(row)
        imported_list = imported_list[0]
        print(imported_list, "THIS IS NEW")

def open_file(filename):
    with open (filename) as csvfile:
        importedList = csv.reader(csvfile, delimiter=',')
        for row in importedList:
            print(row, "This is ADDED!")

#open_file("test_inventory.csv")
