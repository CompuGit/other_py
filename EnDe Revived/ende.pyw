import tkinter as tk
from tkinter import filedialog
import json
import hashlib

config_file = open('./config.json','r')
config = json.load(config_file)

_VERSION = '1.1'

class Menubar:

	def __init__(self, parent):

		menubar = tk.Menu(parent.master, font = config['menubar']['font'])
		parent.master.config(menu = menubar)

		file_dropdown = tk.Menu(menubar, font = config['menubar']['font'], tearoff = 0, fg = config['menubar']['foreground'])

		file_dropdown.add_command(label = 'New File', command = parent.new_file, accelerator='Ctrl+N')
		file_dropdown.add_command(label = 'Open File', command = parent.open_file, accelerator='Ctrl+O')
		file_dropdown.add_command(label = 'Save File', command = parent.save_file, accelerator='Ctrl+S')
		file_dropdown.add_command(label = 'Save as', command = parent.save_file_as, accelerator='Ctrl+Shift+S')
		file_dropdown.add_separator()
		file_dropdown.add_command(label = 'Quit', command = parent.master.destroy)

		menubar.add_cascade(label = "File", menu = file_dropdown)


		EnDe_dropdown = tk.Menu(menubar, font = config['menubar']['font'], tearoff = 0, fg = config['menubar']['foreground'])
		EnDe_dropdown.add_command(label = 'Encrypt Content')
		EnDe_dropdown.add_command(label = 'Decrypt Content')
		menubar.add_cascade(label = "EnDe", menu = EnDe_dropdown)

		hash_dropdown = tk.Menu(menubar, font = config['menubar']['font'], tearoff = 0, fg = config['menubar']['foreground'])
		hash_dropdown.add_command(label = 'MD5 Hash Content', command = parent.md5)
		hash_dropdown.add_command(label = 'SHA1 Hash Content', command = parent.sha1)
		menubar.add_cascade(label = "Hash", menu = hash_dropdown)


class Statusbar:

	def __init__(self, parent):

		self.status = tk.StringVar()
		self.status.set(f'EnDe Editor - version {_VERSION} ')

		label = tk.Label(parent.textarea, textvariable = self.status, fg = config['statusbar']['foreground'], 
								bg = config['statusbar']['background'], anchor = 'sw', font = config['statusbar']['font'])
		
		label.pack(side = tk.BOTTOM, fill = tk.BOTH)

	def update_status(self, *args):
		if isinstance(args[0], bool):
			self.status.set('[*] File Updated Successfully.')
		else:
			self.status.set(f'EnDe Editor - version {_VERSION} ')

class EnDe:

	def __init__(self, master):
		
		master.title('Untitled - EnDe Editor')
		master.geometry(config['windowsize'])

		self.master = master
		self.filename = None

		self.textarea = tk.Text(master, font = config['textarea']['font'], fg = config['textarea']['foreground'])
		self.scroll = tk.Scrollbar(master, command = self.textarea.yview)
		self.textarea.configure(yscrollcommand = self.scroll.set)
		self.textarea.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
		self.scroll.pack(side = tk.RIGHT, fill = tk.Y)

		self.menubar = Menubar(self)
		self.statusbar = Statusbar(self)

		self.bind_shortcuts()

	def set_window_title(self, name = None):
		if name:
			self.master.title(name + ' - EnDe Editor')
		else:
			self.master.title('Untitled - EnDe Editor')
		

	def new_file(self, *args):
		self.textarea.delete(1.0, tk.END)
		self.filename = None
		self.set_window_title(self.filename)

	def open_file(self, *args):
		self.filename = filedialog.askopenfilename(defaultextension = '*.txt', filetypes = [('Text Files','*.txt'), ('ED Files','*.ed'), ('All FIles','*.*')])

		if self.filename:
			self.textarea.delete(1.0, tk.END)

			with open(self.filename, 'r') as f:
				self.textarea.insert(1.0, f.read())

			self.set_window_title(self.filename)


	def save_file(self, *args):
		if self.filename:
			
			try:
				textarea_content = self.textarea.get(1.0, tk.END)
				with open(self.filename,'w') as f:
					f.write(textarea_content)
				self.statusbar.update_status(True)

			except Exception as e:
				print(e)

		else:
			self.save_file_as()

	def save_file_as(self, *args):
		
		try:
			new_file = filedialog.asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = '*.txt', filetypes = [('Text Files','*.txt'), ('All FIles','*.*')])

			textarea_content = self.textarea.get(1.0, tk.END)
			with open(new_file,'w') as f:
				f.write(textarea_content)

			self.statusbar.update_status(True)
			self.filename = new_file
			self.set_window_title(self.filename)

		except Exception as e:
			print(e)

	def bind_shortcuts(self):
		self.textarea.bind('<Control-n>', self.new_file)
		self.textarea.bind('<Control-o>', self.open_file)
		self.textarea.bind('<Control-s>', self.save_file)
		self.textarea.bind('<Control-S>', self.save_file_as)
		self.textarea.bind('<Key>', self.statusbar.update_status)


	def md5(self):
		content = self.textarea.get(1.0, tk.END)
		content = hashlib.md5(content.encode())
		self.textarea.delete(1.0, tk.END)
		self.textarea.insert(1.0, content.hexdigest() )

	def sha1(self):
		content = self.textarea.get(1.0, tk.END)
		content = hashlib.sha1(content.encode())
		self.textarea.delete(1.0, tk.END)
		self.textarea.insert(1.0, content.hexdigest() )

if __name__ == '__main__':
	master = tk.Tk()
	ed = EnDe(master)
	master.mainloop()