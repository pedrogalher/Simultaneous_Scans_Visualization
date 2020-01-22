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

class slices_vis_app():
    
    def __init__(self, master):
        self.width_value = master.winfo_screenwidth()
        self.height_value = master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (self.width_value,self.height_value))  # Set that the GUI takes up all the screen
        self.directories = []  # We store here the name of the scan folders
        
        
        # Title
        self.title = Label(master, text = "Scans visualization").grid(row=0, columnspan = 5)
        
        #Buttons to select the files
        self.select_file_1 = Button(master, text = "First Scan").grid(row = 1, column = 0, columnspan = 2)
        self.select_file_2 = Button(master, text = "Second Scan").grid(row = 2, column = 0, columnspan = 2)
        self.select_file_3 = Button(master, text = "Third Scan").grid(row = 3, column = 0, columnspan = 2)
        self.select_file_4 = Button(master, text = "Fourth Scan").grid(row = 4, column = 0, columnspan = 2)
        
        
        def load_file(self):
            self.folder = filedialog.askdirectory
            
        
        
        
    
    
    
    
if __name__ == "__main__":
    root = Tk()
    slice_vis = slices_vis_app(root)
    root.mainloop()
    