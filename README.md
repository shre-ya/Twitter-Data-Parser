
# Twitter Data Parser

## About
Python scripts that allow downloading account data and tweets for given users.

## How to use it

1. Configure API Keys and Access Tokens in `config.py`(Don't share these with anyone)
2. Adjust additional params in `config.py`
3. Prepare a list of usernames in `users.txt`

### Tweets
1. `python twitter_tweets_parser.py`
2. For each user there will be created a folder named `{user_name}` with with `{user_name}_tweets.csv` file inside it.

### Account Data
1. `python twitter_account_data_parser.py`
2. For each user there will be created a folder named `{user_name}` with with `{user_name}_account_data.csv` file inside it.
3. There will also be a single `account_data.csv` file combining all entries in output folder.
