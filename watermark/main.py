from tkinter import *
from PIL import Image , ImageTk , ImageDraw, ImageFilter
from tkinter import filedialog as fd

#---------------------------------------------------------
window_size = 1200
COLORS = ['#F9D371','#F47340','#EF2F88','#8843F2']
TEXT = ['Add Photo','Add ']
#---------------------------------------------------------

class Watermark():
    def __init__(self):
        self.window=Tk()
        self.window.title('Watermark App')
        self.window.config(padx=50,pady=50 ,width = window_size/2 ,height= (window_size)/3 + 100,bg=COLORS[0])

        #---------------------------------------------------
        self.canvas = Canvas(width=window_size/2,height=(window_size)/3,bg='white' )
        self.photo = self.canvas.create_image(window_size/4,window_size/6)
        self.canvas.config( highlightthickness=0)
        self.canvas.grid(row=0, column=0,columnspan=4)
        self.img=''

        picture = PhotoImage(file="4855034.png")
        img_save = PhotoImage(file="2874091.png")
        img_text= PhotoImage(file="167502.png")
        img_reset = PhotoImage(file="25051.png")
        self.pic_button = Button(width=window_size/8+50,height=110,image=picture,highlightthickness=0 , command=self.search_image, bg=COLORS[3])
        self.pic_button.grid(row=1, column=0 , pady=10)
        #self.pic_button = Button(width=window_size/8,height=110,image=img_text,highlightthickness=0, bg=COLORS[3])
        #self.pic_button.grid(row=1, column=1 , pady=10)
        self.pic_button = Button(width=window_size/8+50,height=110,image=img_save,highlightthickness=0, command=self.save_file, bg=COLORS[3])
        self.pic_button.grid(row=1, column=2 , pady=10)
        self.pic_button = Button(width=window_size/8+50,height=110,image=img_reset,highlightthickness=0, command=self.mark, bg=COLORS[3])
        self.pic_button.grid(row=1, column=1 , pady=10)
        self.canvas.itemconfig(self.photo,image=picture)

        #self.fill_text = Entry(text="", width=100 )
        #self.fill_text.grid(row=2, column=0,columnspan=4 )

        self.mainloop()

    def search_image(self):
        file = fd.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg *.gif")])
        img = Image.open(file)
        img = img.resize((int(window_size/2),int(window_size/3)), Image.ANTIALIAS)
        img.save('sample.png')
        img = ImageTk.PhotoImage(img)
        self.canvas.itemconfig(self.photo, image=img)
        self.canvas.image = img
        return self.img

    def save_file(self):

        img1=Image.open('sample.png')
        img2=Image.open('sample2.png')
        png_info1 = img2.info
        img1.paste(img2, (int(window_size/3),int(window_size/4.5)), **png_info1)
        png_info = img1.info
        img1.save("my_image.png", **png_info)

        #filename = "my_image.eps"
        #self.canvas.postscript(file=filename)
        #save_img = Image.open(filename)
        #save_img.save("my_image.png", "png")

    def mark(self):
        file = fd.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg *.gif")])
        mark = Image.open(file)
        mark.putalpha(80)
        mark = mark.resize((int(window_size/6),int(window_size/9)))
        mark.save('sample2.png')
        mark = ImageTk.PhotoImage(mark)
        self.canvas.image_names = mark
        self.canvas.create_image(int(window_size/2.4),int(window_size/3.6),image=mark)

    def mainloop(self):
        self.window.mainloop()

Watermark()