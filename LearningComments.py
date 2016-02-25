
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.svm import SVR
from sklearn.cluster import KMeans

from sklearn.decomposition import PCA

from sklearn.naive_bayes import MultinomialNB as MNB
import pandas
import numpy
import scipy
import random
import re
import collections

PATH_TO_CSV = './testSample.csv'

data = pandas.read_csv(PATH_TO_CSV, header=0)

for i in range(len(data["body"])):
	data["body"][i] = re.sub('\w([ ]{2,})\w', ' ', str(data["body"][i]))
	data["body"][i] = re.sub('\d', ' ', data["body"][i])
	data["body"][i] = data["body"][i].replace('.', ' ')
	data["body"][i] = data["body"][i].replace('[]', ' ')
	data["body"][i] = data["body"][i].split(' ')
	toRemove = set()
	for word in data["body"][i]:
		if len(word) < 5 or len(word) >= 15:
			toRemove.add(word)
	for word in toRemove:
		data["body"][i].remove(word)
	del toRemove
	data["body"][i] = " ".join(data["body"][i])




#for i in range(len(data['utc'])):
#	X.append([data['utc'][i], data['score'][i], data['subreddit'][i], data['body'][i], len(data['author'][i])])




#X.append([len(x) for x in data['author']])
#X.append(data['utc'])
#X.append(data['score'])
#X.append(data['subreddit'])
#X.append(data['body'])

X_training = []
X_test = []
Y_training = []
Y_test = []


size = len(data["body"])
selected_indices = random.sample(xrange(size), int(0.1 * size))

for i in range(len(data['body'])):
	if i in selected_indices:
		X_test.append(data['body'][i])
		Y_test.append(data['score'][i])
	else:
		X_training.append(data['body'][i])
		Y_training.append(data['score'][i])


cv = CountVectorizer(stop_words='english', strip_accents='ascii', max_df=0.8, ngram_range=(1, 5))	#, ngram_range=(1, 2)
X_training = cv.fit_transform(X_training)
X_test = cv.transform(X_test)

#transformer = TfidfTransformer(norm='l2', use_idf=True, sublinear_tf=True)
#X_training = transformer.fit_transform(X_training)
#X_test = transformer.transform(X_test)


svr_poly = SVR(kernel='sigmoid', C=1e-1)

predicted = svr_poly.fit(X_training, Y_training).predict(X_test)

counterOK = 0
counter = 0

for pred, target in zip(predicted, Y_test):
	print "Found %s, actual %s"%(str(pred), str(target))
	if pred <= target*1.3 and pred >= target * 0.7:
		counterOK += 1
	counter += 1
	print "statistics: %d / %s" %(counterOK, counter)


exit()


#y_pred = KMeans(n_clusters=8).fit_predict(X)

#print y_pred

exit()

bodyCommentsTraining = []
bodyCommentsTest = []
scoreTraining = []
scoreTest = []
subredditTraining = []
subredditTest = []

size = len(data["body"])
selected_indices = random.sample(xrange(size), int(0.1 * size))

for i in range(len(data['body'])):
	if i in selected_indices:
		bodyCommentsTest.append(data['body'][i])
		scoreTest.append(data['score'][i])
	else:
		bodyCommentsTraining.append(data['body'][i])
		scoreTraining.append(data['score'][i])


cv = CountVectorizer(stop_words='english', strip_accents='ascii', max_df=0.8, ngram_range=(1, 5))	#, ngram_range=(1, 2)
bodyCommentsTraining = cv.fit_transform(bodyCommentsTraining)
bodyCommentsTest = cv.transform(bodyCommentsTest)

transformer = TfidfTransformer(norm='l2', use_idf=True, sublinear_tf=True)
bodyCommentsTraining = transformer.fit_transform(bodyCommentsTraining)
bodyCommentsTest = transformer.transform(bodyCommentsTest)

y_pred = KMeans().fit_predict(bodyCommentsTraining)

print y_pred

values = set()

for x in y_pred:
	values.add(x)


temp = collections.Counter(y_pred)

maxValue = 0
maxIndex = 0
for x in temp:
	if temp[x] > maxValue:
		maxValue = temp[x]
		maxIndex = x

print maxIndex

for i in range(len(y_pred)):
	if y_pred[i] != maxIndex:
		print subredditTraining[i] 


#svr_poly = SVR(kernel='rbf', C=1e5)

#predicted = svr_poly.fit(bodyCommentsTraining, scoreTraining).predict(bodyCommentsTest)

counterOK = 0
counter = 0
for pred, target in zip(predicted, scoreTest):
	print "Found %s, actual %s"%(str(pred), str(target))
	if pred <= target*1.3 and pred >= target * 0.7:
		counterOK += 1
	counter += 1
	print "statistics: %d / %s" %(counterOK, counter)


exit()

###################""




print trainingX
exit()

print len(cv.get_feature_names())

polynomialFeaturizer = PolynomialFeatures(degree=2)
bodyCommentsTraining = polynomialFeaturizer.fit_transform(bodyCommentsTraining.toarray())
bodyCommentsTest = polynomialFeaturizer.transform(bodyCommentsTest.toarray())

regressor = LinearRegression()
regressor.fit(bodyCommentsTraining, scoreTraining)

predicted = regressor.predict(bodyCommentsTest)


counterOK = 0
counter = 0
for pred, target in zip(predicted, scoreTest):
	print "Found %s, actual %s"%(str(pred), str(target))
	if pred <= target*1.1 and pred >= target * 0.9:
		counterOK += 1
	counter += 1
	print "statistics: %d / %s" %(counterOK, counter)


exit()
#hashingVectorizer = HashingVectorizer(strip_accents='ascii', stop_words='english', norm='l2')
#bodyCommentsTraining = hashingVectorizer.transform(data['body'])
#print bodyCommentsTraining
#exit()
#print hashingVectorizer.get_params()

#tf_transformer = TfidfTransformer(use_idf=True).fit(bodyCommentsTraining)
#bodyCommentsTraining = tf_transformer.transform(bodyCommentsTraining)

pca = PCA(n_components=6)
pca.fit(bodyCommentsTraining.toarray())
print(pca.explained_variance_ratio_) 

exit()

classes = set(data["subreddit"])

INCREMENT = 1
for i in range(0, size, INCREMENT):
	clf = MNB().partial_fit(bodyCommentsTraining[i:i+INCREMENT], subredditTraining[i, i+INCREMENT], classes)

exit()
bodyCommentsTest = cv.transform(bodyCommentsTest)
bodyCommentsTest = tf_transformer.transform(bodyCommentsTest)
predicted = clf.predict(bodyCommentsTest)


counterOK = 0
counter = 0
for pred, target in zip(predicted, subredditTest):
	print "Found %s, actual %s"%(pred, target)
	if pred == target:
		counterOK += 1
	counter += 1
	print "statistcs: %d / %s" %(counterOK, counter)
exit()

counterOK = 0
counter = 0
for i in range(0, len(bodyCommentsTest), 1):
	predicted = classifier.predict(bodyCommentsTest[i])#.reshape(1, -1))
	predicted = str(predicted[0])
	print "Found: " + predicted + ", real: " + str(subredditTest[i])
	if predicted == subredditTest[i]:
		counterOK += 1
	counter += 1
	print "statistcs: %d / %s" %(counterOK, counter)

exit()