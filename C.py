import M
import json

def file_name_fetcher():
    with  open('config_manager.json', 'r') as f:
        bruh = json.load(f)['current']
        print(bruh)
        return bruh

file_name_fetcher()

def file_name_updater(new_file_name):
    with open('config_manager.json', 'w') as f:
        json.dump({'current': new_file_name}, f, indent=4)
    return new_file_name

def filehandler(file_name):
    if file_name==None or file_name=='':
        file_name='./lib_default.json'
        file_name_updater(file_name)

    try:
        M.opener(file_name)
        return M.opener(file_name)
    except FileNotFoundError:
        with open (file_name, 'x') as f:
            data= [{'title': 'Title', 'author':'Author', 'year': 'Year', 'status': 'Status'}]
            json.dump(data, f)
        return data


def adder(title, author, year, status, file_name=file_name_fetcher()):
    M.add(title=title, author=author, year=year, status=status)


def editor(index, title, author, year, status, file_name=file_name_fetcher()):
    M.edit(index=index, title=title, author=author, year=year, status=status)
    print(title, author, year, status)


def deleter( index, file_name=file_name_fetcher()):
    M.delete(index=index)

