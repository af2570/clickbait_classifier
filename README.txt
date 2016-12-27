Anna Fenske (af2570)
NLP Final Project

CLICKBAIT CLASSIFIER

Files:
	features.py: feature extractor
	
	train.py: collect featuresets of training data, write them to training_data.json
	
	test.py: train classifier and test on test_clickbait.json and test_news.json
		TO RUN: python test.py [news/clickbait/all]
	
	test_clickbait.json: corpus of headlines from Buzzfeed (different from headlines in training corpus) for testing
		output_clickbait.txt: output from test.py on test_clickbait.json
	
	test_news.json: corpus of headlines from New York times (different from headlines in training corpus) for testing
		output_news.txt: output from test.py on test_news.json
	
	test_all.json: test data from both test_clickbait.json and test_news.json
		output_all.txt: output from test.py on test_all.json
	
	training_data.json: Headlines from all sources and their feature sets and annotations for training classifier
	
	training_data: directory holding annotated training data separated by source
	
	ACL_REPORT.pdf: ACL-style write-up.
