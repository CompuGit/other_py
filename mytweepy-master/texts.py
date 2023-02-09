import os, json
from random import choice, shuffle, randint


def text_randomizer(n):

	with open('./texts.json','r') as jsonFile:
		jsonObj = json.load(jsonFile)

	phrases = list(jsonObj['phrases'].values())
	keywords = list(jsonObj['keywords'].values())
	hashtags = list(jsonObj['hashtags'].values())
	usertags = list(jsonObj['usertags'].values())
	funks = jsonObj['funks']

	emojis = [ "🔥🔥", "❤💕", "👑💫", "💐💐💐", "🤴❤👸" ]


	texts = []

	while n!=0:
		lst = [	choice(phrases)+' '+choice(keywords)+' '+choice(emojis)+'\n'+choice(hashtags),
					choice(funks)+' '+choice(keywords)+'\n'+choice(hashtags),
					choice(emojis)+' '+choice(phrases)+'\n'+choice(hashtags),
					choice(hashtags)+'\n'+choice(phrases)+' '+choice(funks)+choice(keywords)+choice(emojis)
				]
		texts.extend(lst)

		n-=1

	texts = list(set(texts))
	shuffle(texts)
	return texts

if __name__ == '__main__':
	
	for each in text_randomizer(200):
		print(each, end='\n=============\n')