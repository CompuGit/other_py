'''
API DOC : https://docs.tweepy.org/en/stable/api.html
'''

from twitter_api import *
from texts import *

from time import sleep, time, ctime

import threading

def make_tweets(user,api,texts,m=10,n=300,media=False,medialist='./images'):
	
	texts = texts.copy()
	
	flag = False
	if media:
		flag=True
		media = ['./images/'+name for name in os.listdir(medialist)]

	timeout = time()+60*m

	for i in range(1000):
		try:

			text = choice(texts)
			texts.remove(text)

			
			if flag:
				api.update_status_with_media(text,choice(media))
				print(f' {user} {i+1} tweet made.')
			else:
				api.update_status(text)
				print(f' {user} {i+1} tweet made.')
			
			n-=1
			
			if time()>timeout:
				print(f'{user} timeoout completed. number tweets done = {i+1}')
				break
			elif n==0:
				print(f'{user} requested number of tweets done number tweets done = {i+1}')
				break
		except:
			print(sys.exc_info()[1])




if __name__=='__main__':



	texts = text_randomizer(200)
	'''
	d_api = default_api()
	print(ctime(time()))
	make_tweets(d_api,texts,n=100,media=True)
	print(ctime(time()))
	'''
	
	users_tokens = get_users_from_file('./user_base.csv')
	apis = create_user_api(users_tokens)


	for user,api in apis.items():
		print(format(user,'=^30'))
		threading.Thread(target = make_tweets, args = (user,api,texts,10,100,True)).start()
		#make_tweets(d_api,texts,n=100,media=True)

	
