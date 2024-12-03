from Project.server import *
from Project.pakages import *




class BillingSoftware(tk.Tk):

    def __init__(self, root):
        #server connection
        self.root = root
        self.root.geometry("1500x800")
        self.root.title("Billing Software")

        """VARIABLE DECLARATION"""
        self.enteredUserName = StringVar()
        self.enteredPassword = StringVar()
        self.current_frame = None
        
        self.acountdict = {'UserName':'Yogesh','PassWord':'yogi@123'}
        """ FRAMES INITIALIZATION"""

        self.init_frames_logInframe()
        # self.init_widges()
        
        
            

    def init_frames_logInframe(self):
        self.LogInFrame = tk.LabelFrame(self.root, text="Login", bg='light blue')
        self.LogInFrame.pack(fill="both", expand="yes", padx=500, pady=100)
        # LogInPage UI
        self.space = Label(self.LogInFrame, text='', padx=20, bg='light blue')
        self.space.grid(row=1, column=0, rowspan=4)

        self.welcomeLable = Label(self.LogInFrame, font=('arial', 25, 'bold', 'underline'), text="WELCOME TO LOG IN",
                                  bg='light blue', anchor="center")
        self.welcomeLable.grid(row=0, column=1, columnspan=3, padx=30, pady=50)
        # lable
        self.UserLable = Label(self.LogInFrame, font=('arial', 20, 'bold'), text="User Name", bg='light blue')
        self.UserLable.grid(row=1, column=1, padx=15, pady=10)

        self.PassWordLable = Label(self.LogInFrame, font=('arial', 20, 'bold'), text="PassWord", bg='light blue')
        self.PassWordLable.grid(row=3, column=1, padx=15, pady=10)
        # entry
        self.UserNameEntry = Entry(self.LogInFrame, font=('arial', 20, ''), textvariable=self.enteredUserName, width=20)
        self.UserNameEntry.grid(row=2, column=1, padx=50)

        self.PassWordEntry = Entry(self.LogInFrame, font=('arial', 20, ''), textvariable=self.enteredPassword, width=20)
        self.PassWordEntry.grid(row=4, column=1)

        # Loginbutton

        self.LogInButton = Button(self.LogInFrame, font=('arial', 15, ''), text='Log In', width=20,
                                  command=self.MainScreenTab)
        self.LogInButton.grid(row=5, column=1, pady=10)

    # sign up page entry lables
    def user_details(self, frame, lable_text, variable, row):
        label = Label(frame, font=('arial', 16, 'bold'), text=lable_text, bg='light blue')
        label.grid(row=row, column=0, pady=10, padx=20)
        # create Entry widget
        entry = Entry(frame, font=('arial', 20, 'bold'), textvariable=variable)
        entry.grid(row=row, column=1)

        # Main Screen tabs Button

    def MainScreentapsCreation(self, root, text, command, column):
        self.TabButton = Button(root, font=('arial', 10, ''), text=text, command=command)
        self.TabButton.grid(row=0, column=column, padx=5)

    """ALL COMMAND FUNCTIONS"""

    def SignUpConfirm(self):
        self.SignupFrame.destroy()
        self.init_frames_logInframe()

    def MainScreenTab(self):
        username = self.enteredUserName.get()
        password = self.enteredPassword.get()
        if self.acountdict['UserName']==username and self.acountdict['PassWord']==password:
            self.LogInFrame.destroy()
            self.TabFrames = Frame(self.root)
            self.TabFrames.pack()
            self.MainScreentapsCreation(self.TabFrames, "Home", self.show_home_screen, 0)
            self.MainScreentapsCreation(self.TabFrames, "Product", self.show_Product_screen, 1)
            self.MainScreentapsCreation(self.TabFrames, "Customer Details", self.show_purchase_details_screen, 2)
            self.MainScreentapsCreation(self.TabFrames, "Sales Chart", self.show_chart_screen, 3)
            self.MainScreentapsCreation(self.TabFrames, "Exit", self.exit, 4)

            self.HomeScreenFrame = Frame(root, bg="light blue")
            self.HomeScreenFrame.pack(side=TOP)
            self.screen = HomeScreen(self.HomeScreenFrame)

            self.ProductScreenFrame = Frame(root, bg="light blue")
            self.ProductScreenFrame.pack(side=TOP)
            self.screen = Product_screen(self.ProductScreenFrame)

            self.PurchseScreenFrame = Frame(root, bg="light blue")
            self.PurchseScreenFrame.pack(side=TOP)
            self.screen = PurchaseDetailsScreenView(self.PurchseScreenFrame)
            
            self.saleschartFrame = Frame(root,bg='light blue')
            self.saleschartFrame.pack(side=TOP)
            self.screen = salesChart_screen(self.saleschartFrame)
            self.show_home_screen()
        elif self.acountdict['UserName']==username and self.acountdict['PassWord']!=password:
            if messagebox.showerror('Password incorect','Enter corect Password'):
                self.enteredPassword.set('')
                self.enteredUserName.set('')
        elif self.acountdict['UserName']!=username and self.acountdict['PassWord']==password:
            if messagebox.showerror('Username incorect','Enter corect UserName'):
                self.enteredPassword.set('')
                self.enteredUserName.set('')
        elif self.acountdict['UserName']!=username and self.acountdict['PassWord']!=password:
            if messagebox.showerror('Username and Password incorect','Enter corect UserName and Password'):
                self.enteredPassword.set('')
                self.enteredUserName.set('')       
        else:
            pass
                
       

    def show_home_screen(self):
        self.PurchseScreenFrame.pack_forget()
        self.ProductScreenFrame.pack_forget()
        self.HomeScreenFrame.pack()
        self.saleschartFrame.pack_forget()

    def show_Product_screen(self):
        self.PurchseScreenFrame.pack_forget()
        self.HomeScreenFrame.pack_forget()
        self.ProductScreenFrame.pack()
        self.saleschartFrame.pack_forget()

    def show_purchase_details_screen(self):
        self.ProductScreenFrame.pack_forget()
        self.HomeScreenFrame.pack_forget()
        self.PurchseScreenFrame.pack()
        self.saleschartFrame.pack_forget()
    def show_chart_screen(self):
        self.saleschartFrame.pack()
        self.HomeScreenFrame.pack_forget()
        self.ProductScreenFrame.pack_forget()
        self.PurchseScreenFrame.pack_forget()

    def exit(self):
        conn.commit()
        root.destroy()


