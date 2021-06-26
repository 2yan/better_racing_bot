




checks = {'gap': ['if you no longer go for a gap', 'if you no longer go for the gap'],
          'rubbing': ['rubbin is racin', 'rubbing is racin'], 
}



def check_text(text):
    for key in checks.keys():
        for check_phrase in checks[key]:
            if check_phrase in text.lower():
                return key

    return False



def check_posts(posts):
    to_respond = []

    
    for post in posts:
        if post is None:
            break
        
        if post.author.name != 'better_racing_bot':
            result = check_text(post.title)
            if result:
                to_respond.append([post, result])
        
        
    return to_respond

def check_comments(comments):
    to_respond= []

    for comment in comments:
        
        if comment is None:
            break
        
        if comment.author.name != 'better_racing_bot':
            result = check_text(comment.body)
            if result:
                to_respond.append([comment, result])
        
        
    return to_respond