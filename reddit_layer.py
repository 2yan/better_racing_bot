




checks = {'gap': ['if you no longer go for a gap', 'if you no longer go for the gap'],
          'rubbing': ['rubbin is racin', 'rubbing is racin'], 
          'nascar': ['NASCAR']
          }



def check_text(text):
    for key in checks.keys():
        inverse_check_list = inverse_checks.get(key, [])
        for inverse_text in inverse_check_list:
            if inverse_text in text.lower():
                return 'False'

        for check_phrase in checks[key]:
            if check_phrase in text.lower():
                return key

    return False




def get_tags(text):
    tags = []
    for key in checks.keys():
        for check_phrase in checks[key]:
            if check_phrase in text.lower():
                tags.append(key)
    return '+'.join(sorted(tags))



def check_posts(posts):
    to_respond = []

    
    for post in posts:
        if post is None:
            break
        
        if post.author.name != 'better_racing_bot':
            tags = get_tags(post.title)
            if len(tags) > 0:
                result = '+'.join(sorted(tags))
                to_respond.append([post, result])
        
        
    return to_respond

def check_comments(comments):
    to_respond= []

    for comment in comments:
        
        if comment is None:
            break
        
        if comment.author.name != 'better_racing_bot':
            tags = get_tags(post.title)
            if len(tags) > 0:
                result = '+'.join(sorted(tags))
                to_respond.append([comment, result])
        
        
    return to_respond
