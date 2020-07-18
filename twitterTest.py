import GetOldTweets3 as got;

word = 'fuck';
f = open("usernameTest.txt", "a");

tweetCriteria = got.manager.TweetCriteria().setQuerySearch(word).setMaxTweets(10);
tweets = got.manager.TweetManager.getTweets(tweetCriteria);
for tweet in tweets:
    print(tweet.text + ' BY: ' + tweet.username + '\n');
    if word in tweet.text.lower():
        print('This has ' + word + ' in it.\n');
        f.write(tweet.username + '\n');
        
    else:
        print('This does not have ' + word + ' in it.\n');
f.close();
