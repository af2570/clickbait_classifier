import json
from features import FE

class Trainer:

	data = []

	def __init__(self, infile_dir, infile_list):

		print("Loading raw data...")

		for infile in infile_list:
			print("\t...from %s" % infile)
			with open('%s/%s.json' % (infile_dir, infile), 'r') as f:
				for line in f:
					self.data.append(json.loads(line))

		print("\n")
		print("Updating raw data...")

		ln = len(self.data)
		fe = FE()

		for title in self.data:
			title['features'] = fe.get_features(title['article_title'].encode('utf-8'))

	def output_trained_data(self, outfile='training_data.json'):

		print("Writing updated json data to %s...\n" % outfile)

		with open(outfile, 'w') as o:
			for d in self.data:
				json.dump(d, o)
				o.write("\n")

	def get_data(self, out=False):
		if out:
			self.output_trained_data()
		return [(t['features'], t['clickbait']) for t in self.data]

t = Trainer('training_data', ['buzzfeed', 'cnn', 'nyt', 'wsj', 'upworthy'])
t.output_trained_data()