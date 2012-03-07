class ColorObj(object):

	def __init__(self, mName, mHex, mSyllbs):
		self.name   = mName
		self.hex    = mHex
		self.syllbs = mSyllbs

	
	def syllable_count(self):
		return self.syllbs

	def name(self):
		return self.name

	
	def __repr__(self):
		return "Color: " + self.name + " Hex" + self.hex + " Syllbs" + str(self.syllbs)

	
	def __str__(self):
		return "Color: " + self.name + " Hex: " + self.hex + " Syllbs: " + str(self.syllbs)


