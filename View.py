#Waled.mahaya@stud.th-deg.de
#tabish.fayaz@stud.th-deg.de
### This Program needs config_manager.json file to run. ####

from tkinter import *
import M
import C
import threading


root = Tk()
scrollbar = Scrollbar(root)
scrollbar.grid( row=2,column=2 , sticky='ns')

mylist = Listbox(root, yscrollcommand = scrollbar.set , width=200)

form = Frame(root)
titleBar = Entry(form, width=60)
titleBar.grid(row=50,column=1)
authorBar = Entry(form, width=60)
authorBar.grid(row=51,column=1)
yearBar = Entry(form, width=60)
yearBar.grid(row=52,column=1)
statusvar = StringVar(form, value='available')
Label(form, text='Status:').grid(row=49, column=2)
R1 = Radiobutton(form, text="available", variable=statusvar, value="available")
R1.grid(row=49, column=3)
R2 = Radiobutton(form, text="deleted", variable=statusvar, value="deleted")
R2.grid(row=50, column=3)
R3 = Radiobutton(form, text="missing", variable=statusvar, value="missing")
R3.grid(row=51, column=3)
R4 = Radiobutton(form, text="lent out", variable=statusvar, value="lent out")
R4.grid(row=52, column=3)


Label(form, text='Title:').grid(row=50, column=0)
Label(form, text='Author:').grid(row=51, column=0)
Label(form, text='Year:').grid(row=52, column=0)

def inserter():
    titleBar.delete(0,END)
    authorBar.delete(0,END)
    yearBar.delete(0,END)
    try:
        titleBar.insert(0,mylist.get(mylist.index(ANCHOR)).split('/')[0])
        authorBar.insert(0,mylist.get(mylist.index(ANCHOR)).split('/')[1])
        yearBar.insert(0,mylist.get(mylist.index(ANCHOR)).split('/')[2])
        statusvar.set(mylist.get(mylist.index(ANCHOR)).split('/')[3])
    except IndexError:
        print('No item selected')


def openstatusdialog():
    dialog = Toplevel()
    dialog.title("Status")
    Label(dialog, text="Change Status:").grid(row=30, column=30)

    Radiobutton(dialog, text="available", variable=statusvar, value="available").grid(row=30, column=35)
    Radiobutton(dialog, text="deleted", variable=statusvar, value="deleted").grid(row=30, column=36)
    Radiobutton(dialog, text="lent out", variable=statusvar, value="lent out").grid(row=30, column=38)
    Radiobutton(dialog, text="missing", variable=statusvar, value="missing").grid(row=30, column=37)

    Button(dialog, text="Confirm", command=lambda: (C.editor(file_name=C.file_name_fetcher(),index=mylist.index(ANCHOR),title=titleBar.get(), author=authorBar.get(),year=yearBar.get(), status=statusvar.get()),update(C.file_name_fetcher()), dialog.destroy())).grid(row=31, column=36)

mylist.bind("<<ListboxSelect>>", lambda event: inserter())
mylist.bind("<Double-Button-1>", lambda event: (openstatusdialog(), ))


Button(form, text='Open Search', command = lambda: (searchformopener())).grid(row=53,column=0)
Button(form, text='Add Book', command = lambda : (C.adder(file_name=C.file_name_fetcher(),title=titleBar.get(), author=authorBar.get(),year=yearBar.get(), status=statusvar.get()),update(C.file_name_fetcher()))).grid(row=53,column=1)
Button(form, text='Edit Book', command = lambda : (C.editor(file_name=C.file_name_fetcher(),index=mylist.index(ANCHOR),title=titleBar.get(), author=authorBar.get(),year=yearBar.get(), status=statusvar.get()),update(C.file_name_fetcher()))).grid(row=53,column=2)
Button(form, text='Delete Book', command = lambda:(C.deleter(file_name=C.file_name_fetcher(),index=mylist.index(ANCHOR)),update(C.file_name_fetcher()))).grid(row=53,column=3)

changeform = Frame(root)
def cahngeformviewer():
    changeform.grid(row=0, column=1)
def cahngeformhider():
    changeform.grid_forget()
