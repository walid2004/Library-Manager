#tabish.fayaz@stud.th-deg.de
#omar.nasr@stud.th-deg.de
#waled.mahaya@stud.th-deg.de

### View.py is he main entry point to our program ###
### This Program needs config_manager.json file to run. ####
import json
import random
import string

data=[]
def opener(file_name):
    with open (file_name, 'r+') as f:
        ff= json.load(f)
    return ff

def file_name_fetcher():
    with  open('config_manager.json', 'r') as f:
        bruh = json.load(f)['current']
        print(bruh)
        return bruh

result=[]



def search(title='', author='',year='',statuses=[]):
    global result
    result.clear()
    for item in opener(file_name_fetcher()):
        if (title in item['title'] and author in item['author'] and year in str(item['year']) and item['status'] in statuses):
            print(f"Title: {item['title']}, Author: {item['author']}, Year: {item['year']}, Status: {item['status']}")
            result.append(item)

def commiter(file_name):
    if not file_name:
        file_name='./lib_default.json'
    try:
        with open (file_name, 'w') as f:
            json.dump(data,f, indent=4)
    except FileNotFoundError:
        with open (file_name, 'x') as f:
            json.dump([],f, indent=4)

def edit(index,title, author, year, status):
    global data
    data = opener(file_name_fetcher())
    data[index]['title'] = title
    data[index]['author'] = author
    data[index]['year'] = year
    data[index]['status'] = status
    commiter(file_name=file_name_fetcher())

def delete(index):
    global data
    data = opener(file_name_fetcher())
    data[index]['status']='deleted'
    commiter(file_name=file_name_fetcher())

def add(title, author, year, status):
    global data
    data = opener(file_name_fetcher())
    data.append({'title': title, 'author': author, 'year':year, 'status':status})
    commiter(file_name=file_name_fetcher())

def randomlog(starting_point, ending_point):
    with open('config_manager.json', 'r') as f:
        config = json.load(f)
        config[file_name_fetcher()]=[starting_point, ending_point]
    with open('config_manager.json', 'w') as m:
        json.dump(config, m, indent=4)
randomlog(0,0)

def randomizer():
    global data
    data = opener(file_name_fetcher())
    starting_point = len(data)
    ending_ppoint = starting_point+100
    randomlog(starting_point, ending_ppoint)
    
    for i in range(1000000):
        st=''.join(random.choices(string.ascii_letters, k=4))
        it = random.randint(1600,2025)
        ss = random.choice(['available', 'deleted','lent out', 'missing'])
        data.append({'title': st, 'author': st, 'year': it, 'status': ss})
        print(st)
    commiter(file_name=file_name_fetcher())

def randomdeleter():
    with open('config_manager.json', 'r') as f:
        all = json.load(f)
        wanted = all[file_name_fetcher()]
        all.pop(file_name_fetcher())
        with open(file_name_fetcher(), 'r')as z:
            bruh=json.load(z)
            del bruh[wanted[0]:wanted[1]]
            with open(file_name_fetcher(), 'w')as m:
                json.dump(bruh, m, indent=4)
        with open('config_manager.json', 'w') as f:
            json.dump(all, f, indent=4)

