import nltk

cmu = nltk.corpus.cmudict.dict()

def count_syllables(word):
	""" How many syllables are there in a word? """
	
	vowelcounts = []

	for pronounciation in cmu[word]:

		vowels = []

		for phoneme in pronounciation:
			if phoneme[-1].isdigit():
				vowels.append(phoneme)

		vowelcounts.append(len(vowels))
	
	return max(vowelcounts)


if __name__ == "__main__":
	word = "confederacy"
	count = count_syllables("confederacy")
	print("There are {} vowels in {}".format(count, word))



