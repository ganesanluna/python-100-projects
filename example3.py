#-*-coding: utf-8-*-
from Tkinter import *                                                                           #1
import math                                                                                     #2

class calc:                                                                                     #3
 def getandreplace(self):                                                                       #4
  """replace x with * and ÷ with /"""                       
  
  self.expression = self.e.get()                                                                #5
  self.newtext=self.expression.replace(self.newdiv,'/')                                         #6
  self.newtext=self.newtext.replace('x','*')                                                    #7

 def equals(self):                                                                              #8
  """when the equal button is pressed"""

  self.getandreplace()                                                                          #9
  try:                                                                                          #10
   self.value= eval(self.newtext) #evaluate the expression using the eval function              #11
  except SyntaxError or NameErrror:                                                             #12
   self.e.delete(0,END)                                                                         #13
   self.e.insert(0,'Invalid Input!')                                                            #14
  else:                                                                                         #15
   self.e.delete(0,END)                                                                         #16
   self.e.insert(0,self.value)                                                                  #17
                 
 def squareroot(self):                                                                          #18
  """squareroot method"""
  
  self.getandreplace()                                                                          #19
  try:                                                                                          #20
   self.value= eval(self.newtext) #evaluate the expression using the eval function              #21
  except SyntaxError or NameErrror:                                                             #22
   self.e.delete(0,END)                                                                         #23
   self.e.insert(0,'Invalid Input!')                                                            #24
  else:                                                                                         #25
   self.sqrtval=math.sqrt(self.value)                                                           #26
   self.e.delete(0,END)                                                                         #27
   self.e.insert(0,self.sqrtval)                                                                #28

 def square(self):                                                                              #29
  """square method"""
  
  self.getandreplace()                                                                          #30
  try:                                                                                          #31
   self.value= eval(self.newtext) #evaluate the expression using the eval function              #32
  except SyntaxError or NameErrror:                                                             #33
   self.e.delete(0,END)                                                                         #34
   self.e.insert(0,'Invalid Input!')                                                            #35
  else:                                                                                         #36
   self.sqval=math.pow(self.value,2)                                                            #37
   self.e.delete(0,END)                                                                         #38
   self.e.insert(0,self.sqval)                                                                  #39
                 
 def clearall(self):                                                                            #40
  """when clear button is pressed,clears the text input area"""
  self.e.delete(0,END)                                                                          #41
 
 def clear1(self):                                                                              #42
  self.txt=self.e.get()[:-1]                                                                    #43
  self.e.delete(0,END)                                                                          #44
  self.e.insert(0,self.txt)                                                                     #45
    
 def action(self,argi):                                                                         #46 
  """pressed button's value is inserted into the end of the text area"""
  self.e.insert(END,argi)                                                                       #47
 
 def __init__(self,master):                                                                     #48
  """Constructor method"""
  master.title('Calulator')                                                                     #49
  master.geometry()                                                                             #50
  self.e = Entry(master)                                                                        #51
  self.e.grid(row=0,column=0,columnspan=6,pady=3)                                               #52
  self.e.focus_set() #Sets focus on the input text area                                         #53
    
  self.div='÷'                                                                                  #54
  self.newdiv=self.div.decode('utf-8')

  #Generating Buttons
  Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)  #55
  Button(master,text='AC',width=3,command=lambda:self.clearall()).grid(row=1, column=4)             #56
  Button(master,text='C',width=3,command=lambda:self.clear1()).grid(row=1, column=5)                #57
  Button(master,text="+",width=3,command=lambda:self.action('+')).grid(row=4, column=3)             #58
  Button(master,text="x",width=3,command=lambda:self.action('x')).grid(row=2, column=3)             #59
  Button(master,text="-",width=3,command=lambda:self.action('-')).grid(row=3, column=3)             #60
  Button(master,text="÷",width=3,command=lambda:self.action(self.newdiv)).grid(row=1, column=3)     #61
  Button(master,text="%",width=3,command=lambda:self.action('%')).grid(row=4, column=2)             #62
  Button(master,text="7",width=3,command=lambda:self.action('7')).grid(row=1, column=0)             #63
  Button(master,text="8",width=3,command=lambda:self.action(8)).grid(row=1, column=1)               #64
  Button(master,text="9",width=3,command=lambda:self.action(9)).grid(row=1, column=2)               #65
  Button(master,text="4",width=3,command=lambda:self.action(4)).grid(row=2, column=0)               #66
  Button(master,text="5",width=3,command=lambda:self.action(5)).grid(row=2, column=1)               #67
  Button(master,text="6",width=3,command=lambda:self.action(6)).grid(row=2, column=2)               #68
  Button(master,text="1",width=3,command=lambda:self.action(1)).grid(row=3, column=0)               #69
  Button(master,text="2",width=3,command=lambda:self.action(2)).grid(row=3, column=1)               #70
  Button(master,text="3",width=3,command=lambda:self.action(3)).grid(row=3, column=2)               #71
  Button(master,text="0",width=3,command=lambda:self.action(0)).grid(row=4, column=0)               #72
  Button(master,text=".",width=3,command=lambda:self.action('.')).grid(row=4, column=1)             #73
  Button(master,text="(",width=3,command=lambda:self.action('(')).grid(row=2, column=4)             #74
  Button(master,text=")",width=3,command=lambda:self.action(')')).grid(row=2, column=5)             #75
  Button(master,text="√",width=3,command=lambda:self.squareroot()).grid(row=3, column=4)            #76
  Button(master,text="x²",width=3,command=lambda:self.square()).grid(row=3, column=5)               #77
#Main
root = Tk()                                                                                         #78
obj=calc(root) #object instantiated                                                                 #79
root.mainloop()                                                                                     #80
