#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:31:40 2020

@author: gauravsingh
"""
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import smtplib
#import os
from contextlib import contextmanager


class send_email:
    def __init__(self,username,password,toaddrs,msg_text,subject,fromaddr=None,attachment=None):
        
        self.username = username
        self.password = password
        self.toaddrs = toaddrs
        self.msg_text = msg_text
        self.subject=subject 
        self.fromaddr = fromaddr
        self.attachment = attachment
    
    @contextmanager   
    def make_connection(self):
        try:
            s = smtplib.SMTP('smtp.gmail.com:587')
            s.starttls()
            s.login(self.username, self.password)
            yield s
        
        finally:
            s.quit()
            
    def send_email(self):
        #s.set_debuglevel(1)
        msg = MIMEMultipart()
        sender = self.fromaddr
        recipients = self.toaddrs
        msg['Subject'] = self.subject
        if self.fromaddr is not None: 
            msg['From'] = sender
        msg['To'] = recipients
        #if self.attachment is not None:
        attached_file_path = self.attachment
        attached_file = open(attached_file_path,"rb")
        msg.attach(MIMEText(self.msg_text,'plain'))             
        part = MIMEBase('application', "octet-stream")
        part.set_payload(attached_file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment",filename=attached_file_path)
        msg.attach(part)
    
        
        with self.make_connection() as s:
            print(msg)
            s.send_message(msg,sender, recipients)
        
            
