import praw

reddit = praw.Reddit(client_id='jgF2ebrSIHroxw',
                     client_secret='y-oWddqWsBEWz_GO9kzd4EUBaEc', password='Mar@1234',
                     user_agent='syedPraw', username='syed2672')


subreddit = reddit.subreddit('python')


hot_python = subreddit.hot(limit=5)
for submission in hot_python:
    #print(dir(submission))         # will give all the attributes of the object
    if not submission.stickied:     #checking the post as not stickied
        #print(submission.title)     # to get the title of the objects; check it in https://www.reddit.com/r/Python/
        print('Title: {}, \nup: {}, \ndowns: {}, \nHave we visited: {}'.format(submission.title, submission.ups, submission.downs, submission.visited))
        print ("****************")


# to subscribe and unsubscribe the subreddit python call the below commands
subreddit.subscribe()
# subreddit.unsubscribe()