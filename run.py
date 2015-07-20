#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  run.py
#  
#  Copyright 2015 Ericson Willians (Rederick Deathwill) <EricsonWRP@ERICSONWRP-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 

import wikipedia
import traceback
import tkinter as tk
import sys

class App(tk.Frame):
	
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.config()
		self.grid()
		self.create_widgets()
		
	def config(self):
		self.master.title("Pykipedia Explorer")
		
	def create_widgets(self):
		top = self.winfo_toplevel() 
		top.rowconfigure(0, weight=1)
		top.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		self.search_label = tk.Label(self, text="Search: ")
		self.search_label.grid(row=0, column=0, sticky=tk.N+tk.SW)
		self.search_entry = tk.Entry(self)
		self.search_entry.grid(row=0, column=0, padx=60, sticky=tk.N+tk.SW)
		self.content_area = tk.Text(self, wrap=tk.WORD)
		self.content_area.grid(row=1, column=0, sticky=tk.SW+tk.E)
		self.content_scroll_bar = tk.Scrollbar(self, command=self.content_area.yview)
		self.content_scroll_bar.grid(row=1, column=1, sticky=tk.NW+tk.S+tk.W)
		self.content_area["yscrollcommand"] = self.content_scroll_bar.set
		def fetch_summary(): 
			try:
				self.content_area.delete("1.0", tk.END)
				self.content_area.insert(tk.INSERT, wikipedia.summary(self.search_entry.get()))
			except wikipedia.exceptions.DisambiguationError:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				self.content_area.insert(tk.INSERT, exc_obj)
		def fetch_page(): 
			try:
				self.content_area.delete("1.0", tk.END)
				self.content_area.insert(tk.INSERT, wikipedia.WikipediaPage(self.search_entry.get()).content.replace("Edit", ''))
			except wikipedia.exceptions.DisambiguationError:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				self.content_area.insert(tk.INSERT, exc_obj)
		def fetch_html(): 
			try:
				self.content_area.delete("1.0", tk.END)
				self.content_area.insert(tk.INSERT, wikipedia.WikipediaPage(self.search_entry.get()).html())
			except wikipedia.exceptions.DisambiguationError:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				self.content_area.insert(tk.INSERT, exc_obj)
		def fetch_images(): 
			try:
				self.content_area.delete("1.0", tk.END)
				[self.content_area.insert(tk.INSERT, image_link + '\n') for image_link in wikipedia.WikipediaPage(self.search_entry.get()).images]
			except wikipedia.exceptions.DisambiguationError:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				self.content_area.insert(tk.INSERT, exc_obj)
				
		self.fetch_summary_button = tk.Button(self, text="Fetch summary", command=fetch_summary)
		self.fetch_summary_button.grid(row=0, column=0, padx=232, sticky=tk.SW)
		self.fetch_page_button = tk.Button(self, text="Fetch page", command=fetch_page)
		self.fetch_page_button.grid(row=0, column=0, padx=352, sticky=tk.SW)
		self.fetch_html_button = tk.Button(self, text="Fetch HTML", command=fetch_html)
		self.fetch_html_button.grid(row=0, column=0, padx=446, sticky=tk.SW)
		self.fetch_images_button = tk.Button(self, text="Fetch images", command=fetch_images)
		self.fetch_images_button.grid(row=0, column=0, padx=546, sticky=tk.SW)
		self.quit_button = tk.Button(self, text="Quit", command=self.quit)
		self.quit_button.grid(row=2, column=0, sticky=tk.SW)

def main():
	
	app = App()
	app.mainloop()
		
	return 0

if __name__ == '__main__':
	main()
