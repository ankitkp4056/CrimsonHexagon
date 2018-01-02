import tweepy

class TweepyClient(object):
    """Interacts with the Tweepy API to retrieve post/tweet data from twitter
    """

    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET):
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET = CONSUMER_SECRET
        self.OAUTH_TOKEN = OAUTH_TOKEN
        self.OAUTH_TOKEN_SECRET = OAUTH_TOKEN_SECRET
        self._auth()
        self.invalid_tweet_count = 0
        

    def _auth(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.OAUTH_TOKEN, self.OAUTH_TOKEN_SECRET)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        #print('-- Twitter Authenticated --')
        return
        
    def get_tweet_from_url(self, url):
        tweet_id = url.split('/')[-1]
        tweet = self.api.get_status(tweet_id, tweet_mode='extended')
        return [tweet._json['full_text'], tweet._json['created_at']]

    def add_detail(self, json_data):
        for post in json_data:
            if post['type'] == 'Twitter':
                try: 
                    tweet_info = self.get_tweet_from_url(post['url'])
                    post['text'] = tweet_info[0]          #INFO received from tweepy 
                    post['created_at'] = tweet_info[1]    #INFO received from tweepy
                    ## More info can be added similarly
                    
                except:
                    self.invalid_tweet_count += 1      ## Counts no. of tweets that were not available on twitter


