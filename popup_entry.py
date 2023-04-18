class PopupEntry(tk.Entry):
    def __init__(self, parent, x, y, textvar,width = 10 ,entry_value='', text_justify = 'left', ):
        super().__init__(parent, relief = 'flat', justify = text_justify,bg='white', textvariable=textvar, font= "sublime ")
        self.place(x=x, y=y, width=width)
        
        self.textvar = textvar
        self.textvar.set(entry_value)
        self.focus_set()
        self.select_range(0, 'end')
        # move cursor to the end
        self.icursor('end')

        self.wait_var = tk.StringVar(master=self)
        self._bind_widget()

        self.entry_value = entry_value
        self.wait_window()
    
    def _bind_widget(self):
        self.bind("<Return>", self.retrive_value)
        self.bind('<FocusOut>', self.retrive_value)

    def retrive_value(self, e):
        value = self.textvar.get()
        self.destroy()
        self.textvar.set(value)
 
            
def demo():

    root = tk.Tk()
    root.title('Demo')
    root.geometry('620x200')

    PopupEntry(root,0,0,tk.StringVar(),width=200)
    root.mainloop()

if __name__ == '__main__':

    demo()
