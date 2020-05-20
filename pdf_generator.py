#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:23:47 2020

@author: gauravsingh
"""

from fpdf import FPDF

class pdf_generator:
    def __init__(self,some_string,pdf_file):
        self.some_string = some_string
        self.pdf_file=pdf_file


    def pdf_generator(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=self.some_string, ln=1, align="C")
        pdf.output(self.pdf_file)
        
        
        
        
