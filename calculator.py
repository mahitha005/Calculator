import tkinter as tk
def click(val):
    temp=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,temp+val)
def clear():
    entry.delete(0,tk.END)
def calc():
    try:
        res=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(res))
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Invalid")
def spec(op):
    try:
        val=float(entry.get())
        if(op=='√'):
            res=val**(0.5)
        entry.delete(0,tk.END)
        entry.insert(0,str(res))
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Invalid")
def backspace():
    val=entry.get()
    entry.delete(len(val)-1)
root =tk.Tk()
root.title("Calculator")
entry=tk.Entry(root,width=35,borderwidth=5,bg="#E7DDFF",fg="black")
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=20)
buttons=[('7',2,0),('8',2,1),('9',2,2),('*',2,3),
         ('4',3,0),('5',3,1),('6',3,2),('-',3,3),
         ('1',4,0),('2',4,1),('3',4,2),('+',4,3),
         ('√',5,0),('0',5,1),('^',5,2),('÷',5,3)]
for (val,row,col) in buttons:
    if(val=="*"):
        tk.Button(root,text='x',padx=20,pady=20,command=lambda v=val:click(v)).grid(row=row,column=col)
    elif(val=="√"):
        tk.Button(root,text='√',padx=20,pady=20,command= lambda: spec('√'),bg="orange",fg="black").grid(row=row,column=col)
    elif(val=='^'):
        tk.Button(root,text='^',padx=20,pady=20,command= lambda: click('**'),bg="orange",fg="black").grid(row=row,column=col)
    elif(val=='÷'):
        tk.Button(root,text='÷',padx=20,pady=20,command= lambda: click('/')).grid(row=row,column=col)
    elif col==3:
        tk.Button(root,text=val,padx=20,pady=20,command=lambda v=val:click(v)).grid(row=row,column=col)
    else:
        tk.Button(root,text=val,padx=20,pady=20,command=lambda v=val:click(v),bg="orange",fg="black").grid(row=row,column=col)
tk.Button(root,text='AC',padx=20,pady=20,command= clear,).grid(row=1,column=0)
tk.Button(root,text='.',padx=20,pady=20,command=lambda:click('.')).grid(row=1,column=1)
tk.Button(root,text='⌫',padx=20,pady=20,command=backspace).grid(row=1,column=2)
tk.Button(root,text='=',padx=20,pady=20,command= calc).grid(row=1,column=3)
root.mainloop()
