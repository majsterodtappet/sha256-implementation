from tkinter import *
from tkinter import ttk
import tkinter as tk
import hashlib

hash_types = ('sha256', 'sha224', 'sha512')
#hash_types = ('sha512', 'md4', 'sha384', 'sha3_384', 'sha512_256', 'whirlpool', 'md5-sha1', 'ripemd160', 'shake_128', 'sha512_224', 'sha256', 'sha3_224', 'blake2b', 'mdc2', 'blake2s', 'sm3', 'md5', 'sha3_512', 'sha224', 'shake_256', 'sha1', 'sha3_256') #all available hashes in hashlib

root = Tk()
root.title('Encryption')
root.resizable(False,False)
root.geometry("750x230")
root.iconbitmap("lock.ico")

root.frame_header = ttk.Frame()

ttk.Label(root.frame_header, text = f'Choose hash:', style = 'Header.TLabel').grid(row = 1, column = 0, sticky=W)
ttk.Label(root.frame_header, text = 'Input:', style = 'Header.TLabel').grid(row = 3, column = 0, sticky=W)
ttk.Label(root.frame_header, text='Hash Value:',style='Header.TLabel').grid(row=4, column=0, sticky=W)
ttk.Label(root.frame_header, text='Hexadecimal:',style='Header.TLabel').grid(row=5, column=0, sticky=W)
ttk.Label(root.frame_header, text='Digest Size:',style='Header.TLabel').grid(row=6, column=0, sticky=W)
ttk.Label(root.frame_header, text='Block Size:',style='Header.TLabel').grid(row=7, column=0, sticky=W)

ttk.Label(root.frame_header, text='‎',style='Header.TLabel').grid(row=9,column=1)
ttk.Label(root.frame_header, text='‎',style='Header.TLabel').grid(row=0,column=1)
ttk.Label(root.frame_header, text='‎',style='Header.TLabel').grid(row=2,column=1)

options = tk.StringVar()
options.trace_add('write', lambda *args: options.get())
OptionMenu(root.frame_header, options, *hash_types).grid(row=1, column=1, sticky=W)

text_entry = ttk.Entry(root.frame_header, width=100)
text_entry.grid(row=3,column=1)
hex_output = ttk.Entry(root.frame_header, width=100)
hex_output.grid(row=5, column=1, sticky=W)
digest_output = ttk.Entry(root.frame_header, width=10)
digest_output.grid(row=6, column=1, sticky=W)
block_output = ttk.Entry(root.frame_header, width=10)
block_output.grid(row=7, column=1, sticky=W)
enc_dec_text = ttk.Entry(root.frame_header, width=100)
enc_dec_text.grid(row=4,column=1)

def encrypt_text():

    enc_dec_text.delete(0, END)
    hex_output.delete(0, END)
    digest_output.delete(0, END)
    block_output.delete(0, END)

    hash_type = options.get()

    stringtoencrypt = text_entry.get()
    encoded = stringtoencrypt.encode()

    if hash_type == 'sha256':
     result = hashlib.sha256(encoded)
    elif hash_type == 'sha512':
     result = hashlib.sha512(encoded)
    elif hash_type == 'sha224':
     result = hashlib.sha224(encoded)

    enc_dec_text.insert(0, result)
    hex_output.insert(0, result.hexdigest())
    digest_output.insert(0, result.digest_size)
    block_output.insert(0, result.block_size)

def clear_text():
    
    text_entry.delete(0, END)
    enc_dec_text.delete(0, END)
    hex_output.delete(0, END)
    digest_output.delete(0, END)
    block_output.delete(0, END)

encrypt_button = ttk.Button(root.frame_header, text='Encrypt',command = lambda: encrypt_text()).grid(row=10,column=1, sticky =W)
clear_button = ttk.Button(root.frame_header,text='Clear all',command = lambda: clear_text()).grid(row=10,column=1, sticky=E)

root.frame_header.pack()
root.mainloop() 
