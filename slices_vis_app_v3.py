# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:13:30 2020

@author: zz19101
"""

import pandas as pd
import numpy as np
import os
import random
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class slices_vis_app():
    
    """
    References:
        https://stackabuse.com/python-gui-development-with-tkinter/
        
    """
    
    def __init__(self, master):
        
        self.master = master
        self.width_value = master.winfo_screenwidth()
        self.height_value = master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (self.width_value,self.height_value))  # Set that the GUI takes up all the screen
        
        # Dimensions of the canvas where we'll place the images
        self.height_image = self.height_value/3.75 
        self.width_image = self.width_value/2
        self.directories = {}  # We store the filenames in a dictionary
        self.images_list = {}  # We store here the names of the images as a list in each folder
        self.image_id = 0
        
        # Buttons to select the files
        self.select_file_0 = Button(master, text = "First Scan", command = lambda: self.load_file(0)).grid(row = 1, column = 0, padx = 4, pady = 4)
        self.select_file_1 = Button(master, text = "Second Scan", command = lambda: self.load_file(1)).grid(row = 2, column = 0, padx = 4, pady = 4)
        self.select_file_2 = Button(master, text = "Third Scan", command = lambda: self.load_file(2)).grid(row = 3, column = 0, padx = 4, pady = 4)
        
        # Buttons to pass the current slice
        self.pass_back = Button(master, text = "←", command = self.previous_slice).grid(row = 5, column = 0, padx = 2, pady = 2)
        self.pass_forward = Button(master, text = "→", command = self.next_slice ).grid(row = 5, column = 2, padx = 2, pady = 2 )
        self.canvas_0 = Canvas(master, width=self.width_image, height=self.height_image, bg='white')
        self.canvas_1 = Canvas(master, width=self.width_image, height=self.height_image, bg='white')
        self.canvas_2 = Canvas(master, width=self.width_image, height=self.height_image, bg='white')
        
        # Display the slice number 
        self.text_slice = Text(master, height=1, width=5)
        self.text_slice.insert(END, self.image_id)
        self.text_slice.tag_configure("center", justify = 'center')
        self.text_slice.tag_add("center", 1.0, "end")
        self.text_slice.grid(row=0, column=1)
        self.label_slice = Label(master, text="Slice number: ").grid(row=0, column=0, padx = 2, pady = 2) 
        
        # Select Slice
        self.entry_slice = Entry(master)
        self.entry_slice.delete(0, END)
        self.entry_slice.grid(row=0, column=3)
        self.master.bind('<Return>', self.select_slice)
        self.label_select = Label(master, text="Select a slice: ").grid(row=0, column=2, padx = 2, pady = 2) 
        
        
    # Select folders
    def load_file(self,i):
        
        self.folder = filedialog.askdirectory()
        self.directories[i] = self.folder
        self.images_list[i] = os.listdir(self.directories[i])
        
        if i == 0:
            
            #print first image into the canvas
            self.image_filename_0 = os.path.join(self.directories[i], self.images_list[i][self.image_id])
            self.img_0 = ImageTk.PhotoImage(file = self.image_filename_0)  # This format works!
            self.canvas_0.create_image(0, 0, image=self.img_0, anchor='nw')
            self.canvas_0.grid(row = 1, column = 1)
            
        elif i == 1:
            #print second image into the canvas
            self.image_filename_1 = os.path.join(self.directories[i], self.images_list[i][self.image_id])
            self.img_1 = ImageTk.PhotoImage(file = self.image_filename_1)  # This format works!
            self.canvas_1.create_image(0, 0, image=self.img_1, anchor='nw')
            self.canvas_1.grid(row = 2, column = 1)
            
        elif i == 2:
            #print third image into the canvas
            self.image_filename_2 = os.path.join(self.directories[i], self.images_list[i][self.image_id])
            self.img_2 = ImageTk.PhotoImage(file = self.image_filename_2)
            self.canvas_2.create_image(0, 0, image=self.img_2, anchor='nw')
            self.canvas_2.grid(row = 3, column = 1)
            
            
    def previous_slice(self):
        
        self.image_id = self.image_id - 1
        nb_slices = len(self.images_list[0])
        
        if self.image_id < 0:
            self.image_id = nb_slices-1
            
        else:
            self.show_image(self.image_id)
        
        self.text_slice.delete(1.0, END)
        self.text_slice.insert(END, self.image_id)
        self.text_slice.config(state=NORMAL)
        self.text_slice.tag_configure("center", justify = 'center')
        self.text_slice.tag_add("center", 1.0, "end")
        self.show_image(self.image_id)
            
            
    def next_slice(self):
        
        self.image_id = self.image_id +1 
        nb_slices = len(self.images_list[0])
        
        if self.image_id > nb_slices-1:
            self.show_image(0)
            self.image_id = 0

        else:
            self.show_image(self.image_id)
            
        self.text_slice.delete(1.0, END)
        self.text_slice.insert(END, self.image_id)
        self.text_slice.config(state=NORMAL)
        self.text_slice.tag_configure("center", justify = 'center')
        self.text_slice.tag_add("center", 1.0, "end")
            
    def select_slice(self, event=None):
        self.i = self.entry_slice.get()
        self.show_image(int(self.i))
        self.image_id = int(self.i)
        self.text_slice.delete(1.0, END)
        self.text_slice.insert(END, self.image_id)
        self.text_slice.config(state=NORMAL)
        self.text_slice.tag_configure("center", justify = 'center')
        self.text_slice.tag_add("center", 1.0, "end")
        self.entry_slice.delete(0,END)
        
            
    def show_image(self, slice_nb):
        
         self.image_filename_0 = os.path.join(self.directories[0], self.images_list[0][slice_nb])
         self.img_0 = ImageTk.PhotoImage(file = self.image_filename_0)  # This format works!
         self.canvas_0.create_image(0, 0, image=self.img_0, anchor='nw')
         self.canvas_0.grid(row = 1, column = 1)
            
         self.image_filename_1 = os.path.join(self.directories[1], self.images_list[1][slice_nb])
         self.img_1 = ImageTk.PhotoImage(file = self.image_filename_1)  # This format works!
         self.canvas_1.create_image(0, 0, image=self.img_1, anchor='nw')
         self.canvas_1.grid(row = 2, column = 1)
    
         self.image_filename_2 = os.path.join(self.directories[2], self.images_list[2][slice_nb])
         self.img_2 = ImageTk.PhotoImage(file = self.image_filename_2)
         self.canvas_2.create_image(0, 0, image=self.img_2, anchor='nw')
         self.canvas_2.grid(row = 3, column = 1)
          
       
if __name__ == "__main__":
    root = Tk()
    root.title("Simultaneous Scans Visualization")
    slice_vis = slices_vis_app(root)
    root.mainloop()
    