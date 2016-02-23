import pandas

PATH_TO_CSV = 'ReducedCSV.csv'

PATH_TO_CORRECTED_CSV = 'CorrectedCSV.csv'

def correctImperfectionsData(inputFilePath, outputFilePath):
    outputFile = open(outputFilePath, 'w')
    outputFile.write('username,date,body,score, ups,downs,subreddit\n')
    with open(inputFilePath) as inputFile:
        for line in inputFile:
            lineToWrite = line[:-2]
            outputFile.write(lineToWrite + '\n')


#correctImperfectionsData(PATH_TO_CSV, PATH_TO_CORRECTED_CSV)

#data = pandas.read_csv(PATH_TO_CORRECTED_CSV, header=0) # first row as column title, parses date using column 1


#print pandas.to_datetime(data['date'][99], unit='s') # to convert to readable time 