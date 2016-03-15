from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, FloatField, PasswordField, validators, TextAreaField, SubmitField, IntegerField, RadioField


class WeightForm(Form):
  name = FloatField("Please input the desired weight to be drained from tank (in kg)", [validators.NumberRange(min = 1, max = 800)])
  submit = SubmitField("Confirm")
  
class ConfirmForm(Form):
     confirm = RadioField('Is this correct?', [validators.Required()], choices=[('1','Yes'),('2','No')])
     submit = SubmitField("Confirm")   
  
  
  
 
