from colormath.color_objects import XYZColor
from colormath.color_objects import LabColor, LCHabColor, SpectralColor, RGBColor

class ColorObj(object):

	def __init__(self, mName, mHex, mSyllbs):
		self.name   = mName
		self.hex    = mHex
		self.syllbs = mSyllbs

	
	def syllable_count(self):
		return self.syllbs

	def name(self):
		return self.name

	def getLAB(self):
		rgb = self.getRGB() 
		rgbObj = RGBColor( rgb[0], rgb[1], rgb[2], rgb_type='sRGB' )
		labObj = rgbObj.convert_to('lab')
		return labObj

	def getRGB(self):
		r, g, b = self.hex[:2], self.hex[2:4], self.hex[4:]
		r, g, b = [int(n, 16) for n in (r, g, b)] 
		return (r, g, b)

	def getHSV(self):
		labObj = self.getLAB()
		hsvObj = labObj.convert_to('hsv')
		print hsvObj
		return hsvObj

	def colorDiff(self, colorB):
		colorA = self.getLAB()
		colorB = colorB.getLAB()
		return colorA.delta_e(colorB)


	
	def __repr__(self):
		return "Color: " + self.name + " Hex: " + self.hex + " Syllbs: "  + str(self.syllbs)

	
	def __str__(self):
		return "Color: " + self.name + " Hex: " + self.hex + " Syllbs: " + str(self.syllbs)


