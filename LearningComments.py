
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB as GNB
import pandas
import numpy

PATH_TO_CSV = './testSample.csv'

data = pandas.read_csv(PATH_TO_CSV, header=0)

hv = CountVectorizer(stop_words='english')
vector_complete = hv.fit_transform(data["body"])

vector_partial = vector_complete[:-100]


classifier = GNB()
classifier.fit(vector_partial.toarray(), data['subreddit'][:-100])

print str(classifier.predict(vector_complete[987].toarray()))
print data['subreddit'][987]


exit()