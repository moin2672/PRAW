import praw

reddit = praw.Reddit(client_id='jgF2ebrSIHroxw',
                     client_secret='y-oWddqWsBEWz_GO9kzd4EUBaEc', password='Mar@1234',
                     user_agent='syedPraw', username='syed2672')


subreddit = reddit.subreddit('python')


hot_python = subreddit.hot(limit=10)
for submission in hot_python:
    print(submission)