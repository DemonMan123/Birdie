# pip install tweepy
# pip install pyfiglet
import tweepy
import webbrowser
import time
import pyfiglet
from pyfiglet import Figlet
Loopstart = 1000

#Auth start
print("You'll need to enter your API key and your Secret API key.")
print("These are found at https://developer.twitter.com/")
print("Make sure to give it Read, Write, and read/write Direct messages permissions, or else some features may not work.")
print(" ")
input("Press 'Enter' to continue... ")


ascii_banner = pyfiglet.figlet_format("Login")
print(ascii_banner)
ConsumerKeyInput = input("Please enter your API key: ")
ConsumerSecretKeyInput = input("Please enter your API secret key: ")
time.sleep(2)
for i in range(50):
    print(" ")
    
consumer_key = ConsumerKeyInput
consumer_secret_key = ConsumerSecretKeyInput

callback_uri = 'oob' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key, callback_uri)
redirect_url = auth.get_authorization_url()
print("Redirect URL:", redirect_url)

webbrowser.open(redirect_url)

ascii_banner = pyfiglet.figlet_format("Welcome!")
print(ascii_banner)
user_pin_input = input("Please input the code given to you: ")
user_pin_input
auth.get_access_token(user_pin_input)
for i in range(50):
    print(" ")

api = tweepy.API(auth, wait_on_rate_limit = True)
me = api.me()
#Auth end

#Running actions

