
from datetime import datetime
import sqlite3
from random import sample


con = sqlite3.connect('commented.db')
def create_table():
    cur = con.cursor()
    
    # Create table
    cur.execute('''CREATE TABLE IF NOT EXISTS responses
                   (submission_id text, kind text, date date)''')
    
    # Save (commit) the changes
    con.commit()
    cur.close()

def record_response(submission_id, kind):
    cur = con.cursor()
    now = datetime.now()
    cur.execute(f"INSERT INTO responses VALUES ('{submission_id}','{kind}', '{now}')")
    con.commit()
    cur.close()
    
def check_if_responded(submission_id, kind):
    cur = con.cursor()
    for row in cur.execute('SELECT * FROM responses where submission_id =? and kind=?', (submission_id, kind)):
        return True
    cur.close()
    return False

def get_retorts():
    with open('retorts.txt') as f:
        data = f.read()
        
    result = {}
    
    key = ''
    for line in data.split('\n'):
        line = line.strip()
        if line != '':
            if '[' in line:
                key = line.replace('[','').replace(']', '')
                result[key] = []
            else:
    
                result[key].append(line)
    return result


def sample_retort(tag):
    assert tag in ['gap', 'rubbing']
    x = get_retorts()
    x = x[tag]
    return sample(x, 1)[0]