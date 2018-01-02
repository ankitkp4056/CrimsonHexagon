from CrimsonSource import CrimsonSource
import timeit
import argparse
import datetime

if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	# Basic model parameters.
	parser.add_argument('--monitor_id', type=int, default=0,
                    	help='Monitor ID of the CrimsonHexagon monitor ')

	#FLAGS = parser.parse_args()
	FLAGS = parser.parse_known_args()
	
	try: 
		FLAGS.monitor_id
	except:
		FLAGS = FLAGS[0]
	
	
	#monitor_id = 7187189128    # BMTC Transport monitor
	#start_date = datetime.date(2017, 12, 4)  # Monitoring Start Date at 00:00:00 
	#end_date   = datetime.date(2017, 12, 5)  # Monitoring End date at 00:00:00

	monitor_id = FLAGS.monitor_id 
	start_date = datetime.date.today() - datetime.timedelta(1)  # Monitoring Start Date at 00:00:00 
	end_date   = datetime.date.today()                 # Monitoring End date at 00:00:00
	
	source = CrimsonSource()      ## Creating an instance of class CrimsonSource
	
	#print ("---Fetching Tweets---")
	#start_time = timeit.default_timer()
	
	json_data = source.fetch_info(monitor_id= monitor_id, from_= start_date, to_= end_date)     ## Fetching info from Crimson and Tweepy
	
	#elapsed_time = timeit.default_timer()
	#print ("---Tweets fetched Successfully in ", elapsed_time/60, " minutes---", )	
	
	entries_count = len(json_data)
	print ("Total no. of entries = ", entries_count)

	j_str = str(json_data)
	print (j_str.encode("utf-8"))
	