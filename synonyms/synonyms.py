import nltk
from nltk.corpus import wordnet as wn

import random

def synonimize(word, pos=None):
	""" Get synonyms of the word / lemma """ 
	try:
		# map part of speech tags to wordnet
		pos = {'NN': wn.NOUN,'JJ':wn.ADJ,'VB':wn.VERB,'RB':wn.ADV}[pos[:2]]
	except:
		# or just return the original word
		print("OUCH {} {}".format(word, pos))
		return [word]

	synsets = wn.synsets(word, pos)
	synonyms = []
	for synset in synsets:
		for sim in  synset.similar_tos():
			synonyms += sim.lemma_names()
	
	# return list of synonyms or just the original word
	return synonyms or [word]

def vary_sentence(sentence):
	""" Create variations of a sentence using synonyms """
	words = nltk.word_tokenize(sentence)
	pos_tags = nltk.pos_tag(words)

	words = []
	for (word, pos) in pos_tags:
		synonyms = synonimize(word, pos)
		picked = random.choice(synonyms)
		words.append(picked)

	return " ".join(words)


if __name__ == "__main__":
	print(vary_sentence("A small word that can have many meanings"))


