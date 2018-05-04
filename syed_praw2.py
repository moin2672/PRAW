import praw

reddit = praw.Reddit(client_id='jgF2ebrSIHroxw',
                     client_secret='y-oWddqWsBEWz_GO9kzd4EUBaEc', password='Mar@1234',
                     user_agent='syedPraw', username='syed2672')


subreddit = reddit.subreddit('news')

# for comment in subreddit.stream.comments():   # to get stream of data
#     try:
#         parent_id=str(comment.parent())
#         original = reddit.comment(parent_id)
#
#         print("Parent: \n" + original.body)
#         print ('Reply: \n', comment.body)
#
#     except praw.exceptions.PRAWException as e:
#         pass

for submission in subreddit.stream.submissions():   # to get stream of data
    try:
       print (submission.title+"\n"+"*"*20)

    except Exception as e:
        print(str(e))

