import twint
import schedule
import time


# you can change the name of each "job" after "def" if you'd like.

def jobone():
	print ("Fetching Tweets")
	c = twint.Config()
		# choose username (optional)
	c.Username = "Dutzee"
		# choose beginning time (narrow results)
	c.Since = "2018-01-01"
		# choose beginning time (narrow results)
	c.Until = "2018-12-01"
		# set limit on total tweets
	c.Limit = 1000
		# no idea, but makes the csv format properly
	c.Store_csv = True
		# format of the csv
		# c.Custom = ["date", "time", "username", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags"]
		# change the name of the csv file
	c.Output = "Dutzee.csv"
	twint.run.Search(c)

#def jobtwo():
#	print ("Fetching Tweets")
#	c = twint.Config()
		# choose username (optional)
#	c.Username = "djokernole"
		# choose search term (optional)

#	c.Since = "2018-01-01"
		# set limit on total tweets
#	c.Until = "2018-12-01"
		# set limit on total tweets
#	c.Limit = 1000
		# no idea, but makes the csv format properly
#	c.Store_csv = True
		# format of the csv
		#c.Custom = ["date", "time", "username", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags"]
		# change the name of the csv file
#	c.Output = "djokernole2.csv"
#	twint.run.Search(c)#

	# run once when you start the program

jobone()
#jobtwo()
