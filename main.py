from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog
from multi import Multi
import asyncio
import threading
import dir
from tkinter.messagebox import showinfo
import os
import time
import scrap
import tools
#gui sucks on linux, need update


def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)

class App(Tk):
	


	def __init__(self):
		Tk.__init__(self)
		app_width = 460
		app_height = 480
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()
		x = int((screen_width / 2) - (app_width / 2))
		y = int((screen_height / 2) - (app_height / 2))
		self.geometry(f'{app_width}x{app_height}+{x}+{y}')
		self.title("Manga Downloader")
		if sys.platform == 'win32':
			self.iconbitmap(resource_path("md.ico"))
		self.resizable(False, False)

		self.input_thread = None
		self.admin = 0
		self.admin_mode = False
		self._thread, self._pause, self._stop = None, False, True

		self.labelPath = Label(self, text="path:")
		self.labelPath.place(x=10,y=10)

		self.path = StringVar()
		self.pathEntered = Entry(self, width = 50, textvariable = self.path, highlightthickness=1)
		self.pathEntered.config(highlightbackground = "black")
		self.pathEntered.place(x=50,y=10)

		self.browse_button = ttk.Button(self, text="Browse", width = 10, command=self.browse_button)
		self.browse_button.place(x=356,y=8)

		self.toplabel = Label(self, text="", fg="red")  
		self.toplabel.place(x=50,y=31)

		self.labelCode = Label(self, text="url:")
		self.labelCode.place(x=10,y=60)

		self.code = StringVar()
		self.codeEntered = Entry(self, width = 50, textvariable = self.code, highlightthickness=1)
		self.codeEntered.config(highlightbackground = "black")
		self.codeEntered.place(x=50,y=60)

		self.myButton = ttk.Button(self, text="Download", width = 15, command=self.download)
		self.myButton.place(x=170,y=150)

		self.text = scrolledtext.ScrolledText(self, height=15, width=49)
		self.text.place(x=30,y=200)
		self.text.tag_configure("green", foreground="green")
		self.text.tag_configure("red", foreground="red")
		self.text.configure(state='disabled')

		self.stopButton = ttk.Button(self, text="About", width = 15, command=self.about)
		self.stopButton.place(x=170,y=450)

		

		
	def downloading(self):
		# BEGIN
		self.testpath()
		self.testcode()
		
		if self.path_validity and self.code_validity:
		    multi = Multi(self.text)
		    try:
			    t = time.perf_counter()
			    test = multi.download_manga(self.code.get(), self.path.get())
			    t2 = time.perf_counter() - t
			    if test != "":
			    	self.write_in_widget(f"\n\n\nDownload complete UwU\nElapsed time: {t2:0.2f} seconds\n\n", "green")
		    except:
		    	self.write_in_widget("\n\nAn error occurred while processing your request  (-_-)\n\n", "red")

		    self.text.configure(state='disabled')
	    # END
		if self._thread is not None:
		    self._thread, self._pause, self._stop = None, False, True
		self.myButton.configure(text="Download", command=self.download)
		self.myButton["state"] = "normal"

	def download(self):
	    if self._thread is None:
	    	self._stop = False
	    	self._thread = threading.Thread(target=self.downloading)
	    	self._thread.start()
	    self.myButton["state"] = "disable"
	    self.myButton.configure(text="Downloading...")

	def browse_button(self):
		filename = filedialog.askdirectory()
		self.path.set(filename)

	def testpath(self):
		self.path_validity = False
		
		if dir.is_pathname_valid(self.path.get()):
		    self.path_validity = True
		    self.toplabel.config(text="")
		    self.pathEntered.config(highlightbackground = "black")
		else:
			self.pathEntered.config(highlightbackground = "red")
			self.toplabel.config(text="invalid path")

	def testcode(self):
		self.code_validity = False
		try:
			# int(self.code.get())
			self.code_validity = True
			self.codeEntered.config(highlightbackground = "black")
		except ValueError:
			self.codeEntered.config(highlightbackground = "red")


	def write_in_widget(self, str, color):
		self.text.configure(state='normal')
		self.text.insert(END, str, (color,))
		self.text.configure(state='disabled')
		self.text.see("end")

	def clear(self):
		self.text.configure(state='normal')
		self.text.delete('1.0', END)
		self.text.see("end")




	def about(self):
		showinfo("About", "Manga Downloader v1\nCreated by Yūki\n\nPlease report bug to me XD")
		
            


App().mainloop()
