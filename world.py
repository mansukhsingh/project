#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template
world=Flask(__name__)
@world.route('/')
def fhjhfjh():
    return render_template('d:df.html') #IT TAKES STRING VALUE
world.run()


# In[ ]:





# In[4]:


from flask import Flask,render_template,request
world=Flask(__name__)
@world.route('/')
def function():
    return render_template('d:flask.html') 
@world.route('/mansukh',methods=['POST'])
def xyz():
    if(request.method=='POST'):
        username=request.form['username']
        password=request.form['password']
        curry=request.form['curry']
        quantity=request.form['quantity']
        quantity2=request.form['quantity2']
        return render_template('d:flask.html')
world.run()


# In[2]:


import smtplib
server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login('mansukh11singh@gmail.com','mites@111')
server.sendmail('mansukh11singh@gmail.com','kaur17karamjeet@gmail.com','k')
server.quit()


# # from flask import Flask,render_template,request
# world=Flask(__name__)
# @world.route('/')
# def function():
#     return render_template('d:flask.html') 
# @world.route('/mansukh',methods=['POST'])
# def xyz():
#     if(request.method=='POST'):
#         
#         return render_template('d:deployment.html')

# In[ ]:


from flask import Flask,render_template,request
world=Flask(__name__)
@world.route('/')
def function():
    return render_template('d:deployment.html') 
@world.route('/deployment',methods=['POST'])
def xyz():
    if(request.method=='POST'):
        num1=request.form['num1']
        num2=request.form['num2']
        total=int(num1)+int(num2)
        product=int(num1)*int(num2)
        return render_template('d:deployment.html',total=total,product=product)
world.run()


# In[ ]:




