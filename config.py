
#API Keys
access_key = "10...........NA" # enter valid access key of your twitter application 
access_secret = "Hx...........rj" # enter valid access secret of your twitter application 
consumer_key = "3Q...........hy" # enter valid consumer key of your twitter application 
consumer_secret = "yP...........iv" # enter valid consumer secret of your twitter application 

#API Limits
max_tweets_count = 200
required_sleep_time = 60 * 15
tweets_request_quota = 900
account_data_request_quota = 900

#CSV Headers
tweets_headers = ["id", "created_at", "text"]
account_data_headers = ["friends_count", "followers_count", "favourites_count", "geo_enabled", "listed_count", "verified", "created_at", "location", "id", "name"]

#Input
users_file = "users.txt"

# Output
output_folder = "output"
tweets_name = "tweets"
account_data_name= "account_data"
account_data_file= account_data_name + ".csv"

#I/0 Constants
write_mode = "w"
append_mode = "a"
read_mode = "r"
read_or_write_mode = "rb"
