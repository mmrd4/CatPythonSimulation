import tweepy

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAANiWqQEAAAAAWOdOSkmccSYZh3n%2BErFtABKC8ok%3DilbLxoOCTI2CUjE5uxOOCl9RCQOpoZBlgIZGG2TG2vgH7TGtgx")
api = tweepy.API(auth)