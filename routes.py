#!/usr/bin/python

from flask import Flask, render_template, request, flash
import os
from forms import WeightForm, ConfirmForm

 
app = Flask(__name__, static_url_path='')   

app.secret_key = 'development key'   
 
@app.route('/')
def home():
        return render_template('home.html')
        return app.send_static_file('main.css')
        
@app.route('/about')
def about():
  return render_template('about.html')
  
@app.route('/control', methods =['GET', 'POST'])
def control():
  form = WeightForm(request.form)
  
  if request.method == 'POST':
   if form.validate() == False:
      #print form.errors  
      #flash('All fields are required.')
      return render_template('control.html', form=form)
   
   else:
        weight = str(form.name.data)
        weightfile = open('weightfile', 'w')
        weightfile.write(weight)
        weightfile.close()
        form = ConfirmForm(request.form)  
        return render_template('control2.html', form=form, weight=weight)
      
 
  elif request.method == 'GET':
    return render_template('control.html', form=form)
    
 
  
      
@app.route('/control2', methods =['GET', 'POST'])
def control2():
        form =ConfirmForm(request.form)
        file = open('weightfile', 'r')
        weight = file.read()
        file.close()
        
        if request.method == 'POST':
                if form.validate() == False:
                        print form.errors  
                        flash('All fields are required.')
                        return render_template('control2.html', form=form, weight=weight)
                
                else:
                        x = str(form.confirm.data)
                        if x == '2':
                                form = WeightForm(request.form)
                                return render_template('control.html', form=form, weight=weight)
                                
                        elif x == '1':
                                return render_template('control2.html', form=form, weight=weight)
                        
        elif request.method == 'GET':
                print "hello"
                return render_template('control.html', form=form, weight = weight)
                


if __name__ == '__main__':
  app.run(host= '0.0.0.0', debug=True)
