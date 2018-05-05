import praw
import random
import GetCred as c
import time
common_spamy_words = {'udemy','course','save','coupon','free','discount'}

reddit = praw.Reddit(client_id=c.client_id,
                     client_secret=c.client_secret, password=c.password,
                     user_agent=c.user_agent, username=c.username)


def findSpam(search_term):
    authors=[]
    for submission in reddit.subreddit("all").search(search_term, sort="new", limit=5):
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
                                # print("thrash in url")
                                # print(user_trashy_urls)

                    if dirty:
                        dirty_count+=1
                    sub_count+=1

                try:
                    trashy_score = dirty_count/sub_count

                except: trashy_score=0.0

                print("Users: {} trashy score is: {}".format(str(author), round(trashy_score,3)))

                if trashy_score>=0.5:
                    trashy_users[str(author)]=[trashy_score, sub_count]
                    print(trashy_users)
                    # print(user_trashy_urls)

                    for trash in user_trashy_urls:
                        spam_content.append(trash)
                        # print("spam content")
                        # print(spam_content)
            except Exception as e:
                print (str(e))

        for spam in spam_content:
            print("spam")
            print(spam)
            spam_id=spam[0]
            spam_user=spam[2]
            submission=reddit.submission(id==spam[0])

            created_time=submission.created_utc
            print(time.time()-created_time)
            print(time.time()-created_time <=229287000)
            if time.time()-created_time <=229287000:
                link="https://reddit.com"+submission.permalink

                print(link)
                print("**message**")
                message="""*Beep boop
                Bot sniffs out spammer
                spam {}% of {} submission from /u/{}""".format(round(trashy_users[spam_user][0]*100,2), trashy_users[spam_user][1],spam_user)

                try:
                    with open("posted_urls.txt","r") as f:
                        already_posted = f.read().split('\n')

                    if link not in already_posted:
                        print(message)
                        # submission.reply(message)

                        print("We have posted to {} and now we need to sleep for 12 minutes" .format(link))

                        with open("posted_urls.txt","a") as f:
                            f.write(link+'\n')
                            print('#### written in the text file #####')

                        time.sleep(12*60)
                        break

                except Exception as e:
                    print(str(e))
                    time.sleep(12*60)