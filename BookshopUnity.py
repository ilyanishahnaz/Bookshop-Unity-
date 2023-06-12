############################################### Book Unity ########################################
#ID MEMBERS ---- NAME
#1201101864 ---- AFIF DZAKIRIN BIN MOHD AZLI
#1201101761 ---- ILYANI SHAHNAZ BINTI SHUKOR
#1201101871 ---- MUHAMMAD ZAFRI BIN MARWAN
#1201101522 ---- RAFIE BIN RAUZAN
#GROUP : TT4L
#TUTOR : SIR NEOH KEE LIN
#PROJECT NAME : BOOKSHOP SYSTEM
#####################################################################################################

from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import sqlite3

def no():
    pass 

def goto(k):
    if k == 2:
        register()

def table():
    # Create table
    ###################################################  User table  ################################################################################
    #Create a database or connect
    conn = sqlite3.connect('storage.db')
    #Create cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS  User (
            Username text,
            Password text,
            Name text,
            Age integer,
            Email text,
            Phone integer,
            Type text,
            Money integer
            )""")
    #Commit changes
    conn.commit()
    #Close connection
    conn.close()

    ###########################################################   Book Table   ###################################################################

    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS  book (
            title text,
            author text,
            category text,
            year integer,
            price integer,
            quantity integer
            )""")
    conn.commit()
    conn.close()

    ###########################################################   Cart Table   ###################################################################
   
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS  cart (
            title text,
            price integer,
            quantity integer,
            bookid integer
            )""")
    conn.commit()
    conn.close()

    ###########################################################   Paid Table   ###################################################################


    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS  paid (
            name text,
            title text,
            quantity integer
            )""")
    conn.commit()
    conn.close()

    ###################################################################################################################################

