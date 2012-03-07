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

#Sanity Check 
#print "Aphorism: " + str( len(aphorism_set) )
#print "Colors: " + str ( len(color_set) )


#init pronunciations dict
pronounce_dict = Pronouncing_Key()

#number of lines we need for a sonnet 
num_lines = 14

#MAIN LOOP
for n in range(0, num_lines):
	prismatic_line = ""

	#grab a random aphorism for line #1
	random_aphorism = random.sample(aphorism_set, 1)[0]  #[0] required to get str
	#grab just word and no punctuation
	matched_obj = re.search(r"\b(\w+)[.\?!]", random_aphorism)
	last_word = matched_obj.group(1)
	#print "Line: " + random_aphorism							#debugging
	#print "\tMatched last word: " + matched_obj.group(1)		#debugging
	#print "**********************\n"							#debugging
	#how many syllables does the word have?
	last_word_syl = pronounce_dict.syllables_for_word(last_word)
	#print "last_word_syl: " + str(last_word_syl)				#debugging
	
	#grab colors with just as many syllables
	search_syllb_count = 0;
	while search_syllb_count != last_word_syl:
		r_color_dict_key = random.choice( color_dict.keys() )
		r_colorObj = color_dict[r_color_dict_key]
		search_syllb_count = r_colorObj.syllable_count()

	#print "Random ColorObj: " + str(r_colorObj) 				#debugging

	print "#" + str(n) + ": " + random_aphorism.replace(last_word, r_colorObj.name)

	if n == 0 or n == 2: 
		colorA = r_colorObj

	if n == 1 or n == 3 or n == 4 or n == 6:    
		colorB = r_colorObj

	if n == 5 or n == 7 or n == 8 or n == 10:    
		colorC = r_colorObj

	if n == 9 or n == 11:
		colorD = r_colorObj

	if n == 12 or n == 13:
		colorE = r_colorObj

	#rprint newlines
	if n % 4 == 0 and n != 0:
		print "\n"	



#matching_colors = find_key(color_dict, last_word_syl)
#matched_color = random.sample(matching_colors, 1)
#print "Line A Color: " + matched_color[0]
#print 