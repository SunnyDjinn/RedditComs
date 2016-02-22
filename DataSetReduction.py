# the number of data entries being read in
increment = 500000;

# get file length
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# read in all the data
def getRawData(filePath):
    rawData = [0 for j in range(increment)];
    count = 0;
    with open(filePath) as file:
        for i in range(increment):
            rawData[count] = file.readline();
            count += 1;
    return rawData;

# split the data by commas
def splitData(rawData):
    fullData = [[0 for i in range(25)] for j in range(increment)]
    count = 0;
    for i in rawData:
        fullData[count] = i.split(',')
        # fullData[count] = re.split(r', (?=(?:"[^"]*?(?: [^"]*)*))|, (?=[^",]+(?:,|$))', i)
        count += 1
    return fullData

# reduce the data to the proper tags
# author, created_utc, score, ups, downs, body, subreddit
def reducedData(fullData):
    data = [[0 for m in range(7)]for k in range(increment)]
    for i in range(len(fullData)):
        count = 0;
        for j in fullData[i]:
            string = j
            if  string.endswith('\n'):
                string = string[:-2]
            if '"author":' in string:
                data[i][0] = parse(string)
            elif '"created_utc":' in string:
                data[i][1] = parse(string)
            elif '"body":' in string:
                if string[-1] == '\"':
                    data[i][2] = parse(string)
                else:
                    begin = string.find(":") + 2
                    data[i][2] = string[begin:] +", "
                    # pos = (count) + 1
                    # while ':' not in fullData[i][pos] and fullData[i][pos]!='0' and pos < 25:
                        # print(fullData[i][pos])
                        # data[i][2] += parse(fullData[i][pos])
                        # pos +=1
            elif '"score":' in string:
                begin = string.find(":") + 1
                data[i][3] = string[begin:]
            elif '"ups":' in string:
                begin = string.find(":") + 1
                data[i][4] = string[begin:]
            elif '"downs":' in string:
                begin = string.find(":") + 1
                data[i][5] = string[begin:]
            elif '"subreddit":' in string:
                data[i][6] = parse(string)
            count += 1
    return data

# get the word from a string
def parse(string):
    begin = string.find(":") + 2
    return(string[begin:-1])

# write the data to a file
def writeDataToFile(data):
    w = open('D:/RedditDataSetSmall.txt', "a")
    for i in range(increment):
        for j in range(7):
            w.write(str(data[i][j]) + " ")
        w.write("\n")

rawData = getRawData('D:/RedditDataSet.txt')
fullData = splitData(rawData)
data = reducedData(fullData)

print (len(data))
print (data[0])