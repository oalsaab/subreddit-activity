import requests
import datetime
from reddit_auth import auth

auth()

def request_subreddit_info(subreddit):
    res = requests.get(f'https://oauth.reddit.com/r/{subreddit}/about', headers=auth.headers)
    res.raise_for_status()
    res_json = res.json()
    items_subscribers = res_json['data']['subscribers']
    items_accounts_active = res_json['data']['accounts_active']
    return items_subscribers, items_accounts_active
    
def request_subreddit(subreddit):
    res = requests.get(f'https://oauth.reddit.com/r/{subreddit}/new', headers=auth.headers)
    res.raise_for_status()
    res_json = res.json()
    items = res_json['data']['children']
    if not items:
        raise RuntimeError(f'The subreddit "{subreddit}" does not exist')
    else:
        return items

#Function that returns the number of posts for a time specfied from user
def time_created(subreddit, minutes_param):
    list_times = []
    list_comments = []
    #Loops over all the posts in 'new' and selects the creation date value
    for i in request_subreddit(subreddit):
        time = i['data']['created_utc']
        comments = i['data']['num_comments']
        time_converted = datetime.datetime.fromtimestamp(time)
        time_input = datetime.datetime.now() - datetime.timedelta(minutes = minutes_param)
        if time_input < time_converted:
            list_times.append(time_converted)
            list_comments.append(comments)
    
    return len(list_times), sum(list_comments)












