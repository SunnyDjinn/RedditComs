import re

def readfile(filename):
    with open(filename) as infile:
        for line in infile:
            yield line

stop_words = []
with open('stopwords.txt') as infile:
    stop_words = infile.read().split('\n')

new = []
symbols = []
with open('stopsymbols.txt') as infile:
    symbols = infile.read().split('\n')

dataset = 'dataset.csv'
pattern = '^https?://[a-zA-Z0-9_\.]+.[a-zA-Z0-9_\.]+[a-zA-Z0-9_\.]+'

for line in readfile(dataset):
    for word in line.split(" "):
        if re.findall(pattern, word):
            line = line.replace(word,'')
        if word in stop_words:
            # remove it
            line = line.replace(word, '')
        for character in word:
            if character in symbols:
                line = line.replace(character, '')
                print(word)
    line = re.sub(' +', ' ', line)
    new.append(line)

with open('reduced_dataset.csv', 'w') as outfile:
    for line in new:
        outfile.write(line)