class HomeScreen(tk.Frame):
    def __init__(self, master):
        
        
        # Home Screen Variables
        self.a=0
       
        self.Customer_Name = StringVar(value='')
        self.Customer_number = StringVar(value='')
        query = 'select bill_no from customerdeatails'
        cursor.execute(query)
        rows = cursor.fetchall()
        counts = len(rows)
        
        self.bill_next = 1001+counts
        self.Product_name = StringVar()
        self.Product_qtys = IntVar(value='')
        self.Bill_Number = StringVar(value=f'B_S_{self.bill_next}')

        self.Total = IntVar()
        self.discount = StringVar()
        self.NetPay = IntVar()
        
        self.curentdate=datetime.date.today()
               
        
        query = "SELECT ProductName FROM ProductDetails"
        cursor.execute(query)
        rows = cursor.fetchall()

        self.cleaned_datas=[]
        for row in rows:
            self.Our_products =row[0]
            self.cleaned_item = self.Our_products.replace("(", "").replace(")", "").replace(",", "").replace("'", "")
            self.cleaned_datas.append(self.cleaned_item)
        
        
        # Frame declaration
        self.Bill_Product = tk.LabelFrame(master, text="Bill Product", bg='light blue')
        self.Bill_Product.pack(fill="both", expand="yes", padx=10, pady=10)

        self.Customer_details = tk.LabelFrame(master, text="Customer_details", bg='light blue')
        self.Customer_details.pack(fill="both", expand="yes", padx=10)
        
        self.Total_frame = Frame(master,bg="light blue",bd =1,relief=tk.SUNKEN)
        self.Total_frame.pack(fill="both",expand="yes",padx=10,pady=10)
        
        self.Purchase_display = tk.Frame(master, bg='light blue', bd=1, relief=tk.SUNKEN,width=1500,height=500)
        self.Purchase_display.pack(side=TOP, padx=10, pady=10)
        
        self.bill_lable = Treeview(self.Purchase_display,columns=(1,2,3,4,5,6),show="headings",height=20)
        self.bill_lable.pack(side='left',fill="both")
        
        self.bill_lable.heading(1,text="Product Code")
        self.bill_lable.heading(2,text="Product Name")
        self.bill_lable.heading(3,text="Product Price")
        self.bill_lable.heading(4,text="Product Quantity")
        self.bill_lable.heading(5,text="Total Price")
        self.bill_lable.heading(6,text="Store Stock")
        
        self.scrollbar = Scrollbar(self.Purchase_display,orient='vertical',command=self.bill_lable.yview)
        self.bill_lable.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='left',fill='y')
        

        # lable entry declaration
        self.create_lable_home_screen(self.Customer_details, 'Customer Name  :', self.Customer_Name, 0, 1)
        
        self.create_lable_home_screen(self.Customer_details, 'Customer_mobile  :', self.Customer_number, 2, 3)
        self.create_lable_home_screen(self.Customer_details, 'Bill_Number  :', self.Bill_Number, 4, 5)

        # Product purchase Entry Declaration
        
        self.create_lable_home_screen(self.Total_frame,'Total :', self.Total, 0, 1)
        self.create_lable_home_screen(self.Total_frame, 'Discount % :', self.discount, 2,3)
        self.create_lable_home_screen(self.Total_frame, 'Net Pay  :', self.NetPay, 4, 5)

        self.Lables = Label(self.Bill_Product, font=('arial', 15, ''), text="Product", height=2, bg='light blue')
        self.Lables.grid(row=0, column=0, padx=10)

        self.Product_entry = Entry(self.Bill_Product, font=('arial', 15, ''), textvariable=self.Product_name)
        self.Product_entry.grid(row=0, column=2, padx=10,pady=0)
        
        self.listsbox = Listbox(self.Bill_Product,height=4,font=('Times',15,'bold'),relief='flat',bg='light blue',highlightbackground='light blue')
        self.listsbox.grid(row=1,column=2,pady=0)
        self.listsbox.grid_forget()
        self.Product_name.trace('w',self.getdata)
        self.Product_entry.bind("<Down>",self.my_down)
        self.Product_entry.bind("<Right>",self.change_focus)
        self.Product_entry.bind("<Return>",self.call_fun1)
        self.listsbox.bind("<Return>",self.my_update)

        
        self.Lables1 = Label(self.Bill_Product, font=('arial', 15, ''), text="Quantity  :", height=2, bg='light blue')
        self.Lables1.grid(row=0, column=3, padx=10)

        self.Product_qty = Entry(self.Bill_Product, font=('arial', 15, ''), textvariable=self.Product_qtys)
        self.Product_qty.grid(row=0, column=4, padx=10)
        self.Product_qty.bind("<Return>",self.call_fun)

        self.Next_btn_Prt = Button(self.Bill_Product, font=('arial', 15, ''), text='Next', width=15, command=self.Next_Product)
        self.Next_btn_Prt.grid(row=0, column=5, padx=40)
        self.Enter_btn_Prt = Button(self.Bill_Product, font=('arial', 15, ''), text='Enter', width=15, command=self.finished_bill)
        self.Enter_btn_Prt.grid(row=0, column=6, padx=20)
        
        
    def getdata(self,*args):
        search_str = self.Product_name.get()
        if search_str=='':
            self.listsbox.delete(0,END)
            self.listsbox.grid_forget()
        else:
            self.listsbox.delete(0,END)
            for element in self.cleaned_datas:
                if (re.match(search_str,element,re.IGNORECASE)):
                    self.listsbox.insert(tk.END,element)
            self.listsbox.grid(row=1,column=2)
    def my_update(self,my_widget):
        self.my_w = my_widget.widget
        self.index = int(self.my_w.curselection()[0])
        self.value = self.my_w.get(self.index)
        self.Product_name.set(self.value)
        self.listsbox.delete(0,END) 
        self.listsbox.grid_forget()
        self.Product_entry.focus()     
    def change_focus(self,event):     
        self.Product_qty.focus_set()
    # Home Screen Lable Function  
    def my_down(self,event=None):
        self.listsbox.focus()
        self.listsbox.selection_set(0)
           
    def create_lable_home_screen(self, frame, text, text_variable, column1, colum2):
        self.Lables = Label(frame, font=('arial', 15, ''), text=text, height=2, bg='light blue')
        self.Lables.grid(row=0, column=column1, padx=10)

        self.Entrys = Entry(frame, font=('arial', 15, ''), textvariable=text_variable)
        self.Entrys.grid(row=0, column=colum2, padx=10)
    def call_fun(self,event):
        self.Next_Product() 
    def call_fun1(self,event):
        try:
            temp_pr=self.Product_name.get()
            temp_qt=self.Product_qtys.get()
        except Exception:
            temp_qt=0
        if temp_pr=='' and temp_qt==0:
            self.finished_bill()
        else:
            self.Next_Product(self)
    def Next_Product(self):
        
        product_name = self.Product_name.get().lower()
        quantity = int(self.Product_qtys.get())
        queryP_section = "SELECT Productcode, ProductName, ProductPrice, ProductStock FROM ProductDetails WHERE ProductName=?"
        cursor.execute(queryP_section,(product_name))
        products = cursor.fetchone()
        
        
        temp_p_code = products.Productcode
        temp_p_name = str(products.ProductName)
        temp_p_price =int( products.ProductPrice)
        temp_p_stock = products.ProductStock
        total_price = temp_p_price*quantity
        new_stock = temp_p_stock - quantity
        
        insert_query = """INSERT INTO Customer_Bill VALUES(?, ?, ?, ?, ?, ?)"""
        cursor.execute(insert_query,(temp_p_code,temp_p_name,temp_p_price,quantity,total_price,new_stock))
        update_query = """UPDATE ProductDetails
                        SET ProductStock =?
                        WHERE Productcode=?"""
        cursor.execute(update_query,(new_stock,temp_p_code))
        query = "SELECT * FROM Customer_Bill"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.display_bill(rows)
        self.Product_name.set('')
        self.Product_qtys.set('')
        self.totalCal(total_price) 
        self.Product_entry.focus_set() 
         
        try:
            if self.temp_total>2000:
                temp_discounts = 20
                self.discount.set(f"{temp_discounts}%") 
            elif 2000>=self.temp_total>1500:
                temp_discounts = 15
                self.discount.set(f"{temp_discounts}%") 
            elif 1500>=self.temp_total>1000:
                temp_discounts = 10
                self.discount.set(f"{temp_discounts}%") 
            elif 1000>=self.temp_total>500:
                temp_discounts = 5
                self.discount.set(f"{temp_discounts}%")     
                
            else:
                temp_discounts = 0
                self.discount.set(f"{temp_discounts}%")  
                self.a=0 
            self.temp_less = (self.temp_total*temp_discounts)/100
            self.temp_netpay = self.temp_total - self.temp_less
            self.NetPay.set(self.temp_netpay) 
        except Exception:
            pass 
        self.popup(new_stock)  
    def popup(self,stock):
        if stock<=5:
            messagebox.showwarning('WARNING','Product Reached Minimun Quantity !!!')
                          
    def display_bill(self,rows):
        self.bill_lable.delete(*self.bill_lable.get_children())
        for i in rows:
            lists = list(i)
            self.bill_lable.insert('','end',values=lists)

    def totalCal(self,total):
        self.temp_total = self.Total.get()
        self.temp_total = self.temp_total + total
        self.Total.set(self.temp_total)       
    
    def finished_bill(self):
        self.bill_lable.delete(*self.bill_lable.get_children())

        self.bill_screen_view()
        self.bill_save()
        
    def bill_save(self):
        bill_number = self.Bill_Number.get()  # assuming bill_number is a StringVar
        customer_name = self.Customer_Name.get() # assuming Customer_Name is a StringVar
        if not customer_name:
            customer_name="**********"
        customer_number = self.Customer_number.get() # assuming Customer_number is a StringVar
        if not customer_number:
            customer_number="##########"
        product_count = self.counts  # assuming counts is a StringVar or an integer
        discount = self.temp_less # assuming temp_less is a StringVar or an integer
        netpay = self.temp_netpay
        total = self.temp_total
        #date = self.curentdate.strftime('%Y-%m-%d')
        query = 'INSERT INTO CustomerDeatails (Bill_no, Customer_name, Customer_number, Bill_date, Products_count,total, Discount, NetPay) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        cursor.execute(query, (bill_number, customer_name, customer_number, self.curentdate, product_count,total, discount, netpay))    
        #print(self.old_bill)
        
    def bill_screen_view(self):
        
        self.newroot = Tk()
        self.newroot.geometry("500x600")
        self.newroot.title("Bill Display")
        
        self.font = ('courier',10,'')
        self.bill_number = self.Bill_Number.get()
        self.c_name = self.Customer_Name.get()
        self.c_number = self.Customer_number.get()


        # Optionally set the window to be non-resizable
        self.newroot.resizable(False, False)

        # Bill Title Label
        self.bill_title1 = Label(self.newroot, bg='light gray', font=('courier', 20, 'bold'), text="Bill Area")
        self.bill_title1.pack(side=TOP, padx=10, pady=10, fill='x')  # Fill horizontally

        # Bill Body Frame
        self.Bill_body = Frame(self.newroot)
        self.Bill_body.pack(side=TOP, padx=10, pady=10, fill='both', expand=True)

        # Text widget for the bill content
        self.bill_text = Text(self.Bill_body, font=('courier', 10, ''), wrap='word')
        self.bill_text.pack(side=LEFT, fill='both', expand=True)  # Expanding and filling the available space

        # Scrollbar for the text widget
        self.scrollbar = Scrollbar(self.Bill_body, orient='vertical', command=self.bill_text.yview)
        self.bill_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y') 
        
        query = "SELECT ProductName, ProductPrice,productQuantity,TotalPrice FROM Customer_Bill"
        cursor.execute(query)
        products = cursor.fetchall()
        self.l=[]
        self.counts=0
        for i in products:
            m=[]
            for j in i:
                m.append(j)
            self.l.append(m)
            self.counts+=1
        self.bill_func()
        self.pdf_save()
        self.bill_text.config(state=tk.DISABLED)
        self.discount.set('')
        self.NetPay.set('') 
        self.Total.set(0)
        self.bill_next+=1
        self.next_number = f'B_S_{self.bill_next}'
        self.Bill_Number.set(self.next_number)
        
    def pdf_save(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('courier','',10)
        pdf.write(4,"hi")
        self.loc = f"D:\\Project\\BillingSoftware\\ourbills\\{self.Bill_Number.get()}_{datetime.date.today()}.pdf"
        pdf.write(4,"\n\t                **  Welocme to my store  **\n")
        pdf.write(4,f"\n   Bill number : {self.bill_number}\n")
        pdf.write(4,f"   customer name : {self.c_name}\n")
        pdf.write(4,f"   Customer number : {self.c_number}\n")
        pdf.write(4,f" {'-'*58}\n")
        pdf.write(4,f"   {'S.No':<5}{'Product':<15} {'Unit_Price':<12} {'Quantity':<12} {'Total'}\n")
        pdf.write(4,f" {'-'*58}\n")
        for index ,item in enumerate(self.l,start=1):
            pdf.write(4,f"   {index:<5}{item[0][:15]:<15} {item[1]:<12} {item[2]:<12} {item[3]}\n")
        pdf.write(4,f" {'-'*58}\n")
        pdf.write(4,f"   Total Amount :                                {self.temp_total} Rs\n")
        pdf.write(4,f"   Discount Amount :                             {self.temp_less} Rs\n")
        pdf.write(4,f"   Total Amount you Paid :                       {self.temp_netpay} Rs\n")
        pdf.write(4,f" {'-'*58}\n")
        pdf.write(4,"\n            **  Thangs For Purchasing our shop  **\n")
        pdf.output(self.loc)
        
    def bill_func(self):
        
        self.bill_text.insert(tk.END,"\n\t\t**  Welocme to my store  **\n")
        self.bill_text.insert(tk.END,f"\n   Bill number : {self.bill_number}\n")
        self.bill_text.insert(tk.END,f"   customer name : {self.c_name}\n")
        self.bill_text.insert(tk.END,f"   Customer number : {self.c_number}\n")
        self.bill_text.insert(tk.END,f" {'-'*58}\n")
        self.bill_text.insert(tk.END,f"   {'S.No':<5}{'Product':<15} {'Unit_Price':<12} {'Quantity':<12} {'Total'}\n")
        self.bill_text.insert(tk.END,f" {'-' * 58}\n")
        for index ,item in enumerate(self.l,start=1):
            self.bill_text.insert(tk.END,f"   {index:<5}{item[0][:15]:<15} {item[1]:<12} {item[2]:<12} {item[3]}\n")
        self.bill_text.insert(tk.END,f" {'-' * 58}\n")
        self.bill_text.insert(tk.END,f"   Total Amount :                             Rs.{self.temp_total:.2f} \n")
        self.bill_text.insert(tk.END,f"   Discount Amount :                          Rs.{self.temp_less:.2f} \n")
        self.bill_text.insert(tk.END,f"   Total Amount you Paid :                    Rs.{self.temp_netpay:.2f} \n")
        self.bill_text.insert(tk.END,f" {'-' * 58}\n")
        self.bill_text.insert(tk.END,"\n\t    **  Thangs For Purchasing our shop  **\n")
        query = 'DELETE FROM Customer_Bill'
        cursor.execute(query)
        return self.bill_text

        
class Product_screen(tk.Frame):
    def __init__(self, master):
        self.P_search = StringVar()
        self.P_Code = StringVar()
        self.P_Dep = StringVar()
        self.P_Name = StringVar()
        self.P_Price = StringVar()
        self.P_Stock = StringVar()
        
        self.Product_list_frame = LabelFrame(master, text="Product Screen")
        self.Product_list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.temp_frame = Frame(self.Product_list_frame)
        self.temp_frame.pack(side=TOP,fill='both',expand=True)

        self.Product_view = Treeview(self.temp_frame, columns=(1, 2, 3, 4, 5), show="headings", height="15")
        self.Product_view.pack(side="left", fill="both", expand=True)
        
        self.Product_search_frame = LabelFrame(master, text="Search", height=20)
        self.Product_search_frame.pack(fill='x', padx=20, pady=10)

        self.Product_modification_frame = LabelFrame(master, text="Product Data")
        self.Product_modification_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.Product_view.heading(1, text="Product Code")
        self.Product_view.heading(2, text="Product Department")
        self.Product_view.heading(3, text="Product Name")
        self.Product_view.heading(4, text="Product Price")
        self.Product_view.heading(5, text="Product Stock")
        
       
        
        self.scrollbar = Scrollbar(self.temp_frame,orient='vertical',command=self.Product_view.yview)
        self.Product_view.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right',fill='y')

        # search section
        self.lable1 = Label(self.Product_search_frame, font=('', 10, 'bold'), text="    ")
        self.lable1.pack(side=LEFT, padx=30, pady=20)

        self.lable1 = Label(self.Product_search_frame, font=('', 10, 'bold'), text="Search")
        self.lable1.pack(side=LEFT, padx=10, pady=20)

        self.entry1 = Entry(self.Product_search_frame, font=('', 10, 'bold'), textvariable=self.P_search, width=20)
        self.entry1.pack(side=LEFT, padx=6, pady=20)

        self.btn = Button(self.Product_search_frame, text="Search", command=self.search_Fun)
        self.btn.pack(side=LEFT, padx=6, pady=20)

        self.btn = Button(self.Product_search_frame, text="clear", command=self.clear_search)
        self.btn.pack(side=LEFT, padx=6, pady=20)

        self.btn = Button(self.Product_search_frame, text="Refresh", command=self.clear_search)
        self.btn.pack(side=LEFT, padx=6, pady=20)

        # Product Input Section
        self.Product_input_creation(self.Product_modification_frame, "product Code", self.P_Code, 0)
        self.Product_input_creation(self.Product_modification_frame, "product Departmet", self.P_Dep, 1)
        self.Product_input_creation(self.Product_modification_frame, "product Name", self.P_Name, 2)
        self.Product_input_creation(self.Product_modification_frame, "product Price", self.P_Price, 3)
        self.Product_input_creation(self.Product_modification_frame, "product Stock", self.P_Stock, 4)

        self.Update_btn = Button(self.Product_modification_frame, text="Update", command=self.update)
        self.Update_btn.grid(row=5, column=0, padx=10, pady=10)

        self.add_btn = Button(self.Product_modification_frame, text="Change", command=self.change_product)
        self.add_btn.grid(row=5, column=1, pady=10)

        self.Delete_btn = Button(self.Product_modification_frame, text="Delete", command=self.delete_product)
        self.Delete_btn.grid(row=5, column=2, padx=10, pady=10)
        #server connection codes
        query = "SELECT Productcode, ProductDepartment, ProductName, ProductPrice, ProductStock FROM ProductDetails"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.rowsdisplay(rows)
        
    #button function declaration
    def search_Fun(self):
        self.Pr_search = self.P_search.get()
        query = " SELECT productcode, ProductDepartment, ProductName, ProductPrice, ProductStock FROM  ProductDetails WHERE Productcode LIKE ? or  ProductDepartment LIKE ? or ProductName LIKE ?"
        cursor.execute(query,('%'+self.Pr_search+'%','%'+self.Pr_search+'%','%'+self.Pr_search+'%'))
        rows = cursor.fetchall()
        self.rowsdisplay(rows)
        self.P_search.set('')
        
    def clear_search(self):
        query="SELECT * FROM ProductDetails"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.rowsdisplay(rows)
    def rowsdisplay(self,rows):
        self.Product_view.delete(*self.Product_view.get_children())
        for i in rows:
            lists = list(i)
            self.Product_view.insert('','end',values=lists)
            
    def adding_process(self):
        query = "SELECT * FROM ProductDetails"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.commit()
        self.rowsdisplay(rows)
        
    def update (self):
        self.pr_code = self.P_Code.get()
        self.pr_dep = self.P_Dep.get()
        self.pr_name = self.P_Name.get()
        self.pr_price = self.P_Price.get()
        self.pr_stock = self.P_Stock.get()
        
        if self.pr_code and self.pr_dep and self.pr_name and self.pr_price and self.pr_stock:
            query = 'INSERT INTO ProductDetails VALUES(?, ?, ?, ?, ?)'
            cursor.execute(query,(self.pr_code,self.pr_dep,self.pr_name,self.pr_price,self.pr_stock))
            self.adding_process()
        else:
            messagebox.showwarning("Input Error",message="Check All fields are Filled")
        self.emptyEntrySet()    
    def change_product(self):
        self.pr_code = self.P_Code.get()
        self.ident = self.P_Code.get()
        self.pr_dep = self.P_Dep.get()
        self.pr_name = self.P_Name.get()
        self.pr_price = self.P_Price.get()
        self.pr_stock = self.P_Stock.get()
        if messagebox.askyesno("ConfirmPlease",message="Are you sure want to change product Deatils"):
            query = """
            UPDATE ProductDetails
            SET Productcode = ?, ProductDepartment =?, ProductName =?, ProductPrice =?, ProductStock=? 
            WHERE Productcode = ?
            """
            cursor.execute(query,(self.pr_code,self.pr_dep,self.pr_name,self.pr_price,self.pr_stock,self.ident))
            self.adding_process()
            self.emptyEntrySet()
            
    def delete_product(self):
        self.Product_Code = self.P_Code.get()
        if messagebox.askyesno("ConfirmPlease",message="Are you sure want to DELETE product Deatils"):
            query = "DELETE FROM ProductDetails WHERE Productcode = ?"
            cursor.execute(query,(self.Product_Code))
            self.adding_process()
            self.emptyEntrySet()
            
            
    def emptyEntrySet(self):
        self.P_Code.set('')
        self.P_Dep.set('')
        self.P_Name.set('')
        self.P_Price.set('')
        self.P_Stock.set('')
        
    def Product_input_creation(self, frame, text, variable, row):
        self.lable1 = Label(frame, font=('', 10, 'bold'), text=text)
        self.lable1.grid(row=row, column=0, padx=10, pady=5)
        self.entry2 = Entry(frame, font=('', 10, 'bold'), textvariable=variable, width=20)
        self.entry2.grid(row=row, column=1)


class PurchaseDetailsScreenView(tk.Frame):
    def __init__(self, master):
        
        self.total_profit = IntVar()
        self.year = IntVar(value='')
        self.month = IntVar(value='')
        self.date = IntVar(value='')
        self.purchase_frame = LabelFrame(master, text="Customer Purchase Details")
        self.purchase_frame.pack(fill="both", expand="yes", padx=10, pady=10)
        
        self.bottom_frame = Frame(master,bg='light blue')
        self.bottom_frame.pack()
        
        self.customer_details = Treeview(self.purchase_frame, columns=(1, 2, 3, 4, 5, 6, 7), show="headings",height=30)
        self.customer_details.pack(side='left',fill="both", expand="yes")

        self.customer_details.heading(1, text="Bill No")
        self.customer_details.heading(2, text="Customer Name")
        self.customer_details.heading(3, text="Customer Number")
        self.customer_details.heading(4, text="Products Count")
        self.customer_details.heading(5, text="Total")
        self.customer_details.heading(6, text="Discounts")
        self.customer_details.heading(7, text="Net Pay")
        
        
        self.scrollbar = Scrollbar(self.purchase_frame, orient="vertical", command=self.customer_details.yview)
        self.customer_details.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="left", fill="y")
        
        self.lable = Label(self.bottom_frame,text=f'Year\tMonth\tDate')
        self.lable.grid(row=0,column=0,padx=0,columnspan=3)
        self.lable1 = Label(self.bottom_frame,text=f'Profit')
        self.lable1.grid(row=0,column=7,padx=0)
        self.ref_ent1 = Entry(self.bottom_frame,font=('courier',20,'bold'),textvariable=self.year,width=5)
        self.ref_ent1.grid(row=1,column=0,pady=20)
        self.ref_ent2 = Entry(self.bottom_frame,font=('courier',20,'bold'),textvariable=self.month,width=5)
        self.ref_ent2.grid(row=1,column=1,pady=20)
        self.ref_ent3 = Entry(self.bottom_frame,font=('courier',20,'bold'),textvariable=self.date,width=5)
        self.ref_ent3.grid(row=1,column=2,pady=20)
        self.ref_btn1 = Button(self.bottom_frame,text='Filter',command=self.filter,width=10,height=2)
        self.ref_btn1.grid(row=1,column= 3,padx=5)
        self.space = Label(self.bottom_frame,text='',bg='light blue')
        self.space.grid(row=1,column=4,padx=150)
        self.ref_btn = Button(self.bottom_frame,text='Refresh',command=self.refresh)
        self.ref_btn.grid(row=1,column= 5)
        self.space = Label(self.bottom_frame,text='',bg='light blue')
        self.space.grid(row=1,column=6,padx=200)
        self.ref_ent = Entry(self.bottom_frame,font=('courier',20,'bold'),textvariable=self.total_profit,width=10)
        self.ref_ent.grid(row=1,column=7,pady=20)
        query = "select Bill_no, Customer_name, Customer_number, Products_count,total, Discount, NetPay from CustomerDeatails "
        cursor.execute(query)
        self.rows = cursor.fetchall()
        self.display_deatails(self.rows)
    def display_deatails(self,rows):
        self.customer_details.delete(*self.customer_details.get_children())
        for i in rows:
            lists = list(i)
            self.customer_details.insert('','end',values=lists)
        self.profit_shown()
    def refresh(self): 
        query = 'select Bill_no, Customer_name, Customer_number, Products_count,total, Discount, NetPay from CustomerDeatails '
        cursor.execute(query)
        self.rows = cursor.fetchall()
        self.display_deatails(self.rows)
        
    def profit_shown(self):
        query="select sum(NetPay) from CustomerDeatails" 
        cursor.execute(query)  
        rows = cursor.fetchone()
        newrow = str(rows)
        profit = newrow.replace("(", "").replace(")", "").replace(",", "").replace("'", "").replace("Decimal","")
        self.total_profit.set(profit)
        
    def filter(self):
        
        date = f'{self.year.get()}-{self.month.get()}-{self.date.get()}'
        query = 'select Bill_no, Customer_name, Customer_number, Products_count,total, Discount, NetPay from CustomerDeatails where bill_date=?'
        cursor.execute(query,(date))
        self.rows = cursor.fetchall()
        self.display_deatails(self.rows)
        query="select sum(NetPay) from CustomerDeatails where bill_date=?" 
        cursor.execute(query,(date))  
        rows = cursor.fetchone()
        newrow = str(rows)
        profit = newrow.replace("(", "").replace(")", "").replace(",", "").replace("'", "").replace("Decimal","")
        self.total_profit.set(profit)
        
