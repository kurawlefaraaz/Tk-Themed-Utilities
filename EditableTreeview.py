from tkinter import ttk
from poput_entry import PopupEntry

import tkinter as tk

class EditableTreeview(ttk.Treeview):
    def __init__(self, parent, columns, show, bind_key,data:list, non_editable_columns = None):
        super().__init__(parent, columns=columns, show=show)
        self.parent = parent
        self.column_name = columns
        self.data = data
        self.bind_key = bind_key
        self.non_editable_columns = non_editable_columns

        self.set_primary_key_column_attributes()
        self.set_headings()
        self.insert_data()
        self.set_edit_bind_key()
    
    def set_primary_key_column_attributes(self):
        self.column("#0",width=100,stretch=1)

    def set_headings(self):
        for i in self.column_name:
            self.heading(column=i, text=i)

    def insert_data(self):
        for values in self.data:
            self.insert('', tk.END, values=values)
    
    def set_edit_bind_key(self):
        self.bind('<Double Button-1>', self.edit)

    def get_absolute_x_cord(self):
        rootx = self.winfo_pointerx()
        widgetx = self.winfo_rootx()

        x = rootx - widgetx

        return x

    def get_absolute_y_cord(self):
        rooty = self.winfo_pointery()
        widgety = self.winfo_rooty()

        y = rooty - widgety

        return y
    
    def get_current_column(self):
        pointer = self.get_absolute_x_cord()
        return self.identify_column(pointer)

    def get_cell_cords(self,row,column):
        return self.bbox(row, column=column)
    
    def get_selected_cell_cords(self):
        row = self.focus()
        column = self.get_current_column()
        return self.get_cell_cords(row = row, column = column)

    def update_row(self, values, current_row, currentindex):
        try:self.parent.state()
        except: return

        self.delete(current_row)
        
        # Put it back in with the upated values
        self.insert('', currentindex, values = values)

    def check_region(self):
        result = self.identify_region(x=(self.winfo_pointerx() - self.winfo_rootx()), y=(self.winfo_pointery()  - self.winfo_rooty()))
        print(result)
        if result == 'cell':return True
        else: return False

    def check_non_editable(self):
        if self.get_current_column() in self.non_editable_columns:return False
        else: return True

    def edit(self, e):
        if self.check_region() == False: return
        elif self.check_non_editable() == False: return
        
        current_row = self.focus()
        currentindex = self.index(self.focus())
        current_row_values = list(self.item(self.focus(),'values'))
        current_column = int(self.get_current_column().replace("#",''))-1
        current_cell_value = current_row_values[current_column]

        entry_cord = self.get_selected_cell_cords()
        entry_x = entry_cord[0]
        entry_y = entry_cord[1]
        entry_w = entry_cord[2]
        entry_h = entry_cord[3]

        entry_var = tk.StringVar()
        
        PopupEntry(self, x=entry_x, y=entry_y, width=entry_w,entry_value=current_cell_value, textvar= entry_var, text_justify='left')

        if entry_var.get() != current_cell_value:
            current_row_values[current_column] = entry_var.get()
            self.update_row(values=current_row_values, current_row=current_row, currentindex=currentindex)
            
def demo():

    root = tk.Tk()
    root.title('Demo')
    root.geometry('620x200')
    
    columns = ('attribute', 'value', 'Broh')
    data = [('relx','6','7346347347'),('rely','1',24624623)]

    tree = EditableTreeview(root, columns=columns, show='headings',bind_key='<Double-Button-1>',data=data, non_editable_columns="#1")
    tree.pack()

    # add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack()
    
    # run the app
    root.mainloop()
            
    
    


if __name__ == '__main__':

    demo()
