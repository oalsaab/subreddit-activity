import asyncio
import datetime

async def info(session, subreddit):
    """Retrieves number of subscribers and active accounts for a given subreddit"""

    async with session.get(f'https://oauth.reddit.com/r/{subreddit}/about') as response:
        response.raise_for_status()
        body = await response.json()
    try:
        subscribers = body['data']['subscribers']
        accounts = body['data']['accounts_active']
    except KeyError:
        return 'n/a', 'n/a'
    
    return subscribers, accounts

async def activity(session, subreddit, minutes):
    """Retrieves json data for a given subreddit and returns number of posts and comments for given timeframe"""

    async with session.get(f'https://oauth.reddit.com/r/{subreddit}/new') as response:
        body = await response.json()
    
    items = body['data']['children']
    if not items:
        return 'n/a', 'n/a'
    else:
        data = items

    posts = []
    comments = []
    for i in data:
        post = i['data']['created_utc']
        comment = i['data']['num_comments']

        converted = datetime.datetime.fromtimestamp(post)
        difference = datetime.datetime.now() - datetime.timedelta(minutes=minutes)

        if difference < converted:
            posts.append(converted)
            comments.append(comment)

    return len(posts), sum(comments)

async def fetch(session, subreddits, minutes):
    """Submit coroutines for execution and gather awaitables, returns zipped subreddit data"""

    infos = []
    activities = []
    for subreddit in subreddits:
        i = asyncio.create_task(info(session, subreddit))
        a = asyncio.create_task(activity(session, subreddit, minutes))
        infos.append(i)
        activities.append(a)
    
    info_task = await asyncio.gather(*infos)
    activity_task = await asyncio.gather(*activities)
    data = list(zip(subreddits, info_task, activity_task))

    return data