def book_manager () :
    bookmanager = Tk()
    bookmanager.title('BookshopUnity')
    bookmanager.geometry("800x400")
    bookmanager.focus()

    ##########################################################   Function Section   ##############################################################

    def View():
        conn = sqlite3.connect("storage.db")
        curr = conn.cursor()
        curr.execute("SELECT *, oid FROM book list")
        rows = curr.fetchall()
        for row in rows:
            # change input
            z = (row[6],row[0],row[1],row[2],row[3],row[4],row[5],row[6],)
            tree.insert("", tk.END, values=z)
        conn.commit()
        conn.close()

    def add_new_book() :
        add_book = Tk()
        add_book.title('BookshopUnity')
        add_book.geometry("310x200")
        
        def submit() :

            #Create a database or connect
            conn = sqlite3.connect('storage.db')
            #Create cursor
            c = conn.cursor()

            #Insert table
            c.execute("INSERT INTO book VALUES (:title, :author, :category, :year, :price, :quantity)",
                    {
                        'title': title.get(),
                        'author': author.get(),
                        'category': category.get(),
                        'year': year.get(),
                        'price': price.get(),
                        'quantity': quantity.get()
                    })

            #Commit changes
            conn.commit()
            #Close connection
            conn.close()

            #Clear text box
            title.delete(0, END)
            author.delete(0, END)
            category.delete(0, END)
            year.delete(0, END)
            price.delete(0, END)
            quantity.delete(0, END)
            
        #Create Entry box
        title = Entry(add_book, width=30)
        title.grid(row=0, column=1, padx=20, pady=(10,0))
        author = Entry(add_book, width=30)
        author.grid(row=1, column=1)
        category = Entry(add_book, width=30)
        category.grid(row=2, column=1)
        year = Entry(add_book, width=30)
        year.grid(row=3, column=1)
        price = Entry(add_book, width=30)
        price.grid(row=4, column=1)
        quantity = Entry(add_book, width=30)
        quantity.grid(row=5, column=1)
        
        #Create text box label
        title_label = Label(add_book, text="Title")
        title_label.grid(row=0, column=0, pady=(10,0))
        author_label = Label(add_book, text="Author")
        author_label.grid(row=1, column=0)
        category_label = Label(add_book, text="Category")
        category_label.grid(row=2, column=0)
        year_label = Label(add_book, text="Year")
        year_label.grid(row=3, column=0)
        price_label = Label(add_book, text="Price")
        price_label.grid(row=4, column=0)
        quantity_label = Label(add_book, text="Quantity")
        quantity_label.grid(row=5, column=0)

        #Create submit button
        submit_btn = Button(add_book, text="Add new book", command=lambda:[submit(),add_book.destroy(),bookmanager.destroy(),book_manager()])
        submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    def delete_book():
        if str(Select_ID_Entry.get()) == "":
            messagebox.showinfo("Error", "Please select ID")
        else: 
            #Create a database or connect
            conn = sqlite3.connect('storage.db')
            #Create cursor
            c = conn.cursor()

            #Delete record
            c.execute("DELETE from book WHERE oid = " + Select_ID_Entry.get())

            #Clear text box
            Select_ID_Entry.delete(0, END)

            #Commit changes
            conn.commit()
            #Close connection
            conn.close()

    def select_book() :
        Select_ID_Entry.delete(0,END)
        
        selected = tree.focus()

        selected_id = tree.item(selected,'values')

        if str(selected_id) == "":
            messagebox.showinfo("Error", "Please select ID")

        else:
            #Choose column 
            Select_ID_Entry.insert(0, selected_id[0])

    def edit_book() :
        if str(Select_ID_Entry.get()) == "":
            messagebox.showinfo("Error", "Please select ID")

        else: 
            def update_book():
                
                #Create a database or connect
                conn = sqlite3.connect('storage.db')
                #Create cursor
                c = conn.cursor()

                book_id = Select_ID_Entry.get()

                c.execute("""UPDATE book SET
                        title = :title,
                        author = :author,
                        category = :category,
                        year = :year,
                        price = :price,
                        quantity = :quantity
                        
                        WHERE oid = :oid""",
                        {
                        'title': title_edit.get(),
                        'author': author_edit.get(),
                        'category': category_edit.get(),
                        'year': year_edit.get(),
                        'price': price_edit.get(),
                        'quantity': quantity_edit.get(),
                        'oid' : book_id
                        })

                #Commit changes
                conn.commit()
                #Close connection
                conn.close()
                #Close window
                editor.destroy()
        
            editor = Tk()
            editor.title('BookshopUnity')
            editor.geometry("270x180")

            book_id = Select_ID_Entry.get()

            #Create a database or connect
            conn = sqlite3.connect('storage.db')
            #Create cursor
            c = conn.cursor()

            #Query the database
            c.execute("SELECT * FROM book WHERE oid = " + book_id)
            records = c.fetchall()

            #Create global var
            global title_edit
            global author_edit
            global category_edit
            global year_edit
            global price_edit
            global quantity_edit

            #create text box
            title_edit = Entry(editor, width=30)
            title_edit.grid(row=0, column=1, padx=20, pady=(10,0))
            author_edit = Entry(editor, width=30)
            author_edit.grid(row=1, column=1)
            category_edit = Entry(editor, width=30)
            category_edit.grid(row=2, column=1)
            year_edit = Entry(editor, width=30)
            year_edit.grid(row=3, column=1)
            price_edit = Entry(editor, width=30)
            price_edit.grid(row=4, column=1)
            quantity_edit = Entry(editor, width=30)
            quantity_edit.grid(row=5, column=1)

            #Create text box label
            title_label_edit = Label(editor, text="Title")
            title_label_edit.grid(row=0, column=0, pady=(10,0))
            author_label_edit = Label(editor, text="Author")
            author_label_edit.grid(row=1, column=0)
            category_label_edit = Label(editor, text="Category")
            category_label_edit.grid(row=2, column=0)
            year_label_edit = Label(editor, text="Year")
            year_label_edit.grid(row=3, column=0)
            price_label_edit = Label(editor, text="Price")
            price_label_edit.grid(row=4, column=0)
            quantity_label_edit = Label(editor, text="Quantity")
            quantity_label_edit.grid(row=5, column=0)

            #Loop through results
            for record in records:
                    title_edit.insert(0, record[0])
                    author_edit.insert(0, record[1])
                    category_edit.insert(0, record[2])
                    year_edit.insert(0, record[3])
                    price_edit.insert(0, record[4])
                    quantity_edit.insert(0, record[5])

            #Create save button
            save_btn = Button(editor, text="Save Book", command=lambda:[update_book(),bookmanager.destroy(),book_manager()])
            save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=70)

    def search_book(*args) :
        ## Create Variable (to know which category)
        Search_Type = int()
        
        ##Search by Title
        if search_type.get() == "Title" :
            Search_Type = 1
        
        ##Search by Author
        elif search_type.get() == "Author" :
            Search_Type = 2
        
        ##Search by Category
        elif search_type.get() == "Category" :
            Search_Type = 3

        elif search_type.get() == "Type":
            messagebox.showinfo("Error", "Please select type")
        
        item_search = tree.get_children()
        search = search_entry_var.get().capitalize()

        for eachitem in item_search :
            if search in tree.item(eachitem)['values'][Search_Type] :
                
                search_var = tree.item(eachitem)['values']
                tree.delete(eachitem)

                tree.insert("",0,values=search_var)

    ################################################################ Tree View ###################################################################

    tree_scroll = Scrollbar(bookmanager)
    tree_scroll.pack(fill="y", expand="no", side =RIGHT)
    
    tree = ttk.Treeview(bookmanager, column=("c1","c2", "c3","c4","c5","c6","#7"), show='headings',yscrollcommand=tree_scroll.set)
    
    tree.column("#1", anchor=tk.CENTER,width=30)
    tree.heading("#1", text="ID")
            
    tree.column("#2", anchor=tk.W,width=150)
    tree.heading("#2", text="Title")

    tree.column("#3", anchor=tk.W,width=150)
    tree.heading("#3", text="Author")

    tree.column("#4", anchor=tk.CENTER,width=110)
    tree.heading("#4", text="Category")

    tree.column("#5", anchor=tk.CENTER,width=100)
    tree.heading("#5", text="Year Published")

    tree.column("#6", anchor=tk.CENTER,width=70)
    tree.heading("#6", text="Price")

    tree.column("#7", anchor=tk.CENTER,width=70)
    tree.heading("#7", text="Quantity")

    tree.pack()
    tree_scroll.config(command=tree.yview)
    View()

    #Create Select ID
    Select_ID = Label(bookmanager, text="ID")
    Select_ID.place(x=20,y=230)
    Select_ID_Entry = Entry(bookmanager, width=10)
    Select_ID_Entry.place(height=25,x=40,y=230)

    #Create Search
    Search = Label(bookmanager, text="Search by")
    Search.place(x=410,y=240,height=30)
    search_entry_var = StringVar()
   
    Search_Entry = Entry(bookmanager,textvariable=search_entry_var)
    Search_Entry.place(x=410,y=280,height=25,width=200)
    search_entry_var.trace("w",search_book)

    #Create edit button
    edit_btn = Button(bookmanager, text="Edit book",bg="lightgray",command=edit_book)
    edit_btn.place(bordermode=OUTSIDE,x=40,y=260)
            
    #Create delete button
    delete_btn = Button(bookmanager, text="Delete book",bg="lightgray",command=lambda:[delete_book(),bookmanager.destroy(),book_manager()] )
    delete_btn.place(bordermode=OUTSIDE,x=40,y=290)

    #Create add new book button
    addbook_btn = Button(bookmanager, text="Add book",bg="lightgray",command=add_new_book)
    addbook_btn.place(bordermode=OUTSIDE,x=40,y=320)

    #Create select book button
    selectbook_btn = Button(bookmanager, text="Select book",bg="lightgray",command=select_book)
    selectbook_btn.place(height=25,x=120,y=230)

    #Create refresh button
    refresh_btn = Button(bookmanager, text="Refresh",bg="lightgray",command=lambda:[bookmanager.destroy(),book_manager()])
    refresh_btn.place(x=480,y=310)

    #Create return button
    return_btn = Button(bookmanager, text="Return To Profile",bg="lightgray",command=lambda:[bookmanager.destroy(),administrator()])
    return_btn.place(x=480,y=340)

    #Search Type
    search_type = StringVar()
    search_type.set("Type")
    type_list = OptionMenu(bookmanager, search_type, "Title","Author","Category")
    type_list.place(x=480,y=240,height=30)
    ##############################################################  Shopping Page  ######################################################################

