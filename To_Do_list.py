import tkinter as tk
from tkinter import ttk



class Gui(tk.Tk):
    bgExt = "#053959"
    bgMid = "#07B0F2"
    bgInt = "#444DF2"
    fg = "#FFFFFF"
    
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("To Do List")
        self.resizable(0,0)
        self.config(bg=self.bgExt)
        self.tasks = []
        self.readTasks()
        self.AddtaskFrame()
        self.AddedtasksFrame()
        self.showtask()
        
    def readTasks(self):
        with open(R"to_do_list\tasklist.txt") as txt:
            self.tasks = txt.read().split()
        
    def saveTasks(self):
        with open(R"to_do_list\tasklist.txt","w") as txt:
            for task in self.tasks:
                txt.write(f"{task} ")
            
    def AddtaskFrame(self):
        # 1st FRAME Add task
        self.addTask_frame= tk.Frame(self,
                          width=400,
                          height=100,
                          bg=self.bgMid,
                          highlightthickness=2,
                          highlightbackground=self.fg,
                          highlightcolor=self.fg)
        self.addTask_frame.pack(side="top",
                           padx=5,
                           pady=5,
                           fill="both")
        
        self.addtask_label = tk.Label(self.addTask_frame,
                                 text="Add Task:",
                                 fg=self.fg,
                                 bg=self.bgMid,
                                 width=30,
                                 font=("arial",16,"bold"))
        self.addTask_frame.columnconfigure(0,weight=2)
        self.addTask_frame.columnconfigure(1,weight=1)
        self.addtask_label.grid(row=0,
                           column=0,
                           columnspan=2)
        
        self.addtask_entry = tk.Entry(self.addTask_frame,
                                bg=self.bgInt,
                                fg=self.fg,
                                border=2,
                                width=30,
                                font=("arial",12)
                                )
        self.addtask_entry.grid(row=1,
                           column=0,
                           pady=5)
        
        self.addtask_button = tk.Button(self.addTask_frame,
                                   bg=self.bgMid,
                                   text="ADD",
                                   width=10,
                                   fg=self.fg,
                                   command= self.addtask)
        self.addtask_button.grid(row=1,column=1,sticky="W",ipady=5)
        
    def AddedtasksFrame(self):
        # 2nd FRAME Added tasks
        self.added_frame= tk.Frame(self,
                          width=400,
                          height=400,
                          bg=self.bgMid,
                          highlightthickness=2,
                          highlightbackground=self.fg,
                          highlightcolor=self.fg)
        self.added_frame.pack(padx=5,
                           pady=5,
                           fill="both")
        
        self.added_frame.pack_propagate(False)
        self.added_frame.columnconfigure(0,weight=3)
        self.added_frame.columnconfigure(1,weight=1)
        
    def remove(self,task):
        self.tasks.remove(task)
        self.saveTasks()
        self.showtask()
        
    def showtask(self):
        for widget in self.added_frame.winfo_children():
            widget.destroy()
        
        taskframe = tk.Frame(self.added_frame,
                                  width=300,
                                  height=380,
                                  bg=self.bgInt
                                )
        taskframe.pack_propagate(False)
        buttonframe = tk.Frame(self.added_frame,
                                  width=100,
                                  height=380,
                                  bg=self.bgInt
                                )
        buttonframe.pack_propagate(False)
        taskframe.grid(row=0,column=0,padx=10,pady=10)
        buttonframe.grid(row=0,column=1,padx=10,pady=10)
        
        for task in self.tasks:
            
            self.taskLabel = tk.Label(taskframe,
                                  width=30,
                                  font=("arial",12),
                                  bg= self.bgInt,
                                  fg= self.fg,
                                  text= task
                                )
            self.removeButton = tk.Button(buttonframe,
                                  font=("arial",12),
                                  bg= self.bgMid,
                                  fg= self.fg,
                                  text= "Remove",
                                  command= lambda t=task : self.remove(t)
                                )
            
            self.taskLabel.pack(padx=5,pady=9)
            self.removeButton.pack(padx=5,pady=5)      
    
    def addtask(self):
        action = self.addtask_entry.get()
        print(action)
        if action :
            self.tasks.append(action)
            self.addtask_entry.delete(0,tk.END)
            self.saveTasks()
            self.showtask()
        
   
        
if __name__== "__main__":
    toDo = Gui()
    toDo.mainloop()
    print(toDo.tasks)
    