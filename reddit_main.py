from reddit_funcs import request_subreddit, time_created, request_subreddit_info
from tabulate import tabulate

subreddits = ['wow', 'genshin_impact', 'ffxiv', 'classicwow', 'games']
minutes = 30

main_list = []
for subreddit in subreddits:
    request_subreddit(subreddit)
    subscribers = request_subreddit_info(subreddit)[0]
    accounts_active = request_subreddit_info(subreddit)[1]
    posts = time_created(subreddit, minutes)[0]
    comments = time_created(subreddit, minutes)[1]
    response_list = [subreddit, subscribers, accounts_active, posts, comments]
    main_list.append(response_list)

columns = ['subreddit', 'subscribers', 'accounts_active', 'posts', 'comments']

print(tabulate(main_list, headers=columns))


#function that keeps requesting integer as value
# def input_minutes(message):
#     while True:
#         try:
#             minutes_input = float(input(message))
#         except ValueError:
#             print('Please enter a number')
#             continue
#         else:
#             return minutes_input
#             break

