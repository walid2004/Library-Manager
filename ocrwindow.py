#tabish.fayaz@stud.th-deg.de
#omar.nasr@stud.th-deg.de
#waled.mahaya@stud.th-deg.de

### View.py is he main entry point to our program ###
### This Program needs config_manager.json file to run. ####

import tkinter as tk
from PIL import Image, ImageTk
import pyocr
import pyocr.builders
import json
datawithin={'ocr':'none'}
finaltext = ''
opened = False
class ImageDrawer:
    def __init__(self, root, image_path):
        global opened
        opened = True
        global finaltext
        self.root = root
        self.image_path = image_path
        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack()
        
        self.image = Image.open(image_path)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
        self.canvas.image = self.image_tk 
        
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.rect_id = None
        
        self.label = tk.Label(root, text="Dimensions: Width x Height", font=("Helvetica", 12))
        self.label.pack(pady=10)
        self.text_label = tk.Label(root, text="Recognized Text: ", font=("Helvetica", 12))
        self.text_label.pack(pady=10)
        self.ok = tk.Button(root, text="Ok", font=("Helvetica", 12), command=lambda: root.destroy())
        self.ok.pack(pady=10)
        
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            raise Exception("No OCR tool found")
        self.tool = tools[0]
        
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
    
    def on_button_press(self, event):
        if self.rect_id:
            self.canvas.delete(self.rect_id)
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red", width=2)
        self.rect_id = self.rect

    def on_mouse_drag(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)
        width = abs(event.x - self.start_x)
        height = abs(event.y - self.start_y)
        self.label.config(text=f"Dimensions: {width} x {height}")
        
    def on_button_release(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)
        width = abs(event.x - self.start_x)
        height = abs(event.y - self.start_y)
        self.label.config(text=f"Dimensions: {width} x {height}")
        self.recognize_text_in_rectangle(self.start_x, self.start_y, event.x, event.y)
        
    def recognize_text_in_rectangle(self, x1, y1, x2, y2):
        cropped_image = self.image.crop((x1, y1, x2, y2))
        recognized_text = self.tool.image_to_string(cropped_image, lang='eng', builder=pyocr.builders.TextBuilder())
        self.text_label.config(text=f"Recognized Text: {recognized_text.strip()}")
        global finaltext
        global opened
        finaltext = recognized_text
        with open ('config_manager.json') as f:
            global datawithin
            datawithin = json.load(f)
            datawithin['ocr']=finaltext
        with open('config_manager.json','w')as m:
            json.dump(datawithin,m)
            
    




def finalboss(image_path, master):
    window = tk.Toplevel(master)
    window.title("Draw Rectangle on Image with OCR (pyocr)")
    app = ImageDrawer(window, image_path)


