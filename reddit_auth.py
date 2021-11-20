import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
login = config['LOGIN']
keys = config['API_KEYS']


def auth():
    #OAuth2 authentication - authenticate with <CLIENT_ID> and <CLIENT_SECRET>
    client_auth = requests.auth.HTTPBasicAuth(keys['client_id'], keys['client_secret'])

    #Post data to the API to retrieve a access token (grant_type is default to 'password' for script use)
    post_data = {
        'grant_type': 'password',
        'username': login['username'],
        'password': login['password']
    }

    headers = {'User-Agent': "sub_script'/0.0.1"}

    #Post authentication request to acquire a token
    response = requests.post('https://www.reddit.com/api/v1/access_token', auth=client_auth, data=post_data, headers=headers)

    token = response.json()['access_token']

    #Updates API headers with access token
    auth.headers = {
        'Authorization': f'bearer {token}',
        'User-Agent': "sub_script'/0.0.1"
    }