def buy_book():
    shopping_pg = Tk()
    shopping_pg.title('BookshopUnity')
    shopping_pg.geometry("800x400")
    shopping_pg.focus()

    ##########################################################   Function Section   ##############################################################

    def View():
        conn = sqlite3.connect("storage.db")
        curr = conn.cursor()
        curr.execute("SELECT *, oid FROM book list")
        rows = curr.fetchall()
        for row in rows:
            # change input
            z = (row[6],row[0],row[1],row[2],row[3],row[4],row[5],row[6],)
            tree.insert("", tk.END, values=z)
        conn.commit()
        conn.close()

    def select_book() :
        addbook_id.delete(0,END)
        selected = tree.focus()
        selected_id = tree.item(selected,'values')
        if str(selected_id) == "":
            messagebox.showinfo("Error", "Please select ID")

        else:
            #Choose column 
            addbook_id.insert(0, selected_id[0])

    def tocart() :
        if str(addbook_id.get()) == "": 
            messagebox.showinfo("Error", "Please select ID")
        else : 
            addtocart = Tk()
            addtocart.title('BookshopUnity')
            addtocart.geometry("350x130")

            def savetocart():
                x = int(quant_box.get())
                if x <= avlquant:
                    conn = sqlite3.connect('storage.db')
                    c = conn.cursor()
                    c.execute("INSERT INTO cart VALUES (:title, :price, :quantity, :bookid)",
                        {
                            'title': title1,
                            'price': pricebook,
                            'quantity': x,
                            'bookid': id1
                        })
                    conn.commit()
                    conn.close()

                    y = avlquant - x

                    conn = sqlite3.connect('storage.db')
                    c = conn.cursor()
                    c.execute("""UPDATE book SET
                            title = :title,
                            author = :author,
                            category = :category,
                            year = :year,
                            price = :price,
                            quantity = :quantity
                            WHERE oid = :oid""",
                            {
                            'title': title1,
                            'author': author1,
                            'category': cartegory1,
                            'year': year1,
                            'price': pricebook,
                            'quantity': y,
                            'oid' : id1
                            })
                    conn.commit()
                    conn.close()
                    addtocart.destroy()
                    shopping_pg.destroy()
                    buy_book()

                else :
                    messagebox.showinfo("Error","Please Enter Right Amount")
                    addtocart.destroy()

            book_id = addbook_id.get()
            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            c.execute("SELECT * FROM book WHERE oid = " + book_id)
            records = c.fetchall()
            #Loop through results
            for record in records:
                title1 = record[0]
                author1= record[1]
                cartegory1 = record[2]
                year1 = record[3]
                pricebook = int(record[4])
                avlquant = int(record[5])
                id1 = book_id

            Label(addtocart,text= "Add "+title1+" to the cart?").place(x=50, y=20)
            Label(addtocart,text= "Enter Quantity").place(x=50, y=40)

            quant_box = Entry(addtocart, width=10)
            quant_box.place(x=50, y=70)
            save_btn = Button(addtocart,text= "Confirm", width=8,command=savetocart)
            save_btn.place(x=50, y=100)
            cancel_btn = Button(addtocart,text= "Cancel", width=8,command=lambda:[shopping_pg.destroy(),addtocart.destroy(),buy_book()])
            cancel_btn.place(x=170, y=100)

    def search_book(*args) :
        ## Create Variable (to know which category)
        Search_Type = int()
        
        ##Search by Title
        if search_type.get() == "Title" :
            Search_Type = 1
        
        ##Search by Author
        elif search_type.get() == "Author" :
            Search_Type = 2
        
        ##Search by Category
        elif search_type.get() == "Category" :
            Search_Type = 3

        elif search_type.get() == "Type":
            messagebox.showinfo("Error", "Please select type")
        
        item_search = tree.get_children()
        search = search_entry_var.get().capitalize()

        for eachitem in item_search :
            if search in tree.item(eachitem)['values'][Search_Type] :
                
                search_var = tree.item(eachitem)['values']
                tree.delete(eachitem)

                tree.insert("",0,values=search_var)

    ################################################################ Tree View Book List ###################################################################

    tree_scroll = Scrollbar(shopping_pg)
    tree_scroll.pack(fill="y", expand="no", side =RIGHT)
    
    tree = ttk.Treeview(shopping_pg, column=("c1","c2", "c3","c4","c5","c6","#7"), show='headings',yscrollcommand=tree_scroll.set)
    
    tree.column("#1", anchor=tk.CENTER,width=30)
    tree.heading("#1", text="ID")
            
    tree.column("#2", anchor=tk.W,width=150)
    tree.heading("#2", text="Title")

    tree.column("#3", anchor=tk.W,width=150)
    tree.heading("#3", text="Author")

    tree.column("#4", anchor=tk.CENTER,width=110)
    tree.heading("#4", text="Category")

    tree.column("#5", anchor=tk.CENTER,width=100)
    tree.heading("#5", text="Year Published")

    tree.column("#6", anchor=tk.CENTER,width=70)
    tree.heading("#6", text="Price")

    tree.column("#7", anchor=tk.CENTER,width=70)
    tree.heading("#7", text="Quantity")

    tree.pack()
    tree_scroll.config(command=tree.yview)
    View()

    #Create Select ID
    Select_ID = Label(shopping_pg, text="ID")
    Select_ID.place(x=20,y=230)
    addbook_id = Entry(shopping_pg, width=10)
    addbook_id.place(height=25,x=40,y=230)

    #Create Search
    Search = Label(shopping_pg, text="Search by")
    Search.place(x=410,y=240,height=30)
    search_entry_var = StringVar()
   
    Search_Entry = Entry(shopping_pg,textvariable=search_entry_var)
    Search_Entry.place(x=410,y=280,height=25,width=200)
    search_entry_var.trace("w",search_book)

    #create edit button
    add_btn = Button(shopping_pg, text="Add to Cart",bg="lightgray",command=tocart)
    add_btn.place(bordermode=OUTSIDE,x=40,y=260)

    #create select book button
    selectbook_btn = Button(shopping_pg, text="Select book",bg="lightgray",command=select_book)
    selectbook_btn.place(height=25,x=120,y=230)

    #create refresh button
    refresh_btn = Button(shopping_pg, text="Refresh",bg="lightgray",command=lambda:[shopping_pg.destroy(),buy_book()])
    refresh_btn.place(x=480,y=310)

    #create return button
    return_btn = Button(shopping_pg, text="Return To Profile",bg="lightgray",command=lambda:[shopping_pg.destroy(),buyer()])
    return_btn.place(x=480,y=340)

    #Search Type
    search_type = StringVar()
    search_type.set("Type")
    type_list = OptionMenu(shopping_pg, search_type, "Title","Author","Category")
    type_list.place(x=480,y=240,height=30)