class salesChart_screen(tk.Frame):
    def __init__(self,master):
        self.plotframe_date = Frame(master)
        self.plotframe_date.pack(side=LEFT,fill=tk.BOTH,expand=True)
        self.plotframe_month = Frame(master)
        self.plotframe_month.pack(side=LEFT,fill=tk.BOTH,expand=True)
        self.plotframe_week = Frame(master)
        self.plotframe_week.pack(side=LEFT,fill=tk.BOTH,expand=True)
        
        self.date_data = Text(self.plotframe_date, font=('courier', 15, ''),width=100, wrap='word')
        self.date_data.grid(row=1,column=0)
        self.week_data = Text(self.plotframe_week, font=('courier', 15, ''),width=100, wrap='word')
        self.week_data.grid(row=1,column=0)
        self.month_data = Text(self.plotframe_month, font=('courier', 15, ''),width=100, wrap='word')
        self.month_data.grid(row=1,column=0)
        
        
        self.butonframes = Frame(master)
        self.butonframes.pack(side=RIGHT,fill=tk.BOTH,expand=True)
        
        buton = Button(self.butonframes,text='Daily sales',width=20,command= self.plot_switch_date)
        buton.grid(row=0,column=0)
        buton1 = Button(self.butonframes,text='Weekly sales',width=20,command=self.plot_switch_week)
        buton1.grid(row=1,column=0)
        buton2 = Button(self.butonframes,text='Monthly sales',width=20,command=self.plot_switch_month)
        buton2.grid(row=2,column=0)
        
        
        
        
        fig = self.create_plot_date()
        fig1 = self.create_plot_weekly()
        fig2 = self.create_plot_month()
        
        canvas = FigureCanvasTkAgg(fig,master=self.plotframe_date)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0,column=0,sticky='nsew')
        
        canvas = FigureCanvasTkAgg(fig1,master=self.plotframe_week)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0,column=0,sticky='nsew')
             
        canvas = FigureCanvasTkAgg(fig2,master=self.plotframe_month)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0,column=0,sticky='nsew')
        
        self.plot_switch_date()
    def plot_data(self,value):
        if value==2:
            query = """SELECT 
                        YEAR(bill_date) AS Year,
                        CONCAT(DAY(bill_date), '-', MONTH(bill_date)) AS DayMonth,
                        SUM(netpay) AS TotalNetPay,
                        COUNT(Bill_no) AS Total_No,
                        SUM(Products_count) AS Total_Sold
                    FROM CustomerDeatails
                    WHERE bill_date >= DATEADD(DAY, -4, GETDATE())
                    GROUP BY 
                        YEAR(bill_date),
                        DAY(bill_date),
                        MONTH(bill_date)
                    ORDER BY 
                        TotalNetPay DESC;"""
            cursor.execute(query)
            self.rows = cursor.fetchall() 
            self.rows=self.rows[:4]
            self.text_entry(self.date_data,'Day')
                       
        elif value==3:
            query = """select 
	                year(bill_date) as year,
	                datepart(week,bill_date) as weeknumber,
	                sum(netpay) as TotalNetPay,
                    count(Bill_no) as total_no,
                    sum(Products_count) as total_sold
                    from CustomerDeatails
                    group by
	                year(bill_date),
	                datepart(week,bill_date)
                    order by 
	                TotalNetPay desc"""
            
            cursor.execute(query)
            self.rows = cursor.fetchall() 
            self.rows=self.rows[:4]
            self.text_entry(self.week_data,'Week')
        elif value==4:
            query = """select
                    year(bill_date) as year,
                    month(bill_date)as month,
                    sum(netpay) as TotalNetPay,
                    count(Bill_no) as total_no,
                    sum(Products_count) as total_sold
                    from CustomerDeatails
                    group by
                    year(bill_date),
                    month(bill_date)
                    order by 
                    TotalNetPay desc
                    """
            cursor.execute(query)
            self.rows = cursor.fetchall()  
            self.text_entry(self.month_data,'Month')
        else:
            pass
    def plot_switch_date(self):
        self.plotframe_date.pack()
        self.plotframe_month.pack_forget()
        self.plotframe_week.pack_forget()
         
    def plot_switch_month(self):
        self.plotframe_date.pack_forget()
        self.plotframe_month.pack()
        self.plotframe_week.pack_forget()
    def plot_switch_week(self):
        self.plotframe_date.pack_forget()
        self.plotframe_month.pack_forget()
        self.plotframe_week.pack()  
        
    def create_plot_date(self):
        

        query = """select 
	                convert(date,bill_date) as Bill_dates,
	                sum(netpay) as TotalNetPay
                   from CustomerDeatails
                    group by
	                convert(date,bill_date)"""
        cursor.execute(query)
        rows = cursor.fetchall()
        x=[]
        y=[]
        
        for i in rows[-10:]:
            x.append(i[0])
            y.append(i[1]) 
        fig ,ax = plt.subplots(figsize=(10,4))
        ax.bar(x,y,color='blue')
        ax.set_title('Daily Sales')
        ax.set_xlabel('Day')
        ax.set_ylabel('Sales')
        self.plot_data(2)
        return fig
        
    def create_plot_weekly(self):
        query = """select 
	                year(bill_date) as year,
	                datepart(week,bill_date) as weeknumber,
	                sum(netpay) as TotalNetPay
                   from CustomerDeatails
                   group by
	                year(bill_date),
	                datepart(week,bill_date)
                   order by 
	                year,
	                weeknumber"""
        cursor.execute(query)
        rows = cursor.fetchall()
        x=[]
        y=[]
        for i in rows:
            x.append(i[1])
            y.append(i[2])
        fig1 ,ax = plt.subplots(figsize =(10,4))

        ax.bar(x,y,color='blue')
        ax.set_title('Weekly Sales')
        ax.set_xlabel('Weeks')
        ax.set_ylabel('Sales')
        self.plot_data(3)
        return fig1
    
    def create_plot_month(self):
        query = """select 
	                year(bill_date) as year,
	                datepart(month,bill_date) as month,
	                sum(netpay) as TotalNetPay
                    from CustomerDeatails
                    group by
	                year(bill_date),
	                datepart(month,bill_date)
                    order by 
	                year,
	                month"""
        cursor.execute(query)
        rows = cursor.fetchall()
        x=[]
        y=[]
        for i in rows:
            x.append(i[1])
            y.append(i[2]) 
        fig2 ,ax = plt.subplots(figsize=(10,4))
        ax.bar(x,y,color='blue')
        ax.set_title('Monthly Sales')
        ax.set_xlabel('Month')
        ax.set_ylabel('Sales')
        self.plot_data(4)
        return fig2
    
    def text_entry(self,frame,part):
        frame.insert(tk.END,f"\t{' '*30}{part} WISE SALES REPORT\n")
        frame.insert(tk.END,f"\t{' '*15} {"_"*50}\n")
        frame.insert(tk.END,f"\t{' '*15}| {'Year':<5}|{part:<5}|{'Total Sales':<10}|{'Customers':<10}|{'Products Sold':<13} |\n")
        temp_var=0
        for item in self.rows:
            frame.insert(tk.END,f"\t{' '*15}| {"-"*5}|{"-"*5}|{"-"*10} |{"-"*10}|{"-"*14}|\n")
            frame.insert(tk.END,f"\t{' '*15}| {item[0]:<5}|{item[1]:<5}|{item[2]:<10} |{item[3]:<10}|{item[2]:<13} |\n")
            temp_var+=1           
        frame.insert(tk.END,f"\t{' '*15}| {"_"*5}|{"_"*5}|{"_"*10} |{"_"*10}|{"_"*14}|\n")
        frame.insert(tk.END,f"\n\t{' '*15}Highest Sales of the {part} is {self.rows[0][1]} with Sales RS.{self.rows[0][2]}\n")
        frame.insert(tk.END,f"\t{' '*15}Lowest Sales of the {part} {self.rows[temp_var-1][1]} with Sales RS.{self.rows[temp_var-1][2]}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = BillingSoftware(root)
    root.mainloop()
