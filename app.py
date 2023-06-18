#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import openai
import time
from tkinter import *
from tkinter import font

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")
msg = [{"role": "system", "content": "You are a helpful assistant."}]
total_tokens = 0

class chatGPT_GUI(Tk):
  def __init__(self):
    super().__init__()
    self.title("OpenAI ChatGPT GUI")
    self.geometry("500x500")

    self.my_font = font.Font(family="宋介文體", size=12)
    
    self.label = Label(self, text='请输入要ChatGPT回答的问题:',font=self.my_font ,bg="lightcyan" ,fg='teal')
    self.label.pack(fill= 'both', pady=5)

    self.GUI_Question = Text(self, bg='ivory', font=self.my_font, height=10)
    self.GUI_Question.pack()

    self.button = Button(self, text='Answer', fg='green', command=self.Ask)
    self.button.pack(pady=5)

    self.out = Text(self)
    self.out.pack(fill=BOTH, expand=1,pady=5)
    self.out.tag_configure("Question", foreground="steel blue" ,font=("Calibri", 13, "bold"))
    self.out.tag_configure("Answer", foreground="black" ,font=("Calibri", 12, "normal"))
    self.out.configure(state=DISABLED)

  def Ask(self):
    self.out.configure(state=NORMAL)
    self.out.delete("1.0", END)
    prompt = str(self.GUI_Question.get('0.0', 'end'))
    self.out.insert(END, prompt + "\n", "Question")

    content = {"role": "user", "content": prompt}

    msg.append(content)

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=msg
    )

    global total_tokens
    total_tokens += int(completion["usage"]["total_tokens"])

    #print(completion['choices'][0]['message']['content'] + "\n")
    #print ("There are " + str(total_tokens) + " have been used" + "\n")

    msg.append({"role": "assistant", "content": completion['choices'][0]['message']['content']})
    self.out.insert(END, completion['choices'][0]['message']['content'] + "\n", "Answer")
    self.out.configure(state=DISABLED)
    self.GUI_Question.delete('0.0', END)

    return True
    

if __name__ == '__main__':
  my_app = chatGPT_GUI()
  my_app.mainloop()

  
