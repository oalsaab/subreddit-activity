import aiohttp
import configparser

async def authenticate():
    """Authenticates with reddit credentials and API keys to retrieve access token"""
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    login = config['LOGIN']
    keys = config['API_KEYS']

    post_data = {
        'grant_type': 'password',
        'username': login['username'],
        'password': login['password']
    }

    url = 'https://www.reddit.com/api/v1/access_token'
    headers = {'User-Agent': "sub_script'/0.0.1"}
    auth = aiohttp.BasicAuth(keys['client_id'], keys['client_secret'])

    async with aiohttp.ClientSession() as session:
        async with session.post(url, auth=auth, data=post_data, headers=headers) as response:
            response.raise_for_status()
            body = await response.json()
        
    token = body['access_token']
    headers = {'Authorization': f'bearer {token}', 'User-Agent': "sub_script'/0.0.1"}

    return headers