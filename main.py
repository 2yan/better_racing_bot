#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:22:56 2021

@author: ryan
"""


import praw
import reddit_layer
import database

r = praw.Reddit('racing_bot')
        
        
subreddit = r.subreddit("iracing+karting+simracing+F1Game+formula1+granturismo+assettocorsa+forzahorizon")


posts = subreddit.stream.submissions(pause_after=-1, skip_existing=False)
cmts = subreddit.stream.comments(pause_after=-1, skip_existing=False)




p = reddit_layer.check_posts(posts)
c = reddit_layer.check_comments(cmts)

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
        print('commenting')
        
        retort = database.sample_retort(kind)
        print(retort)

        retort  = retort + base_text.replace(' ',  ' ^^')
    
        thing.reply(retort)
        database.record_response(thing.id, reddit_type)
    


    

    
while True:
    p = reddit_layer.check_posts(posts)
    c = reddit_layer.check_comments(cmts)
    

    for post, kind in p:
        response_function(post, kind, 'submission')

    for comment, kind in c:
        response_function(comment, kind, 'comment')
        
