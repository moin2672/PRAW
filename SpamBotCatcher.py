import praw
import random
import GetCred as c

common_spamy_words = {'udemy','course','save','coupon','free','discount'}

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
    while True:
        current_search_term = random.choice(['udemy'])
        spam_content=[]
        trashy_users={}
        smelly_authors=findSpam(current_search_term)

        for author in smelly_authors:
            user_trashy_urls=[]
            sub_count=0
            dirty_count=0

            try:
                for sub in reddit.redditor(str(author)).submissions.new():
                    submit_inks_to = sub.url
                    submit_id= sub.id
                    submit_subreddit= sub.subreddit
                    submit_title=sub.title

                    dirty=False

                    for w in common_spamy_words:
                        if w in submit_title.lower():
                            dirty=True
                            junk=[submit_id, submit_title]
                            if junk not in user_trashy_urls:
                                user_trashy_urls.append([submit_id, submit_title, str(author)])

                    if dirty:
                        dirty_count+=1
                    sub_count+=1

                try:
                    trashy_score = dirty_count/sub_count

                except: trashy_score=0.0

                print("Users: {} trashy score is: {}".format(str(author), round(trashy_score,3)))

                if trashy_score>=0.5:
                    trashy_users[str(author)]=[trashy_score, sub_count]

                    for trash in user_trashy_urls:
                        spam_content.append(trash)

            except Exception as e:
                print (str(e))

