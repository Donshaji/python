import tkinter as tk
root=tk.Tk()
root.geometry("500x700")
current=""
def dispaly(x):
    current = textBox1.get("1.0", tk.END)
    textBox1.delete("1.0", tk.END)
    current=current+str(x)
    current=current.replace("\n","")
    textBox1.insert(tk.END, current)
def clear_it():
    textBox1.delete("1.0", tk.END)

def cal():
    current = textBox1.get("1.0", tk.END)
    textBox1.delete("1.0", tk.END)
    x=eval(current)
    current=current+'='+str(x)
    current=current.replace("\n","")
    textBox1.insert(tk.END, current)

textBox1=tk.Text(root,height=4,width=20)
textBox1.pack()

frame=tk.Frame(root)
frame.columnconfigure(0,weight=1)
frame.columnconfigure(1,weight=1)
frame.columnconfigure(2,weight=1)

bt1=tk.Button(frame,text="1",command=lambda: dispaly(1))
bt1.grid(row=0,column=0,sticky=tk.W+tk.E)
bt2=tk.Button(frame,text="2",command=lambda: dispaly(2))
bt2.grid(row=0,column=1,sticky=tk.W+tk.E)
bt3=tk.Button(frame,text="3",command=lambda: dispaly(3))
bt3.grid(row=0,column=2,sticky=tk.W+tk.E)

bt4=tk.Button(frame,text="4",command=lambda: dispaly(4))
bt4.grid(row=1,column=0,sticky=tk.W+tk.E)
bt5=tk.Button(frame,text="5",command=lambda: dispaly(5))
bt5.grid(row=1,column=1,sticky=tk.W+tk.E)
bt6=tk.Button(frame,text="6",command=lambda: dispaly(6))
bt6.grid(row=1,column=2,sticky=tk.W+tk.E)

bt7=tk.Button(frame,text="7",command=lambda: dispaly(7))
bt7.grid(row=2,column=0,sticky=tk.W+tk.E)
bt8=tk.Button(frame,text="8",command=lambda: dispaly(8))
bt8.grid(row=2,column=1,sticky=tk.W+tk.E)
bt9=tk.Button(frame,text="9",command=lambda: dispaly(9))
bt9.grid(row=2,column=2,sticky=tk.W+tk.E)

bt10=tk.Button(frame,text="=",command=cal)
bt10.grid(row=3,column=0,sticky=tk.W+tk.E)
bt11=tk.Button(frame,text="0",command=lambda: dispaly(0))
bt11.grid(row=3,column=1,sticky=tk.W+tk.E)
bt12=tk.Button(frame,text="+",command=lambda: dispaly('+'))
bt12.grid(row=3,column=2,sticky=tk.W+tk.E)

bt13=tk.Button(frame,text="-",command=lambda: dispaly('-'))
bt13.grid(row=4,column=0,sticky=tk.W+tk.E)
bt14=tk.Button(frame,text="x",command=lambda: dispaly('x'))
bt14.grid(row=4,column=1,sticky=tk.W+tk.E)
bt15=tk.Button(frame,text="/",command=lambda: dispaly('/'))
bt15.grid(row=4,column=2,sticky=tk.W+tk.E)
bt15=tk.Button(frame,text="C",command=clear_it)
bt15.grid(row=5,column=2,sticky=tk.W+tk.E)


frame.pack(fill="x")
root.mainloop()