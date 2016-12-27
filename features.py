import nltk

# TODO: add feature -> multiple indicative words

class FE:

	per_pr = []
	rel_pr = []
	dem_pr = []
	ind_pr = []
	int_pr = []
	pos_pr = []
	sub_pr = []
	obj_pr = []
	medium = []
	curse = []
	pronouns = []
	social_media = []
	slang = []
	command = []
	vague = []
	emotion = []
	punc = []
	indicative = []
	forms = []

	def __init__(self):
		self.per_pr = ["i", "me", "you", "she", "her", "he", "him", "we", "us", "they", "them"]
		self.rel_pr = ["that", "which", "who", "whom", "whose", "whichever", "whoever", "whomever"]
		self.dem_pr = ["this", "these", "that", "those"]
		self.ind_pr = ["anybody", "anyone", "anything", "each", "either", "everybody", "everyone", 
		"everything", "neither", "nobody", "nothing", "somebody", "someone", "something", "both", "all", 
		"any", "most", "some"]
		self.int_pr = ["what", "who", "which", "whom", "whose"]
		self.pos_pr = ["my", "your", "his", "her", "mine", "yours", "his", "hers", "our", "their", "ours", "theirs"]
		self.sub_pr = ["i", "you", "she", "he", "we", "they"]
		self.obj_pr = ["me", "you", "her", "it", "him", "us", "you", "them"]

		raw_pr = self.per_pr + self.rel_pr + self.dem_pr + self.ind_pr + self.int_pr + self.pos_pr + self.sub_pr + self.obj_pr

		for p in raw_pr:
			if p not in self.pronouns:
				self.pronouns.append(p)

		self.social_media = ["instagram", "facebook", "likes", "youtube", "buzzfeed", "snapchat", 
		"pinterest", "gif", "gifs", "followers", "vine", "twitter", "tweet", "pic", "pics", "snapchats", 
		"tweets", "tweeted", "nsfw", "selfie", "selfies", "viral", "meme", "memes", 'troll', 'trolling', 'trolls',
		'internet']

		self.slang = ["kinda", "sorta", "hell", "hella", "omg", "wtf", "weird", "weirdly", "weirder",
		"weirdest", "lol", "lmao", "smh", "fuck", "fucking", "fuckin", "ass", "shit", "bitch", 
		"bullshit", "cool", "cooler", "coolest", "frickin", "freakin", "af", "pics", "pic",
		"freaking", "badass", "bad-ass", "guy", "whatever", "totally", "celeb", "heck", "shitty",
		"damn", "goddamnit", "goddammit", "goddamn", "dang", "darn", "nope", "nah", "gtfo", "really"]

		self.command = ["listen", "watch", "read", "see", "look", "hear"]

		self.curiosity = ["if", "react", "reaction", "reacts", "finally", "show", "quiz", "reveal", "reveals",
		"revealed", "share", "shares", "shared", "story", "stories", "explain", "describe", "explains", "describes",
		"important", "understand", "accidental", "accidentally", "accident", "prove", "proves", "until", "just"]

		self.medium = ["comic", "comics", "photos", "pics", "pictures", "drawings", "video", "videos"]

		self.vague = ["person", "people", "guy", "guys", "scientist", "scientists", "science", 
		"happen", "happens", "happened", "happening", "reason", "reasons", "thing", "things",
		"stuff", "kid", "kids", "mom", "dad", "if", "problem", "fact", "facts"]

		self.emotion = ["gut-wrenching", "heartbreaking", "heartbreak", "heartbroken", "hilarious", 
		"hilariously", "powerful", "powerfully", "kindness", "fascinating", "fascinate", "inspire",
		"inspiration", "inspirational", "inspires", "inspiring", "touching", "captivating", "glorious",
		"humanity", "ridiculous", "ridiculously", "beauty", "beautiful", "beautifully", "vicious", 
		"viciously", "silly", "harmless", "harmlessly", "hurtful", "so-called", "laugh", "sexy",
		"horrifying", "horrified", "horrify", "moving", "shock", "shocking", "shockingly", "clever", 
		"surprising", "surprise", "surprisingly", "incredible", "incredibly", "perfect", "perfection", 
		"stunning", "stunningly", "love", "loved", "loves", "adorable", "adorably", "best", "amazing", 
		"amazingly", "amaze", "believe", "unforgettable", "gorgeous", "delicious", "deliciously", "worst",
		"crazy", "awesome", "absolutely", "funny", "funnier", "funniest", "super", "hero", "heroes"]

		self.indicative = self.social_media + self.emotion + self.slang + self.vague + self.command

		self.curse = ["ass", "badass", "bad-ass", "bastard", "bitch", "bitches", "bitchin", "bitching", "bitchy", 
		"bullshit", "crap", "damn", "fuck", "fucking", "fuckin", "fucks", "goddammit", "goddamn", "goddamnit", 
		"hell", "shit", "shitty"]

		self.punc = [".", "!", "?", "?!", "!!", "!!!"]

		self.forms = [["that", "will", " "],
		[["make", "give"], "you", " "],
		["faith", "in", "humanity"],
		["here", "'s", ["how", "what", "why", "the"]],
		["here", ["are", "is", "'s"]],
		[self.pos_pr, "story"],
		["people", "are"],
		["let", "'s"]]

	def clean(self, arr):
		newarr = []
		for token in arr:

			if token.lower() in ['vs.', 'v.']:
				token = 'versus'
			if token == 'US':
				token = 'U.S.'

			if token.lower() in ["'s", "'t", "'ll", "'ve", "'m", "'re", "'ve", "'d"]:
				newarr.append(token)
				continue
			if token in ["'", "''", "\"", "``", ""]:
				continue
			if token[0] in ["'", "''", "\"", "``"]:
				token = token[1:]
			if token[-1:] in ["'", "''", "\"", "``"]:
				token = token[:-1]

			newarr.append(token)
		return newarr

	def chunkify(self, spl):
		chunks = []
		l = [0]
		l.extend([i + 1 for i, x in enumerate(spl) if x in self.punc])
		for (i, idx) in enumerate(l):
			if i == 0:
				continue
			chunks.append(spl[l[i - 1]:idx])
		if len(chunks) < 1:
			chunks.append(spl)
		return chunks

	def has_intersection(self, a, b):
		return len(set(a) & set(b)) > 0

	def has_start(self, tokens, chunks):
		for chunk in chunks:
			if chunk[0] in tokens:
				return True
			if chunk[0] == "(":
				if chunk[1] in tokens:
					return True
		return False

	def convert_nums(self, sent):
		newarr = []
		for s in sent:
			try:
				i = float(s)
				if i > 1900 and i < 2100:
					newarr.append("-YEAR-")
				else:
					newarr.append("-NUM-")
			except ValueError:
				newarr.append(s)
				continue
		return newarr

	def has_form(self, form, sent):
		if len(sent) < len(form):
			return False

		def helper(form, sent):
			if len(form) == 0:
				return True

			if len(sent) < len(form):
				return False
			if isinstance(form[0], list):
				if sent[0] in form[0]:
					return helper(form[1:], sent[1:])
			elif form[0] == " " or form[0] == sent[0]: 
				return helper(form[1:], sent[1:])
			return False


		if form[0] == " ":
			for i in range(0, len(sent) - len(form) + 1):
				if helper(form[1:], sent[i + 1:]):
					return True

		elif isinstance(form[0], list):
			for i in range(0, len(sent) - len(form) + 1):
				if sent[i] in form[0]:
					if helper(form[1:], sent[i + 1:]):
						return True

		else:
			for i in range(0, len(sent) - len(form) + 1):
				if sent[i] == form[0]:
					if helper(form[1:], sent[i + 1:]):
						return True
		return False

	def has_any_form(self, forms, sents):
		for sent in sents:
			for form in forms:
				if self.has_form(form, sent[:-1]):
					return True
		return False

	def get_features(self, title):
		try:
			words = self.clean(nltk.word_tokenize((title)))
		except UnicodeDecodeError:
			dec = title.decode('ascii', 'ignore')
			words = self.clean(nltk.word_tokenize((dec)))

		lower = []
		for w in words:
			lower.append(w.lower())

		if words[len(words) - 1] not in self.punc and words[len(words) - 1] != "...":
			words.append(".")
		pos = [tag for (token, tag) in nltk.pos_tag(words)]
	
		words = self.convert_nums(words)
		lower = self.convert_nums(lower)

		chunks = self.chunkify(words)
		l_chunks = self.chunkify(lower)
		tags = self.chunkify(pos)

		features = dict()
		
		features['multiple_sentences'] = len(chunks) > 1

		features['has_past_tense'] = 'VBD' in pos or 'VBN' in pos
		features['has_ing'] = 'VBG' in pos

		features['start_tag'] = pos[0]
		features['start_tag_bigram'] = ' '.join(pos[:2])
		features['conjunction'] = 'and' in lower or 'but' in lower

		has_you = self.has_intersection(['you', 'your', 'yours'], lower)

		features['multiple_you'] = False

		if has_you:
			cnt = 0
			cnt += lower.count('you')
			cnt += lower.count('your')
			cnt += lower.count('yours')

			features['multiple_you'] = cnt > 1

		features['has_pronoun'] = self.has_intersection(self.pronouns, lower) or self.has_form(["no", "one"], lower)
		features['multiple_pronouns'] = False
		if features['has_pronoun']:
			cnt = 0
			for p in self.pronouns:
				cnt += lower.count(p)
			features['multiple_pronouns'] = cnt > 1

		features['has_adverb'] = self.has_intersection(["RB", "RBR", "RBS", "RP"], pos)
		features['has_adjective'] = self.has_intersection(["JJ", "JJR", "JJS"], pos)
		has_number = "-NUM-" in words

		features['may_have_list'] = (has_number and self.has_intersection(["NNS", "NNPS"], pos))

		#########################

		has_question = "?" in words
		has_exclamation = self.has_intersection(["!", "?!", "!!", "!!!"], words)
		question_to_reader = has_you and has_question
		question_pronoun = has_question and features['has_pronoun']
		interr_no_question = not has_question and self.has_intersection(self.int_pr, lower)

		features['indicative_remark'] = question_to_reader or interr_no_question or question_pronoun or has_exclamation


		############################

		# features['curse'] = self.has_intersection(self.curse, lower)
		# features['vague'] = self.has_intersection(self.vague, lower)
		# features['curiosity'] = self.has_intersection(self.curiosity, lower)
		# features['medium'] = self.has_intersection(self.medium, lower)
		# features['social_media'] = self.has_intersection(self.social_media, lower)
		# features['slang'] = self.has_intersection(self.slang, lower)
		# features['emotion'] = self.has_intersection(self.emotion, lower)

		features['indicative_words'] = self.has_intersection(self.indicative, lower)
		features['multiple_indicative_words'] = False
		if features['indicative_words']:
			cnt = 0
			for word in self.indicative:
				cnt += lower.count(word)

			features['multiple_indicative_words'] = cnt > 1

		#########################33

		features['indicative_start'] = self.has_start(self.pronouns + ['meet', 'why', 'how', 'when', 'if', '-NUM-', 'for', 'now', 'here'], l_chunks)

		features['the_start'] = self.has_any_form([["DT", ["CD", "JJ"]]], tags)
		features['indicative_word_start'] = self.has_start(self.indicative, l_chunks)

		#######################

		features['has_form'] = self.has_any_form(self.forms, l_chunks) or self.has_any_form([["CD", ["NNS", "NNPS"]], ["CD", " ", ["NNS", "NNPS"]]], tags)

		features['indicative_form'] = features['has_form']  or features['indicative_remark']

		features['indicative_form_start'] = features['indicative_form'] or features['indicative_start']

		return features