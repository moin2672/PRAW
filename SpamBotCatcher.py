import praw

import GetCred as c

reddit = praw.Reddit(client_id=c.client_id,
                     client_secret=c.client_secret, password=c.password,
                     user_agent=c.user_agent, username=c.username)


def findSpam(search_term):
    authors=[]
    for submission in reddit.subreddit("all").search(search_term, sort="new", limit=10):
        print (submission.title, submission.author, submission.url)
        if submission.author not in authors:
            authors.append(submission.author)
    return authors


if __name__ == "__main__":
    authors=findSpam('Free Udemy')
    for author in authors:
        print (str(author))