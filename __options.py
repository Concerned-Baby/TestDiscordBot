import random

global fatquotes
global namereplace
namereplace = "*[77687920776f756c64207520646f2074686973]*"
fatquotes = [
	namereplace + " is fat lmao\n",
	namereplace + " has a double chin lmao\n",
	namereplace + " is like my mom\n",
	namereplace + " is way too thicc\n"
]

def fatgenerate(name):
	return fatquotes[int(random.uniform(0, len(fatquotes)))].replace(namereplace, name)
