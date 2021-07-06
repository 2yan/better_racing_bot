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

r = praw.Reddit('racing_bot')
        
        
subreddit = r.subreddit("iracing+motorsports+indycar+formulae+wec+wtcc+racing+startmotorsport+karting+simracing+F1Game+formula1+granturismo+assettocorsa+forzahorizon")





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

while True:
    try:
        p = reddit_layer.check_posts(posts)
        for post, kind in p:
            response_function(post, kind, 'submission')

    except Exception as e:
        pass
    try:
        c = reddit_layer.check_comments(cmts)
        for comment, kind in c:
            response_function(comment, kind, 'comment')
         
    
    
    except Exception as e:
        pass
    
    
    print( datetime.today() , end = '\r')
    