while Loopstart == 1000:
    # Options start
    ascii_banner = pyfiglet.figlet_format("Piano")
    print(ascii_banner)
    print("T - Tweet Menu ")
    print(" ")
    print("O - Others menu")
    print(" ")
    print("================================================")
    print("Developer: DemonMan123/Demin")
    print("Current logged in as:", me.screen_name)
    # Options end
    
    
    print(" ")
    menu_Selection = input("What action would you like to do? ")
    for i in range(10): #Clear terminal
        print(" ")
        
    if menu_Selection == "T":
        ascii_banner = pyfiglet.figlet_format("Tweet Menu")
        print(ascii_banner)
        print("1 - Create a tweet")
        print(" ")
        print("2 - remove a tweet")
        print(" ")
        print("3 - Favorite a tweet")
        print(" ")
        print("4 - Unfavorite a tweet")
        print(" ")
        print("5 - Retweet a tweet")
        print(" ")
        print("6 - Grab the username and ID of a tweets retweeters")
        print(" ")
        print("99 - back")
        print(" ")
        TweetSelection = input("Please enter an option: ")
        for i in range(4): #Clearing
            print(" ")

        
        
        
        if TweetSelection == "1": # Checking the options
            UserTweet = input("Enter a tweet to create: ") # Waiting for user to input a tweet

            new_status = api.update_status(UserTweet) # Tweeting what the user inputted 
            print("Tweet created:", UserTweet) # Printing out the tweet
            time.sleep(3) # Waiting 3 seconds
            for i in range(10): #Clearing the console
                print(" ")
        
        elif TweetSelection == "2":
            TweetDestroy = input("Please enter the ID of the tweet you would like to remove: ")
            api.destroy_status(TweetDestroy)
            time.sleep(1)
            print(" ")
            print("Tweet removed")
            time.sleep(3)
            for i in range(5):
                print(" ")
            
        elif TweetSelection == "3":
            FavoritePost = input("Enter a post id that you would like to favorite: ")
            time.sleep(1)
            print(" ")
            api.create_favorite(FavoritePost)
            print("Favorited: ", FavoritePost)
            time.sleep(3)
            for i in range(5):
                print(" ")
                
        elif TweetSelection == "4":
            UnFavoritePost = input("Enter the ID of the post you would like to unfavorite: ")
            print(" ")
            api.destroy_favorite(UnFavoritePost)
            print("Removed the favorite for the post with the ID: ", UnFavoritePost)
            time.sleep(3)
            for i in range(5):
                print(" ")
                
        elif TweetSelection == "5":  
            UserRetweet = input("Enter the ID of the tweet you would like to retweet: ") # Waiting for user input
            api.retweet(UserRetweet) # Retweeting
            print("Retweeted ", UserRetweet) # Printing out the confirmation
            time.sleep(3)
            for i in range(10): # Clearing the console
                print(" ")
                
        elif TweetSelection == "6":
            TweetID = input("Enter the ID of the tweet: ")
            Count = input("How many users would you like to grab: ")
            retweetlist = api.retweets(TweetID, Count)
            for retweet in retweetlist:
                print(retweet.user.screen_name + " ID: ", + retweet.user.id)
            a = input("Press enter to continue... ")
            
        else:
            print("Returning to main menu in 2s!")
            time.sleep(2)
            for i in range(10):
                print(" ")
                
                
                
                
                
                
                
                
                
    if menu_Selection == "O":
        ascii_banner = pyfiglet.figlet_format("Others Menu")
        print(ascii_banner)
        print(" ")
        print("1 - follow a user")
        print(" ")
        print("2 - Unfollow a user")
        print(" ")
        print("3 - List current followers")
        print(" ")
        print("4 - Send a direct message")
        print(" ")
        print("99 - back")
        print(" ")
        OtherSelection = input("Please enter a valid option! ")
        for i in range(4): #Clearing
            print(" ")
        
        if OtherSelection == "1":
            idurl = "https://codeofaninja.com/tools/find-twitter-id/" # Declaring the URL
            # Information segment start
            print("Feed me the @ or ID of the person you would like to follow. ")
            print(" ")
            print("Opening website for IDs in 2s") 
            # Information segment end
            time.sleep(3) # Waiting for 2s
            webbrowser.open(idurl) # Opening the website URL
            print(" ") # Spacing
            friends = input("ID or @: ") # Waiting for the ID/tag of the twitter user
        
        
        
            api.create_friendship(friends) # following the user
            print("Followed: ", friends) # Printing out the followed user
            time.sleep(3) # Waiting 3 seconds again
            for i in range(10): # Clearing the console
                print(" ")
                
        elif OtherSelection == "2":
            idurl = "https://codeofaninja.com/tools/find-twitter-id/" # Declaring the URL
            # Information segment start
            print("Feed me the @ or ID of the person you would like to unfollow. ")
            print(" ")
            print("Opening website for finding a user id in 2s") 
            # Information segment end
            time.sleep(2) # Waiting for 2s
            webbrowser.open(idurl) # Opening the website URL
            print(" ") # Spacing
            UnfollowUser = input("ID or @: ") # Waiting for the ID/tag of the twitter user
        
            api.destroy_friendship(UnfollowUser) # removing the follow
            print("Removed follow for", UnfollowUser) # Printing out the follow
            time.sleep(3)
            for i in range(5):
                print(" ")
                
        elif OtherSelection == "3":
            TargetProfileUsername = input("Enter the username to return followers of: ")
            for follower in api.followers(TargetProfileUsername):
                print(follower.screen_name)
            time.sleep(2)
            print(" ")
            print(" ")
            print("Done!")
            time.sleep(3)
            for i in range(5):
                print(" ")
                
        elif OtherSelection == "4":
            UserDirMessage = input("Enter the user, screenname, or user id to send a direct message to: ")
            MessageContent = input("Enter the message: ")
        
            api.send_direct_message(UserDirMessage, MessageContent)
            print("Sent a direct message to:", UserDirMessage, "with the contents:", MessageContent)
            time.sleep(3)
            for i in range(5):
                print(" ")
                
        elif OtherSelection == "5":
            MessageCount = int(input("How many messages would you like to retrieve? "))
            last_dms = me.list_direct_messages(1)
            for messages in last_dms:
                print(messages.text)
                
        else:
            print("Returning to main menu in 2s!")
            time.sleep(2)
            for i in range(10):
                print(" ")
