import tweepy
import datetime 

import tweepy

auth = tweepy.OAuthHandler("consumer_key","consumer_secret")
auth.set_access_token("access_token","access_token_secret")

api = tweepy.API(auth)

release_date = datetime.date(2021,11,12) 
today = datetime.date.today() 

hours_to_release = release_date - today 
days_to_release = hours_to_release.days  

if days_to_release !=1:   
  api.update_status("Faltam " + str(days_to_release) + " dias para a Taylor Swift lançar o Red (Taylor's Version)")
        
if days_to_release == 1:
  api.update_status("Falta " + str(days_to_release) + " dia para a Taylor Swift lançar o Red (Taylor's Version)!!!")