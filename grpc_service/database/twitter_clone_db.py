from . import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(f"mysql+mysqldb://dbuser:dbuser@123@localhost/Twitter_grpc")
Session = sessionmaker(bind=engine)
session = Session()


def get_all_tweets():
    all_tweets = (
        session.query(models.Tweet)
        .order_by(models.Tweet.last_edited_at.desc())
        .order_by(models.Tweet.posted_at.desc())
        .all()
    )
    return all_tweets


def get_tweets(request):
    tweets = (
        session.query(models.Tweet)
        .filter(models.Tweet.username == request.username)
        .order_by(models.Tweet.last_edited_at.desc())
        .order_by(models.Tweet.posted_at.desc())
        .all()
    )
    return tweets


def create_tweet(request):
    tweet_new = models.Tweet(username=request.username, content=request.content,)
    for tag in request.tag:
        tweet_new.tags.append(models.Tag(tag=tag))
    session.add(tweet_new)
    session.commit()


def remove_tweet(request):
    tweet = session.query(models.Tweet).filter(models.Tweet.id == request.id).one()
    session.delete(tweet)
    session.commit()


def edit_tweet(request):
    tweet = session.query(models.Tweet).filter(models.Tweet.id == request.id).one()
    tweet.content = request.content
    tags_present = set([tag.tag for tag in tweet.tags])
    for tag in request.tag:
        if tag not in tags_present:
            tweet.tags.append(models.Tag(tag=tag))
    for tag in tweet.tags:
        if tag.tag not in request.tag:
            tweet.tags.remove(tag)
    session.add(tweet)
    session.commit()
