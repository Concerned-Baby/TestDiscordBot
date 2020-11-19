import random

global fatquotes
global namereplace
namereplace = "*[77687920776f756c64207520646f2074686973]*"
fatquotes = [
	namereplace + "is fat lmao\n",
	namereplace + "has a double chin lmao\n"
]

def fatgenerate(name):
	random.seed(namereplace)
	return fatquotes[random.uniform(0, len(fatquotes) - 1)].replace(namereplace, name)
