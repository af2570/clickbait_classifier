Anna Fenske (af2570)
NLP Final Project

CLICKBAIT CLASSIFIER

Files:
	features.py: feature extractor
	
	train.py: collect featuresets of training data, write them to training_data.json
	
	test.py: train classifier and test on test_clickbait.json and test_news.json
		TO RUN: python test.py [news/clickbait/all]
	
	testing_data\test_clickbait.json: corpus of headlines from Buzzfeed (not in training corpus) for testing
		results\output_clickbait.txt: output from test.py on test_clickbait.json
	
	testing_data\test_news.json: corpus of headlines from New York times (not in training corpus) for testing
		results\output_news.txt: output from test.py on test_news.json
	
	testing_data\test_all.json: test data from both test_clickbait.json and test_news.json
		results\output_all.txt: output from test.py on test_all.json
	
	training_data.json: Headlines from all sources and their feature sets and annotations for training classifier
	NOTE: training_data.json not included in this repository (file size too large). This should not be an issue though since test.py runs train.py.
	
	training_data: directory holding annotated training data separated by source
	
	ACL REPORT.pdf: ACL-style write-up.
