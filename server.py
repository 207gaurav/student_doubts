#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:12:30 2020

@author: gauravsingh
"""

from flask import Flask, flash, redirect, render_template, request, session, abort,jsonify,json,make_response
import logging 
from pdf_generator import pdf_generator
from send_mail import send_email
from timeit import default_timer as timer
import email_creds

app = Flask(__name__)

logging.basicConfig(filename="app.log", format='%(asctime)s %(message)s',level=logging.DEBUG, filemode='a')

@app.route("/recieve_question",methods = ['POST'])
def recieve_question():
    if request.method == "POST":
        try:
            
            data = request.data
            data = json.loads(data)
            question = data['data']
            recepient_user_email = data['email_id']
            
            
            pdf_generation = pdf_generator(question,'related_questions.pdf')
            pdf_generation.pdf_generator()
            
            attachment = 'related_questions.pdf'
            sending_mails = send_email(email_creds.email_creds["username"],email_creds.email_creds["password"],recepient_user_email,"related questions","question related to asked question",fromaddr=email_creds.email_creds["username"],attachment=attachment)
            sending_mails.send_email()
            
            return "Mail sent"
            
        except:
            logging.exception("message")



if __name__ == "__main__":
    app.run(host = "127.0.0.1",debug = True,threaded=True)


