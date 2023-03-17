import tkinter as tk
from tkinter import filedialog
import json
import hashlib, rsa

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
		EnDe_dropdown.add_command(label = 'Generate Keys', command = parent.rsa_key_gen)
		EnDe_dropdown.add_command(label = 'Encrypt Content', command = parent.rsa_encrypt)
		EnDe_dropdown.add_command(label = 'Decrypt Content', command = parent.rsa_decrypt)
		menubar.add_cascade(label = "RSA", menu = EnDe_dropdown)

		hash_dropdown = tk.Menu(menubar, font = config['menubar']['font'], tearoff = 0, fg = config['menubar']['foreground'])
		hash_dropdown.add_command(label = 'MD5 Hash Content', command = parent.md5)
		hash_dropdown.add_command(label = 'SHA1 Hash Content', command = parent.sha1)
		hash_dropdown.add_command(label = 'SHA256 Hash Content', command = parent.sha256)
		menubar.add_cascade(label = "Hash", menu = hash_dropdown)


class Statusbar:

	def __init__(self, parent):

		self.status = tk.StringVar()
		self.status.set(f'EnDe Editor - version {_VERSION} ')

		label = tk.Label(parent.textarea, textvariable = self.status, fg = config['statusbar']['foreground'], 
								bg = config['statusbar']['background'], anchor = 'sw', font = config['statusbar']['font'])
		
		label.pack(side = tk.BOTTOM, fill = tk.BOTH)

	def update_status(self, msg, *args):
		if isinstance(args[0], bool):
			self.status.set(f'[*] {msg}')
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
		self.filename = filedialog.askopenfilename(defaultextension = '*.ed', filetypes = [('EnDe Files','*.ed'), ('Text Files','*.txt'), ('All FIles','*.*')])

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
				self.statusbar.update_status('File Saved Successfully.',True)

			except Exception as e:
				print(e)

		else:
			self.save_file_as()

	def save_file_as(self, *args):
		
		try:
			new_file = filedialog.asksaveasfilename(initialfile = 'Untitled.ed', defaultextension = '*.txt', filetypes = [ ('EnDe Files','*.ed'), ('Text Files','*.txt'), ('All FIles','*.*')])

			textarea_content = self.textarea.get(1.0, tk.END)
			with open(new_file,'w') as f:
				f.write(textarea_content)

			self.statusbar.update_status('File Saved Successfully.',True)
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
	
	def sha256(self):
		content = self.textarea.get(1.0, tk.END)
		content = hashlib.sha256(content.encode())
		self.textarea.delete(1.0, tk.END)
		self.textarea.insert(1.0, content.hexdigest() )



	def rsa_key_gen(self):
		pubkey, privkey = rsa.newkeys(1024)

		pubkey = pubkey.save_pkcs1().decode('utf-8')
		privkey = privkey.save_pkcs1().decode('utf-8')

		pub_file = filedialog.asksaveasfilename(initialfile = 'pub_key.pem', defaultextension = '*.txt', filetypes = [('PEM File','*.pem')])
		open(pub_file,'wb').write(bytes(pubkey,'utf-8'))
		
		priv_file = filedialog.asksaveasfilename(initialfile = 'priv_key.pem', defaultextension = '*.txt', filetypes = [('PEM File','*.pem')])
		open(priv_file,'wb').write(bytes(privkey,'utf-8'))

		self.statusbar.update_status('Keys Generated Successfully.',True)

	
	def rsa_encrypt(self):
		content = self.textarea.get(1.0, tk.END)

		try:
			pub_file = filedialog.askopenfilename(initialfile = 'pub_key.pem', defaultextension = '*.pem', filetypes = [('PEM file','*.pem')])
			pub_key = open(pub_file,'rb').read()
			pub_key = rsa.PublicKey.load_pkcs1(pub_key)

			encrypted = rsa.encrypt(bytes(content, 'utf-8'), pub_key)

			self.textarea.delete(1.0, tk.END)
			self.textarea.insert(1.0, encrypted.hex())

			msg = 'Encrypted Successfully.'
		
		except:
			msg = 'Error in Encryption'

		self.statusbar.update_status(msg,True)



	def rsa_decrypt(self):
		encrypted = self.textarea.get(1.0, tk.END)
		try:
			priv_file = filedialog.askopenfilename(initialfile = 'priv_key.pem', defaultextension = '*.pem', filetypes = [('PEM file','*.pem')])
			priv_key = open(priv_file,'rb').read()
			priv_key = rsa.PrivateKey.load_pkcs1(priv_key)

			decrypted = rsa.decrypt(bytes.fromhex(encrypted), priv_key)
			self.textarea.delete(1.0, tk.END)
			self.textarea.insert(1.0, str(decrypted,' utf-8')[:-1])

			msg = 'Decrypted Successfully.'

		except:
			msg = 'Error in decryption'
		
		

		self.statusbar.update_status(msg,True)



if __name__ == '__main__':
	master = tk.Tk()
	ed = EnDe(master)
	master.mainloop()