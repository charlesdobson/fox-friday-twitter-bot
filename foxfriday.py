import tweepy
import os
import time

# Store access keys
consumer_key = '1cLeoWmt5u9bJcCIis8xsKJw9'
consumer_key_secret = 'pokzxnCuAyueXdogzKC3mVL7F0U3dxqZf08bfj7r8sR8XE4Vvn'
access_token = '1125477861115043840-3nTv2MjORa8oUBYoP18uOTOwNstuvl'
access_token_secret = 'kdBlhdwJU3TxHAl67cXcyYIaIRXI3GvKYxBfPnEpN7OKP'

# Connect to Twitter account
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Change to images folder
os.chdir('/Users/charlie/documents/projects/fox-friday-twitter-bot/images/foxes')

# Loop through images
for image in os.listdir('.'):
    api.update_with_media(image)
    break



