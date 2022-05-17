<<<<<<< HEAD
# subreddit-activity
=======
# Subreddit Activity

A simple python script that uses the reddit API to display the number of posts and comments for a given subreddit within a specified timeframe. 
The result are displayed and tabulated on the command line interface.

Reddit API: https://www.reddit.com/dev/api/ <br />
Obtain your reddit access token: https://www.reddit.com/prefs/apps

## Example

For example, in the last 60 minutes how many posts and comments were there in the subreddits: 'news', 'AskReddit', 'funny' and 'soccer'?

![subreddit-act](https://user-images.githubusercontent.com/94754943/146647629-ecba18f7-43e6-45b8-957e-6dbb44fdbd71.png)

The script allows you to compare activities between subreddits in a very simplified manner.

## Installation

Clone the repository and install the python dependancies.

``` git clone https://github.com/oalsaab/subreddit-activity ```

Create a configuration file (INI) with the following structure

```
[API_KEYS] 
client_id = Your client id 
client_secret = Your client secret

[LOGIN]
username = Your reddit username
password = Your reddit password
```
>>>>>>> 3a74a1e4641651224daabdcedbe745fa80c437de
