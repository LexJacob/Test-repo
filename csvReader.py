# Reading and writing to files
import csv # imports csv file

def readingFile(filename):
    file = open(filename, "r")

    for line in file:
        print(line)

    file.close()

# readingFile("condiments.txt")

def csvReader(filename):

    with open(filename, "r") as file:
        csv_reader = csv.reader(file, delimeter=",")

        next(csv_reader)

        for row in csv_reader:
            for item in row:
                print(row)

csvReader(condiments.csv)
