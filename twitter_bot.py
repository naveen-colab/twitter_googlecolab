import tweepy  #authentication
def authentication():
  consumer_key=os.getenv("consumer_key")
  consumer_secret=os.getenv("consumer_secret")
  access_token=os.getenv(" access_token")
  access_token_secret=os.getenv("access_token_secret")
  
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  api.verify_credentials()
  print("api created")
  return api
 
 def new_name(user):
  emoji_dict={0:"0️⃣",1:"1️⃣",2:"2️⃣",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
  emoji_list ="".join([emoji_dict[int(i)] for i in str(user.followers_count) if int(i) in emoji_dict.keys()])
  return emoji_list


def change_the_id():
  api .update_profile(name = f"itsmenaveen|{new_name(user)}")
  print( f"chandrateja|{new_name(user)}")
  print("waiting to refresh")
  time.sleep(60)
  
api = authentication()
user = api.get_user("@Chandra34570619")
prev_count_of_followers = user.followers_count
while True:
  if prev_count_of_followers != user.followers_count:
    print("changed",user)
    change_the_id(user)
     
