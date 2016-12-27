import json
from features import FE
import nltk
from nltk import classify
import sys

class Test:

	data = []

	def __init__(self, infile='test_data.json'):

		print("Loading raw data from %s...\n" % infile)

		with open(infile, 'r') as f:
			for line in f:
				self.data.append(json.loads(line))

		print("Updating raw data...\n")

		ln = len(self.data)
		fe = FE()

		for title in self.data:
			title['features'] = fe.get_features(title['article_title'].encode('utf-8'))

	def output_test_data(self, outfile='development_data.json'):

		print("Writing updated json data to %s...\n" % outfile)

		with open(outfile, 'w') as o:
			for d in self.data:
				json.dump(d, o)
				o.write("\n")

	def get_data(self):
		return [d['features'] for d in self.data]

train_set = []
with open('training_data.json', 'r') as f:
	for line in f:
		data = json.loads(line)
		train_set.append((data['features'], data['clickbait']))


def test(typ):
	te = Test('test_%s.json' % typ)
	test_raw = te.data
	test_set = te.get_data()

	classifier = nltk.classify.NaiveBayesClassifier.train(train_set)
	results = classifier.classify_many(test_set)

	print(classifier.show_most_informative_features())

	# toprint = []

	# for (i, r) in enumerate(results):
	# 	tup = (test_raw[i]['article_title'].encode('utf-8'), r)
	# 	if tup not in toprint:
	# 		toprint.append(tup)

	with open('output_%s.txt' % typ, 'w') as o:
		for (i, r) in enumerate(results):

			toprint = test_raw[i]['article_title'].encode('utf-8')

			o.write("%s\t%s\n" % (toprint.replace('\n', ' '), r))

		# for (t, r) in toprint:
		# 	o.write("%s\t%s\n")

test(sys.argv[1])

print("Done.")
