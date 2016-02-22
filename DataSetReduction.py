## -*- coding: utf-8 -*-

import json
#import pandas 

# the number of data entries being read in
increment = 100;

# Path where the dataset is stored - MODIFY BEFORE LAUNCHING
PATH_TO_DATASET = 'rcomments'

# Path where to store the reduced dataset - MODIFY BEFORE LAUNCHING
PATH_TO_REDUCED_DATASET = './ReducedData'

CSV_OUTPUT_FILE = './ReducedCSV.csv'

# get file length
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# read in all the data
def getRawData(filePath):
    rawData = [0 for j in range(increment)];
    with open(filePath) as file:
        for i in range(increment):
            rawData[i] = json.loads(file.readline())
    return rawData;

# reduce the data to the proper tags
# author, created_utc, score, ups, downs, body, subreddit
def parsedAndreducedData(fullData):
    data = [[0 for m in range(7)]for k in range(increment)]
    i = 0
    for datapoint in fullData:
        data[i][0] = datapoint['author']
        data[i][1] = datapoint['created_utc']
        data[i][2] = datapoint['body'].replace('\n', '')
        data[i][3] = datapoint['score']
        data[i][4] = datapoint['ups']
        data[i][5] = datapoint['downs']
        data[i][6] = datapoint['subreddit']
        i += 1
    return data

def parseAndReduceLine(line):
    data = [0 for m in range(7)]
    datapoint = json.loads(line)
    data[0] = datapoint['author']
    data[1] = datapoint['created_utc']
    data[2] = datapoint['body'].replace('\n', '')
    data[3] = datapoint['score']
    data[4] = datapoint['ups']
    data[5] = datapoint['downs']
    data[6] = datapoint['subreddit']
    return data

# get the word from a string
def parse(string):
    begin = string.find(":") + 2
    return(string[begin:-1])

# write the data to a file
def writeDataToFile(data):
    w = open(PATH_TO_REDUCED_DATASET, "w")
    for line in data:
        w.write(json.dumps(line))
    w.close()

# exports all input data to parsed and reduced csv 
def readAllAndExportCSV(inputFilePath, outputFilePath):
    outputFile = open(outputFilePath, 'w')
    with open(inputFilePath) as inputFile:
        for line in inputFile:
            lineToWrite = ""
            parsedLine = parseAndReduceLine(line)
            for value in parsedLine:
                if type(value) == int:
                    lineToWrite += str(value) + ","
                else:
                    lineToWrite += value.encode('utf-8', 'ignore') + ','

            outputFile.write(lineToWrite + '\n')


readAllAndExportCSV(PATH_TO_DATASET, CSV_OUTPUT_FILE) # ReducedCSV contains the whole file with reduced dimension, colon separated (easier to read with pandas)
exit()

rawData = getRawData(PATH_TO_DATASET)
data = parsedAndreducedData(rawData)    # Data contains now rows of reduced data from 0 to 6, respectively author, created_utc, body, score, ups, downs, subreddit
writeDataToFile(data)

print (len(data))
