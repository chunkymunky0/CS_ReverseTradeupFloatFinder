import json


desiredFloat = 0
minFloat = 0
maxFloat = 0
endFloat = 0
avgFloat = 0
floatRange = 0
floats = [0.2, 0.5, 0.25, 0.25, 0.4, 0.7, 0.01, 0.5, 0.2, 0.2]


class endFloatCalc:
	def __init__(self, minFloat = None, maxFloat = None, endFloat = None, floatRange = None, avgFloat = None):
		self.__minFloat = minFloat
		self.__maxFloat = maxFloat
		self.__endFloat = endFloat
		self.__avgFloat = avgFloat
		self.__floatRange = floatRange

	def getMinFloat(self):
		return self.__minFloat
	
	def setMinFloat(self, newMinFloat):
		self.__minFloat = newMinFloat

	def getMaxFloat(self):
		return self.__maxFloat
	
	def setMaxFloat(self, newMaxFloat):
		self.__maxFloat = newMaxFloat

	def getFloatRange(self):
		return self.__floatRange
	
	def setFloatRange(self, newFloatRange):
		self.__floatRange = newFloatRange

	def getAvgFloat(self):
		return self.__avgFloat
	
	def setAvgFloat(self, newAvgFloat):
		self.__avgFloat = newAvgFloat

	def getEndFloat(self):
		return self.__endFloat
	
	def calcEndFloat(self):
		self.__endFloat = ((self.getFloatRange * self.getAvgFloat) + self.getMinFloat)
		return self.getEndFloat
	
	def __str__(self) -> str:
		return "Final Output Float: {}".format(self.getEndFloat())

	
def findMaxMinAndAvgFloats(floats):
	sum = 0.0
	for i in floats:
		if sum == 0:
			minFloat = i
			maxFloat = i
			sum = i
			continue
		
		sum = sum + i
		
		if i > maxFloat:
			maxFloat = i
		if i < minFloat:
			minFloat = i
	
	floatRange = maxFloat - minFloat
	avgFloat = sum/10
	


def __main__():
	#To be added later
	#desiredFloat = input("What float do you want?")
	newOutput = endFloatCalc()
	findMaxMinAndAvgFloats(floats)
	newOutput.setAvgFloat(avgFloat)
	newOutput.setMaxFloat(maxFloat)
	newOutput.setMinFloat(minFloat)
	newOutput.setFloatRange(floatRange)
	print(newOutput.__str__())
	

if __name__ == "__main__":
	__main__()