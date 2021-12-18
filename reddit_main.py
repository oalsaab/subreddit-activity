from reddit_funcs import request_subreddit, time_created, request_subreddit_info
from tabulate import tabulate


# Function that keeps requesting integer as value
def input_minutes(request_minutes):
    while True:
        try:
            minutes_input = float(input(request_minutes))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            return minutes_input
            break


subreddits = [subreddit for subreddit in input('Enter subreddit(s): ').split()]
minutes_input = input_minutes('Enter in minutes timeframe: ')

main_list = []
# Loops over all the subreddits provided by user and performs the functions on each subreddit
for subreddit in subreddits:
    request_subreddit(subreddit)
    
    subscribers, accounts_active = request_subreddit_info(subreddit)
    
    posts, comments = time_created(subreddit, minutes_input)
    
    response_list = [subreddit, subscribers, accounts_active, posts, comments]
    
    main_list.append(response_list)

columns = ['subreddit', 'subscribers', 'accounts_active', 'posts', 'comments']

print(tabulate(main_list, headers=columns))



