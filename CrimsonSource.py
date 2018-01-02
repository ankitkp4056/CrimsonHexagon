from CH_MonitorClient import CH_MonitorClient
from TweepyClient import TweepyClient

from datetime import date

class CrimsonSource(object):

	def __init__(self):

		self.username = 'manjira.sinha@conduent.com'
		self.password = 'password123'
		self.CONSUMER_KEY = "3A8d5KGwpp35dwGxGgEBdg"
		self.CONSUMER_SECRET = "Vl5xzjCgXM3844YE3bPwT5POOlk6AoEujGSz7wBbPmk"
		self.OAUTH_TOKEN = "364174316-ShlpvKHzUZup9rORc1q4EZPW4BrC4SZDPSIWIqcS"
		self.OAUTH_TOKEN_SECRET = "uvUmOSVwcJxKi5nP8WJFJp5XGitHc0EdhaDkLNlcJo"
 		
	def fetch_info(self, monitor_id=7187189128, from_=date(2017, 12, 11), to_=date(2017, 12, 12)):
	  # Default set for BMTC Transport monitor and 11-Dec-2017

		crimson_monitor_api = CH_MonitorClient(self.username, self.password, monitor_id)
		j_data = crimson_monitor_api.make_data_pipeline(from_, to_)
		#print("No.of docs returned from crimson=", len(j_data))
		
		# Adding Text and Time info from tweepy
		tweepy_api = TweepyClient(self.CONSUMER_KEY, self.CONSUMER_SECRET, self.OAUTH_TOKEN, self.OAUTH_TOKEN_SECRET)
		tweepy_api.add_detail(j_data) 
		#print (tweepy_api.invalid_tweet_count)      

		return j_data