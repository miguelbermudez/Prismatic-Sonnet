from pprint import pprint
import re
import sys


class Pronouncing_Key(object):
	
	def __init__(self):
		self.pronounce_dict = dict()

		for line in open('cmudict.0.7a'):
		#for line in open('cmutest.txt'):
			line = line.strip()
			tokens = line.split()
			#grab the word
			word = tokens[0]

			#create key if none exists
			if word not in self.pronounce_dict:
				self.pronounce_dict[word] = 0

			#remove word from token set
			tokens.remove(word)

			#get syllables for words
			num_syllables = 0
			for n in tokens:	
				#does token represent a syllable
				if (re.search(r"\b([A-Z]+[0-9])", n) != None):
					num_syllables += 1

				if word in self.pronounce_dict:
					self.pronounce_dict[word] = num_syllables

	def pprint(self):
		pprint(self.pronounce_dict)


	def syllables_for_word(self, word):
		word = word.upper()
		if word in self.pronounce_dict:
			return self.pronounce_dict[word]
		else:
			return 0

	def get_pronunciations(self):
		return self.pronounce_dict