def update_info(): 
    update_pg =Tk()
    update_pg.title('BookshopUnity')
    update_pg.geometry("800x600")

    def edit():
        #Create a database or connect
        conn = sqlite3.connect('storage.db')
        #Create cursor
        c = conn.cursor()

        user_id = userid

        c.execute("""UPDATE User SET
                Username = :usernameA,
                Password = :passwordA,
                Name = :nameA,
                Age = :ageA,
                Email = :emailA,
                Phone = :phoneA,
                Type = :typeA
                WHERE oid = :oid""",
                {
                'usernameA': username3a_label.get(),
                'passwordA': password3a_label.get(),
                'nameA': name3a_label.get(),
                'ageA': age3a_label.get(),
                'emailA': email3a_label.get(),
                'phoneA': phone3a_label.get(),
                'typeA': type1,
                'oid' : user_id
                })
        conn.commit()
        conn.close()

        def rturnn(qbook,idbk):
            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            c.execute("SELECT * FROM book WHERE oid = " + str(idbk))
            records = c.fetchall()
            for record in records:
                tqbook = record[5] # total quantity
            conn.commit()
            conn.close()

            tqall = int(qbook)+int(tqbook)

            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            returnbk = """UPDATE book SET quantity = ? WHERE oid = ?"""
            inputt = (str(tqall),str(idbk))
            c.execute(returnbk,inputt)
            conn.commit()
            conn.close()

        conn = sqlite3.connect('storage.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM cart")
        records = c.fetchall()
        conn.commit()
        conn.close()
        for record in records:
            qbook = record[2] # quantity
            idbk = record[3] # book id
            rturnn(qbook,idbk)

        update_pg.destroy()
        login_pg()

    def cancel ():
        update_pg.destroy()
        if type1 == "Administrator":
            administrator()
        else:
            buyer()

    Label(update_pg, text="Update Personal Info", font= ("Arial Bold", 10)).place(x=180,y=50)

    #Create text box label
    Label(update_pg, text="Username : ").grid(row=0, column=0, padx=(100,0), pady=(100,0))
    Label(update_pg, text="Password : ").grid(row=1, column=0, padx=(100,0))
    Label(update_pg, text="Name : ").grid(row=2, column=0, padx=(100,0))
    Label(update_pg, text="Age : ").grid(row=3, column=0, padx=(100,0))
    Label(update_pg, text="Email : ").grid(row=4, column=0, padx=(100,0))
    Label(update_pg, text="Mobile Number : ").grid(row=5, column=0, padx=(100,0))
    
    #Create text box
    username3a_label = Entry(update_pg, width=30)
    username3a_label.grid(row=0, column=1, padx=10, pady=(100,0))
    password3a_label = Entry(update_pg, width=30)
    password3a_label.grid(row=1, column=1)
    name3a_label = Entry(update_pg, width=30)
    name3a_label.grid(row=2, column=1)
    age3a_label = Entry(update_pg, width=30)
    age3a_label.grid(row=3, column=1)
    email3a_label = Entry(update_pg, width=30)
    email3a_label.grid(row=4, column=1)
    phone3a_label = Entry(update_pg, width=30)
    phone3a_label.grid(row=5, column=1)
    
    username3a_label.insert(0, username)
    password3a_label.insert(0, password)
    name3a_label.insert(0, name)
    age3a_label.insert(0, age)
    email3a_label.insert(0, email)
    phone3a_label.insert(0, phone)

    save_btn = Button(update_pg, text = "Save & Log Out", width=20, command=edit)
    save_btn.place(x=208,y=235)

    cancel_btn = Button(update_pg, text = "Cancel", width=20, command=cancel)
    cancel_btn.place(x=208,y=270)

    global img2
    img2=PhotoImage(file='logo3.png')
    Label(update_pg, image=img2).place(x=440,y=100)

def delete():
    delete_pg =Tk()
    delete_pg.title('BookshopUnity')
    delete_pg.geometry("300x130")

    def yes ():
        conn = sqlite3.connect('storage.db')
        c = conn.cursor()
        c.execute("DELETE from User WHERE oid = " + str(userid))
        conn.commit()
        conn.close()
        if type1 == "Buyer":
            def rturnn(qbook,idbk):
                conn = sqlite3.connect('storage.db')
                c = conn.cursor()
                c.execute("SELECT * FROM book WHERE oid = " + str(idbk))
                records = c.fetchall()
                for record in records:
                    tqbook = record[5] # total quantity
                conn.commit()
                conn.close()

                tqall = int(qbook)+int(tqbook)

                conn = sqlite3.connect('storage.db')
                c = conn.cursor()
                returnbk = """UPDATE book SET quantity = ? WHERE oid = ?"""
                inputt = (str(tqall),str(idbk))
                c.execute(returnbk,inputt)
                conn.commit()
                conn.close()

            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM cart")
            records = c.fetchall()
            conn.commit()
            conn.close()
            for record in records:
                qbook = record[2] # quantity
                idbk = record[3] # book id
                rturnn(qbook,idbk)
        delete_pg.destroy()
        login_pg()

    def cencal():
        delete_pg.destroy()
        if type1 == "Administrator":
            administrator()
        else:
            buyer()

    Label(delete_pg,text= "Are You Sure To Delete This Account?").place(x=50, y=20)
    Label(delete_pg,text= "All Data Will Be Permanently Erased.").place(x=50, y=40)
    yes_btn = Button(delete_pg,text= "Yes", width=8, command= yes)
    yes_btn.place(x=50, y=70)
    cancel_btn = Button(delete_pg,text= "Cancel", width=8,command=cencal)
    cancel_btn.place(x=170, y=70)

def reload():
    addmoney =Tk()
    addmoney.title('BookshopUnity')
    addmoney.geometry("350x130")

    def savemoney():
        conn = sqlite3.connect('storage.db')
        c = conn.cursor()

        user_id = userid
        money1 = int(money) + int(moneybox.get())

        c.execute("""UPDATE User SET
                Username = :usernameA,
                Password = :passwordA,
                Name = :nameA,
                Age = :ageA,
                Email = :emailA,
                Phone = :phoneA,
                Type = :typeA,
                Money = :moneyA
                WHERE oid = :oid""",
                {
                'usernameA': username,
                'passwordA': password,
                'nameA': name,
                'ageA': age,
                'emailA': email,
                'phoneA': phone,
                'typeA': type1,
                'moneyA': money1,
                'oid' : user_id
                })
        conn.commit()
        conn.close()
        addmoney.destroy()
        buyer()

    def cnl():
        addmoney.destroy()
        buyer()

    Label(addmoney,text= "Amount To Reload?").place(x=80, y=20)
    Label(addmoney,text= "RM").place(x=80, y=50)
    moneybox = Entry(addmoney, width=10)
    moneybox.place(x=110,y=50)
    btn_1 = Button(addmoney,text= "Save", width=8,command=savemoney)
    btn_1.place(x=50, y=80)
    btn_2 = Button(addmoney,text= "Cancel", width=8, command=cnl)
    btn_2.place(x=170, y=80)

############################################# Registration Page ####################################################

def register ():
    register_pg =Tk()
    register_pg.title('BookshopUnity')
    register_pg.geometry("800x600")

    def save():
        conn = sqlite3.connect('storage.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM User")
        records = c.fetchall()
        if user_type2.get() == "Type of User":
            messagebox.showinfo("Error","Choose Type of User")

        elif username5a_label.get() == "" or password5a_label.get() == "" or name5a_label.get() == "" or age5a_label.get() == "" or phone5a_label.get() == "" or email5a_label.get() == "" :
            messagebox.showinfo("Error","Blank Not Allowed")

        else:
            for record in records:
                if username5a_label.get() == str(record[0]):
                    messagebox.showinfo("Error","Username Not Available. Change Username")
                    conn.commit()
                    conn.close()
                    register_pg.destroy()
                    goto(2)
                    break
            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            if user_type2.get() == "Administrator":
                c.execute("INSERT INTO User VALUES (:Username, :Password, :Name, :Age, :Email, :Phone, :Type, :Money)",
                        {
                            'Username': username5a_label.get(),
                            'Password': password5a_label.get(),
                            'Name': name5a_label.get(),
                            'Age': age5a_label.get(),
                            'Email': email5a_label.get(),
                            'Phone': phone5a_label.get(),
                            'Type': 'Administrator',
                            'Money': 0
                        })
            elif user_type2.get() == "Buyer":
                 c.execute("INSERT INTO User VALUES (:Username, :Password, :Name, :Age, :Email, :Phone, :Type, :Money)",
                        {
                            'Username': username5a_label.get(),
                            'Password': password5a_label.get(),
                            'Name': name5a_label.get(),
                            'Age': age5a_label.get(),
                            'Email': email5a_label.get(),
                            'Phone': phone5a_label.get(),
                            'Type': 'Buyer',
                            'Money': 0
                        })
            conn.commit()
            conn.close()
            register_pg.destroy()
            login_pg()

    Label(register_pg, text="Register New User", font= ("Arial Bold", 10)).place(x=220,y=40)

    # left
    Label(register_pg, text="Username : ").grid(row=0, column=0, padx=(100,0), pady=(100,0))
    Label(register_pg, text="Password : ").grid(row=1, column=0, padx=(100,0))
    Label(register_pg, text="Name : ").grid(row=2, column=0, padx=(100,0))
    Label(register_pg, text="Age : ").grid(row=3, column=0, padx=(100,0))
    Label(register_pg, text="Mobile Number : ").grid(row=4, column=0, padx=(100,0))
    Label(register_pg, text="Email : ").grid(row=5, column=0, padx=(100,0))

    global img2
    img2=PhotoImage(file='logo3.png')
    Label(register_pg,image=img2).place(x=440,y=100)

    # right
    username5a_label = Entry(register_pg, width=30)
    username5a_label.grid(row=0, column=1, padx=10, pady=(100,0))
    password5a_label = Entry(register_pg, width=30)
    password5a_label.grid(row=1, column=1)
    name5a_label = Entry(register_pg, width=30)
    name5a_label.grid(row=2, column=1)
    age5a_label = Entry(register_pg, width=30)
    age5a_label.grid(row=3, column=1)
    phone5a_label = Entry(register_pg, width=30)
    phone5a_label.grid(row=4, column=1)
    email5a_label = Entry(register_pg, width=30)
    email5a_label.grid(row=5, column=1)

    Label(register_pg, text=" ").grid(row=6, column=1)

    user_type2 = StringVar()
    user_type2.set("Type of User")
    type_list2 = OptionMenu(register_pg, user_type2, "Buyer", "Administrator")
    type_list2.grid(row=7, column=1)

    Label(register_pg, text=" ").grid(row=8, column=1)

    register_btn = Button(register_pg, text = "Register", width=10, command=save)
    register_btn.grid(row=9, column=1)
    cancel_btn = Button(register_pg, text="Cancel", width=10, command=lambda : [register_pg.destroy(),login_pg()])
    cancel_btn.grid(row=10, column=1)

############################################## Administrator Page ##################################################
def administrator():
    administrator1 =Tk()
    administrator1.title('BookshopUnity')
    administrator1.geometry("800x600")

    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS  cart (
            title text,
            price integer,
            quantity integer,
            bookid integer
            )""")
    conn.commit()
    conn.close()

    #left 1
    Label(administrator1, text="Username : ").place(x = 60,y = 20)
    Label(administrator1, text="Name : ").place(x = 81,y = 40)
    Label(administrator1, text="Age : ").place(x = 92,y = 60)

    #left 2
    username2b_label = Label(administrator1, text=username)
    username2b_label.place(x = 130,y = 20)
    name2b_label = Label(administrator1, text=name)
    name2b_label.place(x =130,y = 40)
    age2b_label = Label(administrator1, text=age)
    age2b_label.place(x = 130,y = 60)

    #right 1
    Label(administrator1, text="Password : ").place(x = 500,y = 20)
    Label(administrator1, text="Mobile Number : ").place(x = 466,y = 40)
    Label(administrator1, text="Email : ").place(x = 521,y = 60)

    #right 2
    password2b_label = Label(administrator1, text="****", )
    password2b_label.place(x = 567,y = 20)
    phone2b_label = Label(administrator1, text="+60 "+str(phone))
    phone2b_label.place(x = 567,y = 40)
    email2b_label = Label(administrator1, text=email)
    email2b_label.place(x = 567,y = 60)
    update2b_btn2 = Button(administrator1, text="Update Personal Info", command=lambda:[administrator1.destroy(), update_info()])
    update2b_btn2.place(x = 493,y = 80)
    delete2b_btn2 = Button(administrator1, text="Delete Account", command=lambda:[administrator1.destroy(), delete()])
    delete2b_btn2.place(x = 508,y = 110)

    ###########################################################################

    usertable = LabelFrame(administrator1)
    usertable.place(x=100,y=150)

    left = Label(usertable, text = "List Of User (Buyer)")
    left.pack()

    def View():
        conn = sqlite3.connect("storage.db")
        curr = conn.cursor()
        curr.execute("SELECT *, oid FROM User list")
        rows = curr.fetchall()    

        for row in rows:
            z= (row[8],row[2],row[4],row[5],)
            if row[6] == 'Buyer':
                tree.insert("", tk.END, values=z)

        conn.commit()
        conn.close()

    def select_user() :
        id_box2.delete(0,END)
        selected = tree.focus()
        selected_id = tree.item(selected,'values')
        if str(selected_id) == "":
            messagebox.showinfo("Error", "Please select ID")

        else:
            #Choose column 
            id_box2.insert(0, selected_id[0])

            buyerbook =Tk()
            buyerbook.title('BookshopUnity')
            buyerbook.geometry("370x255")

            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            c.execute("SELECT * FROM user WHERE oid = " + id_box2.get())
            records = c.fetchall()
            for q in records:
                nname = q[2]

            Label(buyerbook,text= "Name : "+ nname).place(x=80, y=20)
            Label(buyerbook,text= "Book Title ----- Quantity ").place(x=80, y=40)

            def close():
                buyerbook.destroy()

            close_bt = Button(buyerbook,text="Close", width= 8,command=close)
            close_bt.place(x=250, y=40)

            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM paid")
            qq =c.fetchall()

            ttlbook = ""
            for r in qq:
                if r[0] == nname:
                    book = r[1]
                    qtn = r[2]
                    z = book+"  ----  "+ str(qtn)+"    -Paid"
                    ttlbook += ("\n"+ z)

            if ttlbook == "":
                ttlbook = "User did not purchase any books"

            lbl = Label(buyerbook, text = ttlbook)
            lbl.place(x=80, y=60)
        


    tree_scroll = Scrollbar(usertable)
    tree_scroll.pack(fill="y", expand="yes", side =RIGHT)

    tree = ttk.Treeview(usertable,height=7,column=("c1","c2", "c3","c4"), show='headings',yscrollcommand=tree_scroll.set)

    tree.column("#1", anchor=tk.CENTER,width=30)
    tree.heading("#1", text="ID")

    tree.column("#2", anchor=tk.W,width=170)
    tree.heading("#2", text="Name")

    tree.column("#3", anchor=tk.CENTER,width=120,)
    tree.heading("#3", text="Email")

    tree.column("#4", anchor=tk.CENTER,width=120)
    tree.heading("#4", text="Phone Number")

    tree.pack()
    tree_scroll.config(command=tree.yview)
    View()

    ##########################################################################

    #left 3
    Label(administrator1, text = "ID : ").place(x=100,y=350)
    id_box2 = Entry(administrator1, width=10)
    id_box2.place(x=130,y=350)
    chck_btn2 = Button(administrator1, text="Check User",command=select_user)
    chck_btn2.place(x=130,y=370)

    viewbook_btn2 = Button(administrator1, text="Book Manager",command=lambda: [administrator1.destroy(),book_manager()])
    viewbook_btn2.place(x=130,y=400)

    #right 3
    logout_btn2 = Button(administrator1, text="Log Out", command=lambda : [administrator1.destroy(),login_pg()])
    logout_btn2.place(x=547,y=400)


############################################### Buyer's Homepage ###########################################################

def buyer():
    buyer1 = Tk()
    buyer1.title('BookshopUnity')
    buyer1.geometry("800x600")

    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS  cart (
            title text,
            price integer,
            quantity integer,
            bookid integer
            )""")
    conn.commit()
    conn.close()

    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute("SELECT * FROM User WHERE oid = " + userid)
    all = c.fetchall()

    for item in all:
        mny = item[7]

    #left 1
    Label(buyer1, text="Username : ").place(x = 60,y = 20)
    Label(buyer1, text="Name : ").place(x = 81,y = 40)
    Label(buyer1, text="Age : ").place(x = 92,y = 60)
    Label(buyer1, text="Balance : ").place(x = 72,y = 80)

    #left 2
    username1b_label = Label(buyer1, text=username)
    username1b_label.place(x = 130,y = 20)
    name1b_label = Label(buyer1, text=name)
    name1b_label.place(x =130,y = 40)
    age1b_label = Label(buyer1, text=age)
    age1b_label.place(x = 130,y = 60)
    balance1b_label = Label(buyer1, text="RM "+ str(mny))
    balance1b_label.place(x = 130,y = 80)
    reload_btn1 = Button(buyer1, text="Reload", command=lambda :[buyer1.destroy(),reload()])
    reload_btn1.place(x = 250,y = 80)

    #right 1
    Label(buyer1, text="Password : ").place(x = 500,y = 20)
    Label(buyer1, text="Mobile Number : ").place(x = 466,y = 40)
    Label(buyer1, text="Email : ").place(x = 521,y = 60)

    #right 2
    password1b_label = Label(buyer1, text="****",)
    password1b_label.place(x = 567,y = 20)
    phone1b_label = Label(buyer1, text="+60 "+str(phone))
    phone1b_label.place(x = 567,y = 40)
    email1b_label = Label(buyer1, text=email)
    email1b_label.place(x = 567,y = 60)
    update1b_btn1 = Button(buyer1, text="Update Personal Info", command=lambda:[buyer1.destroy(), update_info()])
    update1b_btn1.place(x = 493,y = 80)
    delete1b_btn1 = Button(buyer1, text="Delete Account", command=lambda:[buyer1.destroy(), delete()])
    delete1b_btn1.place(x = 508,y = 110)

    ########################################################### Cart ###############################################

    carttable = LabelFrame(buyer1)
    carttable.place(x=100,y=150)

    left = Label(carttable, text = "List Of Book (In Cart)")
    left.pack()

    def View():
        conn = sqlite3.connect("storage.db")
        curr = conn.cursor()
        curr.execute("SELECT *, oid FROM cart list")
        rows = curr.fetchall() 
        q = int()
        for row in rows:
            z= (row[4],row[0],row[1],row[2],)
            tree.insert("", tk.END, values=z)
            w =int(row[1])*int(row[2])
            q += w
        global totalprice
        totalprice = q

        conn.commit()
        conn.close()

    def cancelbook():
        selected = tree.focus()
        selected_id = tree.item(selected,'values')
        if str(selected_id) == "":
            messagebox.showinfo("Error", "Please select ID")

        else: 
            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            c.execute("SELECT * FROM cart WHERE oid = " + id_box1.get())
            records = c.fetchall()
            for record in records:
                qbook = record[2] # quantity
                idbk = record[3] # book id
            conn.commit()
            conn.close()

            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            c.execute("SELECT * FROM book WHERE oid = " + str(idbk))
            records = c.fetchall()
            for record in records:
                tqbook = record[5] # total quantity
            conn.commit()
            conn.close()

            tqall = int(qbook)+int(tqbook)

            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            returnbk = """UPDATE book SET quantity = ? WHERE oid = ?"""
            inputt = (str(tqall),str(idbk))
            c.execute(returnbk,inputt)
            conn.commit()
            conn.close()

            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            c.execute("DELETE from cart WHERE oid = " + id_box1.get())
            id_box1.delete(0, END)
            conn.commit()
            conn.close()
            buyer1.destroy()
            buyer()

    def select_book() :
        id_box1.delete(0,END)
        selected = tree.focus()
        selected_id = tree.item(selected,'values')
        if str(selected_id) == "":
            messagebox.showinfo("Error", "Please select ID")

        else:
            #Choose column 
            id_box1.insert(0, selected_id[0])

    tree_scroll = Scrollbar(carttable)
    tree_scroll.pack(fill="y", expand="yes", side =RIGHT)

    tree = ttk.Treeview(carttable,height=7,column=("c1","c2", "c3","c4"), show='headings',yscrollcommand=tree_scroll.set)

    tree.column("#1", anchor=tk.CENTER,width=40)
    tree.heading("#1", text="ID")

    tree.column("#2", anchor=tk.W,width=180)
    tree.heading("#2", text="Title")

    tree.column("#3", anchor=tk.CENTER,width=110,)
    tree.heading("#3", text="Price")

    tree.column("#4", anchor=tk.CENTER,width=110)
    tree.heading("#4", text="Quantity")

    tree.pack()
    tree_scroll.config(command=tree.yview)
    View()

    ######################################################################

    #left 3
    Label(buyer1, text = "ID : ").place(x=100,y=350)
    id_box1 = Entry(buyer1, width=10)
    id_box1.place(x=130,y=350)
    selectbook_btn = Button(buyer1, text="Select book",bg="lightgray",command=select_book)
    selectbook_btn.place(height=25,x=210,y=350)
    chck_btn1 = Button(buyer1, text="Delete Book In Cart", command=cancelbook)
    chck_btn1.place(x=130,y=380)
    viewbook_btn1 = Button(buyer1, text="Buy New Book", command=lambda : [buyer1.destroy(),buy_book()])
    viewbook_btn1.place(x=130,y=410)

    def logout():
        def rturnn(qbook,idbk):
            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            c.execute("SELECT * FROM book WHERE oid = " + str(idbk))
            records = c.fetchall()
            for record in records:
                tqbook = record[5] # total quantity
            conn.commit()
            conn.close()

            tqall = int(qbook)+int(tqbook)

            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            returnbk = """UPDATE book SET quantity = ? WHERE oid = ?"""
            inputt = (str(tqall),str(idbk))
            c.execute(returnbk,inputt)
            conn.commit()
            conn.close()

        conn = sqlite3.connect('storage.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM cart")
        records = c.fetchall()
        conn.commit()
        conn.close()
        for record in records:
            qbook = record[2] # quantity
            idbk = record[3] # book id
            rturnn(qbook,idbk)

        buyer1.destroy()
        login_pg()

    def paying():
        if int(totalprice) > int(mny) or int(totalprice) == 0:
            messagebox.showinfo("Error","Insufficient Balance. Please Reload Your Account/ No Item In Cart")

        else:
            bal = int(mny) - int(totalprice)
            user_id = userid
            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            c.execute("""UPDATE User SET
                    Username = :usernameA,
                    Password = :passwordA,
                    Name = :nameA,
                    Age = :ageA,
                    Email = :emailA,
                    Phone = :phoneA,
                    Type = :typeA,
                    Money = :moneyA
                    WHERE oid = :oid""",
                    {
                    'usernameA': username,
                    'passwordA': password,
                    'nameA': name,
                    'ageA': age,
                    'emailA': email,
                    'phoneA': phone,
                    'typeA': type1,
                    'moneyA': bal,
                    'oid' : user_id
                    })
            conn.commit()
            conn.close()

            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM cart")
            records = c.fetchall()
            
            global buyername
            buyername = name

            def insrt(x,y,z):
                conn = sqlite3.connect('storage.db')
                c = conn.cursor()
                c.execute("INSERT INTO paid (name, title, quantity) VALUES(?,?,?)",
                    (x,y,z))
                conn.commit()
                conn.close()

            for record in records:
                insrt(buyername,record[0],record[2])

            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            c.execute("DROP TABLE cart")
            conn.commit()
            conn.close()
            messagebox.showinfo("Done","Payment Successful")
            buyer1.destroy()
            buyer()

    #right 3
    Label(buyer1, text="Total : ").place(x=529,y=350)
    price_lbl = Label(buyer1, text="RM "+str(totalprice))
    price_lbl.place(x=567,y=350)
    pay_btn = Button(buyer1, text="Check Out/Pay",command=paying)
    pay_btn.place(x=540,y=370)
    logout_btn1 = Button(buyer1, text="Log Out", command=logout)
    logout_btn1.place(x=547,y=400)

def login_pg ():
    mainmenu = Tk()
    mainmenu.title('BookshopUnity')
    mainmenu.geometry("800x600")

    # Delete cart table
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute("DROP TABLE cart")
    conn.commit()
    conn.close()

    def toprofile ():
        conn = sqlite3.connect('storage.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM User")
        records = c.fetchall()

        # to show all user 
        # print(records)

        global username 
        global password 
        global name
        global age 
        global email 
        global phone 
        global type1
        global money 
        global userid

        if user_type1.get() == "Type of User":
            messagebox.showinfo("Error","Choose Type of User")

        elif user_type1.get() == "Administrator":
            if username4a_label.get() == "" or password4a_label.get() == "":
                messagebox.showinfo("Error","Blank Not Allowed")
            elif username4a_label.get() != "" or password4a_label.get() != "":
                for record in records:
                    username = record[0]
                    password = record[1]
                    name = record[2]
                    age = record[3]
                    email = record[4]
                    phone = record[5]
                    type1 = record[6]
                    money = record[7]
                    userid = record[8]
                    if username4a_label.get() == str(record[0]) and password4a_label.get() == str(record[1]) and str(record[6]) == 'Administrator':
                        mainmenu.destroy()
                        administrator()
                        break
                else:
                    messagebox.showinfo("Error", "Username or Password are wrong")

        elif user_type1.get() == "Buyer":
            if username4a_label.get() == "" or password4a_label.get() == "":
                messagebox.showinfo("Error","Blank Not Allowed")
            elif username4a_label.get() != "" or password4a_label.get() != "":
                for record in records:
                    username = record[0]
                    password = record[1]
                    name = record[2]
                    age = record[3]
                    email = record[4]
                    phone = record[5]
                    type1 = record[6]
                    money = record[7]
                    userid = str(record[8])
                    if username4a_label.get() == str(record[0]) and password4a_label.get() == str(record[1]) and str(record[6]) == 'Buyer':
                        mainmenu.destroy()
                        buyer()
                        break
                else:
                    messagebox.showinfo("Error", "Username or Password are wrong")

    def toregister():
        conn = sqlite3.connect('storage.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS  cart (
                title text,
                price integer,
                quantity integer,
                bookid integer
                )""")
        conn.commit()
        conn.close()
        mainmenu.destroy()
        register()
    Label(mainmenu, text="Welcome To", font= ("Monotype Corsiva", 20)).place(x=220,y=10)
    

    global img1
    img1=PhotoImage(file='logo2.png')
    Label(mainmenu,image=img1).place(x=200,y=50)

    Label(mainmenu, text="Username : ").place(x=280,y=360)
    Label(mainmenu, text="Password : ").place(x=280,y=390)

    username4a_label = Entry(mainmenu, width=30)
    username4a_label.place(x=370,y=360)
    password4a_label = Entry(mainmenu, width=30, show='*')
    password4a_label.place(x=370,y=390)

    user_type1 = StringVar()
    user_type1.set("Type of User")
    type_list1 = OptionMenu(mainmenu, user_type1, "Buyer", "Administrator")
    type_list1.place(x=366,y=415)

    login_btn = Button(mainmenu, text = "Login", width= 10, command=toprofile)
    login_btn.place(x=370,y=450)

    register_btn = Button(mainmenu, text = "Register Now", command=toregister)
    register_btn.place(x=370,y=500)

table()
login_pg()

mainloop()