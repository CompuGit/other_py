'''
API DOC : https://docs.tweepy.org/en/stable/api.html
'''

import tweepy
import pandas as pd
import sys

def get_users_from_file(filename):

	users_tokens = []

	try:
		file_df = pd.read_csv(filename)
		for index, row in file_df.iterrows():
			if row['active'] == 'yes':
				user = {
				'api_key' : row['api_key'],
				'api_key_secret' : row['api_key_secret'],
				'access_token' : row['access_token'],
				'access_token_secret' : row['access_token_secret'],
				'app_name': row['app name']
				}

				users_tokens.append(user)

		print('[*] file read successfully, users created.')
		return users_tokens
	except:
		print('[!] error in reading file.')
		print(sys.exc_info()[1])
		return



def default_api():
	try:
		#jeevan api
		auth = tweepy.OAuthHandler('bYEivHOzveecVVZFGEBxX3J1u', 'dg8q8bjMVzdo1jMeOiH63zD3ucfYVAB5AEPVMPvAWVYnYCJTUy')
		auth.set_access_token('1095189722106757120-sm8pJik89ghbqSkIMfhBOGk9owpPNy', 'HS3IJ8ZDD7utRP1AquDK9PhZLB7FfNuY1wYbIrzy4nlea')
		
		api = tweepy.API(auth)
		print('[!] Default Api Done')
		return api
	except:
		print('[!] Default Api error')
		print(sys.exc_info()[1])
		return


def create_user_api(users_tokens):
	apis = {}
	for user in users_tokens:
		try:
			auth = tweepy.OAuthHandler(user['api_key'], user['api_key_secret'])
			auth.set_access_token(user['access_token'], user['access_token_secret'])

			apis[user['app_name']]= tweepy.API(auth)
		except:
			print(user['app_name'],': error')
			print(sys.exc_info()[1])
	
	return apis
