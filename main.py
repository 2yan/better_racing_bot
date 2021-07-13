#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:22:56 2021

@author: ryan
"""


import praw
import reddit_layer
import database
from datetime import datetime
import sys
import time


def load_reddit():
    sleep_time = 1
    done  = False
    while not done:
        try:
            r = praw.Reddit('racing_bot')
            subreddit = r.subreddit("velocityintegrated+iracing+motorsports+indycar+formulae+wec+wtcc+racing+startmotorsport+karting+simracing+F1Game+formula1+granturismo+assettocorsa+forzahorizon")


            cmts = subreddit.stream.comments(pause_after=-1, skip_existing=False)
            posts = subreddit.stream.submissions(pause_after=-1, skip_existing=False)
            done = True
        except Exception as e:
            time.sleep(sleep_time)
            sleep_time = sleep_time * 2
            sleep_time = min(sleep_time, 60)
            pass
    
    return cmts, posts

base_text = """
_____
 I'm a bot and I just detected a quote that is close to universally hated in the racing community. This response has been communally sourced from your fellow racing drivers.
 If you have other responses you want to add to my repository, PM your ideas and the mindless racing nerd, that codes me, will add it.
"""



def response_function(thing, kind,  reddit_type):
    assert reddit_type in ['submission', 'comment']
    assert kind in ['gap', 'rubbing']
    
    has_responded = database.check_if_responded(thing.id, reddit_type)
    
    if not has_responded:
        print('commenting ', datetime.today()) 
        retort = database.sample_retort(kind)

        retort  = retort + base_text.replace(' ',  ' ^^')
    
        thing.reply(retort)
        database.record_response(thing.id, reddit_type)
    


    
print('setting up')

cmts, posts = load_reddit()




while True:
    try:
        p = reddit_layer.check_posts(posts)
        for post, kind in p:
            response_function(post, kind, 'submission')

    except Exception as e:
        cmts, posts = load_reddit()
        print(e)
        pass
    try:
        c = reddit_layer.check_comments(cmts)
        for comment, kind in c:
            response_function(comment, kind, 'comment')
    
    except Exception as e:
        print(e)
        cmts, posts = load_reddit()
        pass
    
    
    print( datetime.today() , end = '\r')
    

