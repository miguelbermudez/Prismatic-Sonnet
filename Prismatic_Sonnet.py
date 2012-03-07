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

def getNearestColor(hexColorHolder):
	prevDelta = sys.maxint
	nearestColor = hexColorHolder		#how do i make this just be an empy ColorObj
	#print "\t\t\t\t\t...hexColorHolder: " + str(hexColorHolder.getRGB()) #debugging
	#loop through color_set 
	for k, v in color_dict.iteritems():
		#get ColorObj from dict
		c = color_dict[k]
		if c.name != 'black':
			delta_E = hexColorHolder.colorDiff(c)
			#print "\t\t\t\t...getNear testing color: " + c.name + " delta_E: " + str(delta_E)	#debugging
			if delta_E < prevDelta:
				prevDelta = delta_E
				#print "\t\t\t\t\t... delta_E: " + str(delta_E)		#debugging
				nearestColor = c
				#print "\t\t\t ...nearestColor" + str(nearestColor)	#debugging

	#print "\t\t\t RETURN: nearestColor" + str(nearestColor) + "\n"	#debugging
	return nearestColor


#####################################################################

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

#### MAIN LOOP ####
r_colorObj = ColorObj('empty', '000000', 0) #how else do i make an empty obj?
rgbColorA = ColorObj('empty', '000000', 0) 
rgbColorB = ColorObj('empty', '000000', 0) 
rgbColorC = ColorObj('empty', '000000', 0)
rgbColorD = ColorObj('empty', '000000', 0) 
rgbColorE = ColorObj('empty', '000000', 0) 

for n in range(0, num_lines):
	prismatic_line = ""
	nearestColor = ColorObj('empty', '000000', 0) 

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
		#print "\t\t...Random ColorObj: " + str(r_colorObj) 				#debugging
			

		

	#mix colors together
	#http://code.activestate.com/recipes/266466-html-colors-tofrom-rgb-tuples/
	#the if /elif is a total hack, seriously, it's gross
	if n == 0:
		rgbColorA = r_colorObj
		#print "\tColorA: " + str(rgbColorA)
		print "#" + str(n) + ": " + random_aphorism.replace(last_word, rgbColorA.name)
	if n == 2:
		#print "\tColorA: " + str(rgbColorA)
		print "#" + str(n) + ": " + random_aphorism.replace(last_word, rgbColorA.name)

	if n == 1:
		rgbColorB = r_colorObj
		#print "\tColorB: " + str(rgbColorB)
		print "#" + str(n) + ": " + random_aphorism.replace(last_word, rgbColorB.name)	
	
	if n == 3 or n == 4 or n == 6:
		print "#" + str(n) + ": " + random_aphorism.replace(last_word, rgbColorB.name)


	if n == 5:
		z = zip(rgbColorA.getRGB(), rgbColorB.getRGB() )
		avgRGB = [ sum(x)/2 for x in z ]
		avgHex = '#%02x%02x%02x' % tuple(avgRGB)
		hexColorHolder = ColorObj('unknown', avgHex[1:], 0) #skip '#'
		rgbColorC = getNearestColor(hexColorHolder)
		#print "\tColorC: " + str(rgbColorC)
		print "#" + str(n) + ": " + random_aphorism.replace(last_word, rgbColorC.name)
	
	if n == 7 or n == 8 or n == 10:
		print "#" + str(n) + ": " + random_aphorism.replace(last_word, rgbColorC.name)

	if n == 9:
		z = zip(rgbColorB.getRGB(), rgbColorC.getRGB() )
		avgRGB = [ sum(x)/2 for x in z ]
		avgHex = '#%02x%02x%02x' % tuple(avgRGB)
		hexColorHolder = ColorObj('unknown', avgHex[1:], 0) #skip '#'
		rgbColorD = getNearestColor(hexColorHolder)
		#print "\tColorD: " + str(rgbColorD)
		print "#" + str(n) + ": " + random_aphorism.replace(last_word, rgbColorD.name)
	
	if n == 11:
		print "#" + str(n) + ": " + random_aphorism.replace(last_word, rgbColorD.name)

	if n == 12:
		z = zip(rgbColorC.getRGB(), rgbColorD.getRGB() )
		avgRGB = [ sum(x)/2 for x in z ]
		avgHex = '#%02x%02x%02x' % tuple(avgRGB)
		hexColorHolder = ColorObj('unknown', avgHex[1:], 0) #skip '#'
		rgbColorE = getNearestColor(hexColorHolder)
		#print "\tColorE: " + str(rgbColorE)
		print "#" + str(n) + ": " + random_aphorism.replace(last_word, rgbColorE.name)
	
	if n == 13:
		print "#" + str(n) + ": " + random_aphorism.replace(last_word, rgbColorE.name)
		
	#print "#" + str(n) + ": " + random_aphorism.replace(last_word, r_colorObj.name)

	#print newlines
	#again another hack but couldn't figure out which modulus forumula to use: n % 3 or n %4 == 0?

	if n == 3 or n == 7 or n == 11  and n != 0:
		print "\n"	

print "\nCOLOLRS USED IN THIS SONNET: "
print str(rgbColorA)
print str(rgbColorB)
print str(rgbColorC)
print str(rgbColorD)
print str(rgbColorE)


#matching_colors = find_key(color_dict, last_word_syl)
#matched_color = random.sample(matching_colors, 1)
#print "Line A Color: " + matched_color[0]
#print 