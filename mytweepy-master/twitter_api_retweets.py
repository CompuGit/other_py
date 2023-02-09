'''
API DOC : https://docs.tweepy.org/en/stable/api.html
'''

from twitter_api import *
import pandas as pd
from time import time
import sys, os

import threading

def search_tweets(api,hashtag,n):

	tweets = set()

	try:
		for tweet in tweepy.Cursor(api.search_tweets, hashtag).items():

			tweets.add(tweet)

			if len(tweets)==n:
				break

		print('[*] tweets gathered.')
	except:
		print('[!] error in gathering tweets.')
		print(sys.exc_info()[1])

	return tweets


def retweet_bulk(api,tweets_ids):

		print(format(user,'=^30'))
		timeout = time()+ 60
		for t_id in tweets_ids:
			try:
				api.retweet(t_id); print(f'{t_id} : retweeted')
				if time()>timeout:
					print('timeoout completed')
					break
			except:
				if '453' in str(sys.exc_info()[1]):
					print('[!] 453 - no Eleveted Access to the api')
					break
				if '327' in str(sys.exc_info()[1]):
					print(f'[!] 327 - aleady retweeted {t_id}')

		print('[*] tweets completed.')


if __name__=='__main__':


	users_tokens = get_users_from_file('./user_base.csv')
	apis = create_user_api(users_tokens)

	d_api = default_api()
	tweets = search_tweets(d_api,'#10yearsUpasanaCharan',250)
	tweets_ids = [tweet.id for tweet in tweets]

	for user,api in apis.items():
		threading.Thread(target=retweet_bulk, args=(api,tweets_ids)).start()

	'''
	for user,api in apis.items():

		print(format(user,'=^30'))
		timeout = time()+ 60
		for t_id in tweets_ids:
			try:
				api.retweet(t_id); print(f'{t_id} : retweeted')
				if time()>timeout:
					print('timeoout completed')
					break
			except:
				if '453' in str(sys.exc_info()[1]):
					print('[!] 453 - no Eleveted Access to the api')
					break
				if '327' in str(sys.exc_info()[1]):
					print(f'[!] 327 - aleady retweeted {t_id}')

		print('[*] tweets completed.')
	'''
