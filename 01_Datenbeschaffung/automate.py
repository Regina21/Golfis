import twint
from multiprocessing import Process
import schedule
import time

# this runs a loop for each user in the users list

def jobone(user):
	print ("Fetching Tweets")
	c = twint.Config()

		# username is the list of users
	c.Username = user

		# beginning time (narrow results)
	c.Since = "2017-01-01"

		# ending time (narrow results)
	c.Until = "2018-12-31"

		# limit on total tweets
	c.Limit = 1000

		# format of storage
	c.Store_csv = True

		# name of the csv file
	c.Output = "twint"

	twint.run.Search(c)

# best 10 men & best 10 women of tennis
users = ["djokernole", "RafaelNadal", "ThiemDomi", "rogerfederer",
 		"keinishikori", "KAndersonATP",
		"delpotrojuan", "JohnIsner", "StefTsitsipas", "cilic_marin",
		"Naomi_Osaka_", "Simona_Halep", "Petra_Kvitova", "KaPliskova",
		"AngeliqueKerber", "ElinaSvitolina", "kikibertens", "SloaneStephens",
		"ashbar96", "SabalenkaA", "serenawilliams"]

for user in users:

	jobone(user)
