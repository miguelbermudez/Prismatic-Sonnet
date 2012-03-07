from Pronouncing_Key import Pronouncing_Key
from ColorObj import ColorObj 	
from pprint import pprint
import sys
import random
import re

def find_key(dic, val):
	syl_color_set = set()
	for k, v in dic.iteritems():
		if v == val:
			syl_color_set.add(k)
	return syl_color_set

aphorism_set = set()
for line in open('aphorism_set.txt'):
#for line in open('test.txt'):
	line = line.strip()
	aphorism_set.add(line)

color_dict = dict()
for line in open('color_set.txt'):
	line = line.strip()
	tokens = line.split()
	color_str = tokens[0]
	color_hex = tokens[1]
	color_syllbs = int(tokens[2])
	c = ColorObj(color_str, color_hex, color_syllbs)

	if color_str not in color_dict:
		color_dict[color_str] = c

#init pronunciations dict
pronounce_dict = Pronouncing_Key()

#Sanity Check 
#print "Aphorism: " + str( len(aphorism_set) )
#print "Colors: " + str ( len(color_set) )

#grab a random aphorism for line #1
random_aphorism = random.sample(aphorism_set, 1)[0]  #[0] req to get str

#grab just word and no punctuation
matched_obj = re.search(r"\b(\w+)[.\?!]$", random_aphorism)
last_word = matched_obj.group(1)

print "Line A: " + random_aphorism
print "\t" + matched_obj.group(1)		#debugging

#how many syllables does the word have?
last_word_syl = pronounce_dict.syllables_for_word(last_word)
#print "last_word_syl: " + str(last_word_syl)

#grab colors with just as many syllables
search_syllb_count = 0;

while search_syllb_count != last_word_syl:
	r_color_dict_key = random.choice( color_dict.keys() )
	r_colorObj = color_dict[r_color_dict_key]
	search_syllb_count = r_colorObj.syllable_count()

#print "Random ColorObj: " + str(r_colorObj) #debuggins


#matching_colors = find_key(color_dict, last_word_syl)
#matched_color = random.sample(matching_colors, 1)
#print "Line A Color: " + matched_color[0]
#print 