Label(changeform, text='Enter file name to be opened/Created:').grid(row=0, column=0)
bih=Entry(changeform)
bih.grid(row=0, column=1)
Button(changeform, text='Change', command= lambda : (C.filehandler(bih.get()),C.file_name_updater(bih.get()),update(C.file_name_fetcher()))).grid(row=0, column=2)
print(bih.get())
print(C.file_name_fetcher())
Button(changeform, text='Cancel', command= lambda :cahngeformhider()).grid(row=0, column=3)




mainmenu = Menu(root)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Change Library', command = lambda : cahngeformviewer())
filemenu.add_command(label='Random Generation', command = lambda : (threading.Thread(target=M.randomizer).start(), searchupdate()))
filemenu.add_command(label='Cancel Generation', command = lambda : (M.randomdeleter() ,update(C.file_name_fetcher())))

mainmenu.add_cascade(label='Library', menu= filemenu)
root.config(menu=mainmenu)

form.grid(row=4, column=1)

def deleter():
   mylist.delete(0, END)

def counterr():
    counter = Label(root,text = len(M.opener(C.file_name_fetcher())))
    counter.grid_forget()
    counter.grid(row=900,column=1)

def update(file_name=C.file_name_fetcher()):#################################################problems#######################################################
    deleter()
    counterr()
    for book in C.filehandler(file_name):
        mylist.insert(END, f'{book['title']}/{book["author"]}/{book["year"]}/{book['status']}')
update()

def searchupdate():

    for book in M.result:
        searchresults.insert(END, f'{book['title']}/{book["author"]}/{book["year"]}/{book['status']}')


searchform = Frame(root)
searchresults = Listbox(searchform, yscrollcommand = scrollbar.set , width=140)
searchresults.grid(row=2,column=2)
Button(searchform, text= 'Cancel', command = lambda : searchformcloser()).grid(row=100, column=3)
Button(searchform, text= 'Search', command = lambda : (M.search(title=searchtitle.get(), author=searchauthor.get(), year=searchyear.get(), statuses=get_selected_statuses()), searchresults.delete(0, END),searchupdate())).grid(row=100, column=2)
searchresults.bind("<Double-Button-1>", lambda event: (openstatusdialog(), ))


searchtitle = Entry(searchform, width=60)
searchtitle.grid(row=50,column=2)
searchauthor = Entry(searchform, width=60)
searchauthor.grid(row=51,column=2)
searchyear = Entry(searchform, width=60)
searchyear.grid(row=52,column=2)
statusvar = StringVar(searchform, value='available')
Label(searchform, text='Status:').grid(row=49, column=0)
statusvar1 = StringVar(value="available")
statusvar2 = StringVar(value="deleted")
statusvar3 = StringVar(value="missing")
statusvar4 = StringVar(value="lent out")

# Checkbuttons using individual variables
C1 = Checkbutton(searchform, text="available", variable=statusvar1, onvalue="available", offvalue="")
C1.grid(row=49, column=1)

C2 = Checkbutton(searchform, text="deleted", variable=statusvar2, onvalue="deleted", offvalue="")
C2.grid(row=50, column=1)

C3 = Checkbutton(searchform, text="missing", variable=statusvar3, onvalue="missing", offvalue="")
C3.grid(row=51, column=1)

C4 = Checkbutton(searchform, text="lent out", variable=statusvar4, onvalue="lent out", offvalue="")
C4.grid(row=52, column=1)

Label(searchform, text='Title:').grid(row=50, column=3)
Label(searchform, text='Author:').grid(row=51, column=3)
Label(searchform, text='Year:').grid(row=52, column=3)

# Function to append selected checkboxes to a list
def get_selected_statuses():
    selected_statuses = []
    for var in [statusvar1, statusvar2, statusvar3, statusvar4]:
        if var.get():  # If the variable is not empty (checkbox is selected)
            selected_statuses.append(var.get())
    print(selected_statuses)  # Replace with your logic
    return selected_statuses




Label(form, text='Title').grid(row=50, column=0)
Label(form, text='Author').grid(row=51, column=0)
Label(form, text='Year').grid(row=52, column=0)




def searchformopener():
    searchform.grid(row=6, column=1)
    
    
def searchformcloser():
    searchform.grid_forget()



mylist.grid( column=1,row=2)
scrollbar.config(command = mylist.yview )



mainloop()