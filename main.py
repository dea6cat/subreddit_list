
from alive_progress import alive_bar
import praw
import pandas as pd
# Read-only instance
reddit = praw.Reddit(client_id="Your client ID",		 # your client id
								client_secret="You client secret",	 # your client secret
								user_agent="Your user agent")	 # your user agent

#pandas dataframe headers
subreddit_dict = {"Display Name":[], "Description":[], "NSFW":[], "Link":[]}
#alphabet list
az = ('A', 'B', 'C', 'D', 'E', 'F', 'G',
      'H', 'I', 'J', 'K', 'L', 'M', 'N',
      'O', 'P', 'Q', 'R', 'S', 'T', 'U',
      'V', 'W', 'X', 'Y', 'Z')
bar= 0 #this is used for alive_progress to set a limit for the progress bar
for i in az: # this forloop will go through the elements within the az list
    for subreddit in reddit.subreddits.search_by_name(i): #this will take the value on i from the first forloop to look the subreddits under that letter
        bar+=1 #This will add to the int variable bar


with alive_bar(bar) as bar: #This begins the progress bar using the bar variable to set the limit
    for x in az: # this forloop will go through the elements within the az list
        for subreddit in reddit.subreddits.search_by_name(x): #this will take the value on i from the first forloop to look the subreddits under that letter
            print(subreddit)#print the subreddits Name of the subreddit.
            subreddit_dict["Display Name"].append(subreddit.display_name) #add to dictionary Name of the subreddit.
            subreddit_dict["Description"].append(subreddit.description) #add to dictionary Subreddit description, in Markdown.
            subreddit_dict["Link"].append(subreddit.url) #add to dictionary Subreddit url
            subreddit_dict["NSFW"].append(subreddit.over18) #add to dictionary Whether the subreddit is NSFW.
            bar() #add progress to the progress bar


# Saving the data in a pandas dataframe
sub = pd.DataFrame(subreddit_dict)
print(sub) #print pandas dataframe
sub.to_csv("subreddits.csv", index=True) #Exporting Data to a CSV File
