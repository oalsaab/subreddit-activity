import asyncio
import aiohttp
from tabulate import tabulate

from reddit_auth import authenticate
from reddit_funcs import fetch

def input_minutes(minutes):
    """Requests timeframe from user, must be integer value"""
    
    while True:
        try:
            request = float(input(minutes))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break
    
    return request

def input_subreddits(subreddits):
    """Requests subreddit from user, must be less than 20 subreddits"""

    while True:
        try:
            request = input(subreddits).split()
            if len(request) > 20:
                raise ValueError
        except ValueError:
            print('Please enter less than 20 subreddits')
            continue
        else:
            break
    
    return request

async def main(headers):
    """Create one ClientSession and submit all subreddits to fetch data from, prints data in tabulated format"""

    subreddits = [subreddit for subreddit in input_subreddits('Enter subreddit(s): ')]
    minutes = input_minutes('Enter timeframe in minutes: ')

    async with aiohttp.ClientSession(headers=headers) as session:
        data = await fetch(session, subreddits, minutes)
    
    columns = ['subreddit', 'subscribers', 'accounts active', 'posts', 'comments']
    table = []
    for i in data:
        subreddit, infos, activities = i
        subscribers, accounts = infos
        posts, comments = activities
        table.append([subreddit, subscribers, accounts, posts, comments])

    print(tabulate(table, headers=columns))

if __name__ == '__main__':
    headers = asyncio.get_event_loop().run_until_complete(authenticate())
    asyncio.get_event_loop().run_until_complete(main(headers))