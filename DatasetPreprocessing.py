import pandas
import string

PATH_TO_CSV = 'ReducedCSV.csv'

PATH_TO_CORRECTED_CSV = 'CorrectedCSV.csv'

def correctImperfectionsData(inputFilePath, outputFilePath):
    outputFile = open(outputFilePath, 'w')
    outputFile.write('username,date,body,score,subreddit\n')
    with open(inputFilePath) as inputFile:
        for line in inputFile:
            outputFile.write(lineToWrite)


#correctImperfectionsData(PATH_TO_CSV, PATH_TO_CORRECTED_CSV)


#data = pandas.read_csv(PATH_TO_CSV, header=0) # first row as column title, parses date using column 1
#print data

#outputFile = open('reducedSmall.csv', 'w')

all = string.maketrans('','')
keeper = all.translate(all, string.digits + string.lowercase + ',!? .()[]\'')

tp = pandas.read_csv('smallDataTest.csv', header=0, iterator=True, chunksize=1)
for chunk in tp:
	for body in chunk['body']:
		body = str(body).lower() #datapoint[2] = 
		body = body.translate(all, keeper)
	chunk.to_csv(path_or_buf=stringToPrint)
	print 
	#outputFile.write(chunk.to_csv())



exit()

print df


#print pandas.to_datetime(data['date'][99], unit='s') # to convert to readable time 