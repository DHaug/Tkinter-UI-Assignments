#**********************************************************
##*****        Students: Derek Haugen and Chris Tudehope      *****
# #*****       Class:  Human Factors and User Interface       *****
# #*****     Instructor:  Gamradt                             *****
# #*****     Assignment:  1                                   *****
# #*****     Due Date:  02-23-18                              *****
# #**********************************************************
# #*****  Description: This program is a GUI for a mock-up
# ****** Shotgun shop. The program handles picking the gun with
# ****** many options and adding it among others to a cart. You
# ****** can then checkout a buy the guns with our payment page.
# ****** We handle all windows through seperate classes and
# ****** instantiating them when needed and destroying when not.
# #**********************************************************


from Tkinter import *   ## notice capitalized T in Tkinter
from PIL import Image, ImageTk
from tkMessageBox import * #Careful with this all-inclusive import
from Globals import *

#Make sure to change GUI colors because they are UGLY

#Class Author: Derek Haugen
#Main class, also the controller
class ShoppingApp(Tk):
    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs) #initialize Tkinter
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.config(cursor="target")

       #Menu is defined
        menu = Menu(container)
        editmenu = Menu(menu,tearoff=0)
        editmenu.add_command(label="Assingment # 2")
        editmenu.add_command(label="Creators: Derek H and Chris T")
        editmenu.add_command(label="Due Date: 2/23/2018")
        editmenu.add_command(label="Class Info: SE 330 Gamradt")
        menu.add_cascade(label="About", menu=editmenu)
        quitMenu = Menu(menu,tearoff=0)
        quitMenu.add_command(label="Quit!", command=self.destroy)
        menu.add_cascade(label="Help",menu=quitMenu)

        self.config(menu=menu)

        self.checkOutInfo = CheckOutInfo(StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),IntVar())

        #Holds the current shopping cart
        self.gunCart = []

        self.frames = {} #initialize a dict of frames really not necessary

        self.startFrame(container,self,StartPage)

    #Used to start a frame without any extra arguments. Call this to go to a new page
    def startFrame(self,container, contoller, Frame):
        frame=Frame(container,contoller)
        self.frames[Frame]=frame
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    #Specific calling for page2 because I need to pass in another variable
    def startPage2(self, container, contoller, Frame, Invar):
        frame = Frame(container, contoller, Invar)
        self.frames[Frame] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

#Class Author: Derek Haugen
class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent,background=backgroundColor)

        #Title
        title = Label(self, text="Welcome to Chris and Derek's Shotgun Shop!", font = ('Arial bold' , 30),background=backgroundColor)

        #image
        startImg= ImageTk.PhotoImage(Image.open("Brett.jpg").resize((450,350)))
        Img = Label(self, image=startImg, relief=RAISED)
        Img.image = startImg

        #Button
        BeginB = Button(self, text="Begin Shopping!", command=lambda:  controller.startFrame(parent,controller,PageOne),width=50,height=4,relief=RAISED,background="green")

        #Packing in order
        title.pack(pady=10, padx=10)
        Img.pack(pady=20)
        BeginB.pack()

#Class Author: Derek Haugen
class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent,background=backgroundColor)
        title = Label(self, text="Available Guns!",font=('Arial bold' , 20),background='Green',relief=RAISED)

        InFrame = Frame()
        InFrame.pack()
        InFrame.rowconfigure(4,weight=1)
        InFrame.columnconfigure(3, weight=1)

        #Image1
        startImg = ImageTk.PhotoImage(Image.open("Xtreme.png").resize((350,250)))
        Img1 = Label(self, image=startImg)
        Img1.image = startImg

        #Image2
        startImg = ImageTk.PhotoImage(Image.open("Outlander.png").resize((350,250)))
        Img2 = Label(self, image=startImg)
        Img2.image = startImg

        #Image3
        startImg = ImageTk.PhotoImage(Image.open("687Classic.png").resize((350,250)))
        Img3 = Label(self, image=startImg)
        Img3.image = startImg


        Op1 = Button(self,background='green', text="More Details!", width=20, height=2, command=lambda: controller.startPage2(parent,controller,PageTwo,Gun("A400 Xtreme","","","","","","Xtreme.png",DescriptionA400,int(1450))))
        Op2 = Button(self,background='green', text="More Details!",width=20, height=2, command=lambda: controller.startPage2(parent,controller,PageTwo,Gun("A300 Outlander","","","","","","Outlander.png",DescriptionA300,int(900))))
        Op3 = Button(self, background='green', text="More Details!",width=20, height=2, command=lambda: controller.startPage2(parent,controller,PageTwo,Gun("687 Classic O/U","","","","","","687Classic.png",Description687,int(3900))))

        title.grid(row=0,column=1)
        Img1.grid(row=1, column=0)
        Img2.grid(row=1, column=1)
        Img3.grid(row=1, column=2)
        Op1.grid(row=2,column=0)
        Op2.grid(row=2, column=1)
        Op3.grid(row=2, column=2)

        startImg = ImageTk.PhotoImage(Image.open("BottomFiller.jpg").resize((950, 250)))
        Img4 = Label(self, image=startImg,background=backgroundColor)
        Img4.image = startImg
        Img4.grid(row=3,column =0, columnspan=3,ipady=20)



#Class Author: Derek Haugen
#Gui page that handles the user's shotgun customization
class PageTwo(Frame):

    def __init__(self, parent, controller, chosenGun):
        Frame.__init__(self, parent,background=backgroundColor)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(1, weight=1)
        self.StockPrice=chosenGun.stockPrice
        self.controller=controller
        self.parent=parent
        self.chosenGun=chosenGun

        InFrameL = Frame(self,background=backgroundColor)
        InFrameL.grid(column=0, row = 0)
        InFrameL.rowconfigure(3,weight=1)
        InFrameL.columnconfigure(1,weight=1)

        InFrameR = Frame(self,background=backgroundColor)
        InFrameR.rowconfigure(10, weight=1)
        InFrameR.columnconfigure(3,weight=1)
        InFrameR.grid(column=1,row = 0, sticky=N,ipady=0)

        startImg = ImageTk.PhotoImage(Image.open(chosenGun.picture_filename).resize((350, 250)))
        Img1 = Label(InFrameL, image=startImg)

        Img1.image = startImg
        Img1.grid(row = 0, column = 0)

        Titledesc = Label(InFrameL, text="Description",font=('Arial bold' , 10), wraplength=300, justify=CENTER,background=backgroundColor)
        Titledesc.grid(row=1, column=0)

        desc = Label(InFrameL, text=chosenGun.description ,wraplength=300, justify=CENTER,background=backgroundColor)
        desc.grid(row=2,column=0)

        self.TitleLabel = Label(InFrameR, text="CUSTOMIZER", font = ('Arial bold' , 40), justify=CENTER,background=backgroundColor,relief=RAISED)
        self.TitleLabel.grid(row=0, column=0, columnspan=2)

        self.FinishLabel = Label(InFrameR, text="Finish:", font=LARGE_FONT,wraplength=100,justify=LEFT,background=backgroundColor)
        self.FinishLabel.grid(row=1,column=0,ipadx=5,ipady=10)

        if chosenGun.name == "687 Classic O/U":
            self.FinishDropDown = MyOptionMenu(InFrameR, "Blued + Stained", "Blued + Stained")
            self.FinishDropDown.var.trace('w',self.updatePrice)
            self.FinishDropDown.grid(row=1, column=1, sticky='w', ipadx=5, ipady=10)
        else:
            self.FinishDropDown = MyOptionMenu(InFrameR,"Max 5 Camo", "Max 5 Camo", "Optifade Camo", "Black Synthetic")
            self.FinishDropDown.var.trace('w',self.updatePrice)
            self.FinishDropDown.grid(row=1,column=1,sticky='w',ipadx=5,ipady=14)

        self.BarrelLabel = Label(InFrameR, text="Barrel Size:", font=LARGE_FONT, wraplength=100, justify=LEFT,background=backgroundColor)
        self.BarrelLabel.grid(row=2, column=0, ipadx=5, ipady=10)

        self.BarrelDropDown = MyOptionMenu(InFrameR, "28", "26", "28","30")
        self.BarrelDropDown.var.trace('w',self.updatePrice)
        self.BarrelDropDown.grid(row=2, column=1, sticky='w', ipadx=5, ipady=10)

        self.ChamberLabel = Label(InFrameR, text="Chamber Size:", font=LARGE_FONT, wraplength=150, justify=LEFT,background=backgroundColor)
        self.ChamberLabel.grid(row=3, column=0, ipadx=5, ipady=10)

        self.ChamberDropDown = MyOptionMenu(InFrameR, "2 3/4", "2 3/4", "3", "3 1/2")
        self.ChamberDropDown.var.trace('w',self.updatePrice)
        self.ChamberDropDown.grid(row=3, column=1, sticky='w', ipadx=5, ipady=10)

        self.SightLabel = Label(InFrameR, text="Sight:", font=LARGE_FONT, wraplength=150, justify=RIGHT,background=backgroundColor)
        self.SightLabel.grid(row=4, column=0, ipadx=5, ipady=10)

        self.SightDropDown = MyOptionMenu(InFrameR, "Single-Bead", "Tru-Glow", "Single-Bead", "Double-Bead")
        self.SightDropDown.var.trace('w',self.updatePrice)
        self.SightDropDown.grid(row=4, column=1, sticky='w', ipadx=5, ipady=10)

        self.ChokeLabel = Label(InFrameR, text="Choke:", font=LARGE_FONT, wraplength=150, justify=RIGHT,background=backgroundColor)
        self.ChokeLabel.grid(row=5, column=0, ipadx=5, ipady=10)

        self.ChokeDropDown = MyOptionMenu(InFrameR, "Modified", "Modified","Full-Choke", "Improved Cylinder")
        self.ChokeDropDown.var.trace('w',self.updatePrice)
        self.ChokeDropDown.grid(row=5, column=1, sticky='w', ipadx=5, ipady=10)


        self.AddToCart = Button(InFrameR, text="Add to cart!", width=20, command=lambda: self.updateCart(chosenGun,controller,parent),background="Green")
        self.AddToCart.grid(row=10, column = 0,columnspan=1, ipady=10)

        self.Back = Button(InFrameR, text="Back!", command=lambda: [self.goBack(self)],background="Red")
        self.Back.config(width = 20)
        self.Back.grid(row=10, column = 2, columnspan=1,ipady=10)

        self.SPACER = Label(InFrameR, text="", font=('Arial', 20), wraplength=100, justify=LEFT, background =backgroundColor)
        self.SPACER.grid(row=9, column=1, columnspan=2, ipadx=5, ipady=70)

        #Checkout button!
        self.Checkout = Button(InFrameR, text="Checkout!", command=lambda: [self.goToCheckout()], background="Green",)
        self.Checkout.grid(row=10, column=1, columnspan=1, ipady=5)
        self.Checkout.config(width=20, height=2)

        self.PriceLabel = Label(InFrameR, text="Price:", font=('Arial',20), wraplength=100, justify=LEFT,background=backgroundColor)
        self.PriceLabel.grid(row=1, column=3, ipadx=5, ipady=10)

        self.UpdatePriceLabel = Label(InFrameR, text=str(self.StockPrice), font=('Arial',20), wraplength=100, justify=LEFT, relief=SUNKEN,background='cyan2')
        self.UpdatePriceLabel.grid(row=1, column=4, ipadx=5, ipady=10)

        self.ChokeDropDown.configure(command=self.updatePrice())

#This maps to the checkout page
    def goToCheckout(self):
        if askyesno('Checkout', 'Do you want to add your current customized gun?'):
            self.updateCart(self.chosenGun, self.controller, self.parent)
        else:
            pass

        self.controller.startFrame(self.parent, self.controller, PageThree)



    #THIS WILL INSERT THE CHOSEN GUN INTO THE LIST
    def updateCart(self,chosenGun,mainAppObj,parent):
        newchosenGun = Gun(chosenGun.name,"","","","","",chosenGun.picture_filename,chosenGun.stockPrice,chosenGun.stockPrice)
        newchosenGun.color = self.FinishDropDown.var.get()
        newchosenGun.barrel=self.BarrelDropDown.var.get()
        newchosenGun.chamber_size=self.ChamberDropDown.var.get()
        newchosenGun.sight=self.SightDropDown.var.get()
        newchosenGun.choke=self.ChokeDropDown.var.get()
        newchosenGun.price= int(self.UpdatePriceLabel.cget("text"))
        mainAppObj.gunCart.append(newchosenGun)
        showinfo("Success!","Gun added to cart!")

    #Goes back to previous page
    def goBack(self,inp):
        if askyesno('Go Back', 'Going back will discard your changes. Are you sure?'):
            inp.destroy() #Destory the frame
        else:
            pass
	
    #function that keeps updating my price as they select it
    def updatePrice(self,*args):
        TotalPrice = self.StockPrice
        if self.BarrelDropDown.var.get() == "28":
            TotalPrice = TotalPrice + 50
        if self.FinishDropDown.var.get() == "Black Synthetic":
            TotalPrice = TotalPrice + 50
        if self.ChokeDropDown.var.get() == "Modified":
            TotalPrice = TotalPrice + 50
        if self.SightDropDown.var.get() == "Single-Bead":
            TotalPrice = TotalPrice + 50


        if self.FinishDropDown.var.get() == "Max 5 Camo":
            TotalPrice = TotalPrice + 100
        if self.SightDropDown.var.get() == "Double-Bead":
            TotalPrice = TotalPrice + 100
        if self.ChokeDropDown.var.get() == "Full-Choke":
            TotalPrice = TotalPrice + 100
        if self.ChamberDropDown.var.get() == "3":
            TotalPrice = TotalPrice + 100


        if self.SightDropDown.var.get() == "Tru-Glow":
            TotalPrice = TotalPrice + 150
        if self.BarrelDropDown.var.get() == "30":
            TotalPrice = TotalPrice + 150
        if self.FinishDropDown.var.get() == "Optifade Camo":
            TotalPrice = TotalPrice + 200
        if  self.ChamberDropDown.var.get() == "3 1/2":
            TotalPrice = TotalPrice + 200

        self.UpdatePriceLabel.configure(text=str(TotalPrice)) #Update my price text



#Class Author: Chris Tudehope
#Page used for checkout of our shopping cart
class PageThree(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent,background=backgroundColor)

        def storeBackend():
            print 'First name: %s' %controller.checkOutInfo.firstName.get()
            print 'Last name: %s' %controller.checkOutInfo.lastName.get()
            print 'Address:  %s' %controller.checkOutInfo.address.get()
            print 'City: %s' %controller.checkOutInfo.city.get()
            print 'Zip Code: %s' %controller.checkOutInfo.zipCode.get()
            print 'Phone Number: %s' %controller.checkOutInfo.phone.get()
            print 'Email: %s' %controller.checkOutInfo.email.get()
            print 'Name on Card: %s' %controller.checkOutInfo.cardName.get()
            print 'Card Number: %s' %controller.checkOutInfo.cardNumber.get()
            print 'Experation Month: %s' %controller.checkOutInfo.expMonth.get()
            print 'Experation Year: %s' %controller.checkOutInfo.expYear.get()
            print 'Liability Check: %s' %controller.checkOutInfo.liability.get()
            inc = 1
            for gun in controller.gunCart:
                print 'Gun %d: %s' % (inc, gun.name)
                print ' Color: %s' % gun.color
                print ' Barrel: %s' % gun.barrel
                print ' Sight: %s' % gun.sight
                print ' Chamber Size: %s' % gun.chamber_size
                print ' Choke: %s' % gun.choke
                print 'Price: %d' %gun.price
                inc = inc + 1
            del controller.gunCart[:]
            controller.checkOutInfo.clear()
            showinfo('Order Placed', 'Your order will be shipped soon.\nA receipt has been sent to your email.')
            controller.startFrame(parent, controller, StartPage)

        def emptyCart():
            del controller.gunCart[:]
            controller.checkOutInfo.clear()
            controller.startFrame(parent, controller, StartPage)

        title = Label(self, text="Shopping Cart",background=backgroundColor,font=("Arial Bold",40))

        itemDetailFrame = Frame(self,width='40', height='20',background=backgroundColor)
        personalInfoFrame = Frame(self,background=backgroundColor)

        shipmentSection = Label(personalInfoFrame, text='Personal Information', width='20',background=backgroundColor,font=("Arial Bold",10)).grid(row=0, column = 0,columnspan=2, sticky=NSEW)
        fName = Label(personalInfoFrame, text='First Name', width='20',background=backgroundColor,font=("Arial Bold",10)).grid(row=2, column = 0,columnspan=2, sticky=NSEW)
        fNameEnt = Entry(personalInfoFrame, width='20',textvariable=controller.checkOutInfo.firstName).grid(row=3, column = 0,columnspan=2, sticky=NSEW)
        lName = Label(personalInfoFrame, text='Last Name', width='20',background=backgroundColor,font=("Arial Bold",10)).grid(row=2, column = 2,columnspan=2, sticky=NSEW)
        lNameEnt = Entry(personalInfoFrame, width='20',textvariable=controller.checkOutInfo.lastName).grid(row=3, column = 2,columnspan=2, sticky=NSEW)
        address = Label(personalInfoFrame, text='Address', width='40',background=backgroundColor,font=("Arial Bold",10)).grid(row=4, column = 0,columnspan=4, sticky=NSEW)
        addressEnt = Entry(personalInfoFrame, width='40',textvariable=controller.checkOutInfo.address).grid(row=5, column = 0,columnspan=4, sticky=NSEW)
        city = Label(personalInfoFrame, text='City', width='20',background=backgroundColor,font=("Arial Bold",10)).grid(row=6, column = 0,columnspan=2, sticky=NSEW)
        cityEnt = Entry(personalInfoFrame, width='20',textvariable=controller.checkOutInfo.city).grid(row=7, column = 0,columnspan=2, sticky=NSEW)
        state = Label(personalInfoFrame, text='State', width='20',background=backgroundColor,font=("Arial Bold",10)).grid(row=6, column = 2,columnspan=2, sticky=NSEW)
        stateChoices = ['-','AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI','ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY', 'NC','ND',
                        'OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
        statePopupMenu = OptionMenu(personalInfoFrame, controller.checkOutInfo.state, *stateChoices).grid(row=7, column=2, columnspan=2,stick=NSEW)
        controller.checkOutInfo.state.set('-')
        zip = Label(personalInfoFrame, text='Zip Code', width='20',background=backgroundColor,font=("Arial Bold",10)).grid(row=8, column = 0,columnspan=2, sticky=NSEW)
        zipEnt = Entry(personalInfoFrame, width='20',textvariable=controller.checkOutInfo.zipCode).grid(row=9, column = 0,columnspan=2, sticky=NSEW)
        phone = Label(personalInfoFrame, text='Phone Number', width='20',background=backgroundColor,font=("Arial Bold",10)).grid(row=8, column = 2,columnspan=2, sticky=NSEW)
        phoneEnt = Entry(personalInfoFrame, width='20',textvariable=controller.checkOutInfo.phone).grid(row=9, column = 2,columnspan=2, sticky=NSEW)
        email = Label(personalInfoFrame, text='Email', width='40',background=backgroundColor,font=("Arial Bold",10)).grid(row=10, column = 0,columnspan=4, sticky=NSEW)
        emailEnt = Entry(personalInfoFrame, width='40',textvariable=controller.checkOutInfo.email).grid(row=11, column = 0,columnspan=4, sticky=NSEW)

        paymentInfoSection = Label(personalInfoFrame, text='Payment Information', width='20',background=backgroundColor,font=("Arial Bold",10)).grid(row=12, column = 0,columnspan=2, sticky=NSEW)
        cardName = Label(personalInfoFrame, text='Name on Card', width='10',background=backgroundColor,font=("Arial Bold",10)).grid(row=13, column = 0,columnspan=1, sticky=NSEW)
        cardNameEnt = Entry(personalInfoFrame, width='20',textvariable=controller.checkOutInfo.cardName).grid(row=13, column = 1,columnspan=3, sticky=NSEW)
        cardNumber = Label(personalInfoFrame, text='Card Number', width='10',background=backgroundColor,font=("Arial Bold",10)).grid(row=14, column = 0,columnspan=1, sticky=NSEW)
        cardNumberEnt = Entry(personalInfoFrame, width='20',textvariable=controller.checkOutInfo.cardNumber,).grid(row=14, column = 1,columnspan=3, sticky=NSEW)
        expDate = Label(personalInfoFrame, text='Exp Date', width='10',background=backgroundColor,font=("Arial Bold",10)).grid(row=15, column = 0,columnspan=1, sticky=NSEW)
        monthChoices = ['-','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']
        monthPopupMenu = OptionMenu(personalInfoFrame, controller.checkOutInfo.expMonth, *monthChoices).grid(row=15, column=1, columnspan=2,stick=NSEW)
        controller.checkOutInfo.expMonth.set('-')
        yearChoices = ['-','2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028','2029', '2030']
        yearPopupMenu = OptionMenu(personalInfoFrame, controller.checkOutInfo.expYear, *yearChoices).grid(row=15, column=3, columnspan=2,stick=NSEW)
        controller.checkOutInfo.expYear.set('-')
        liabilitySection = Label(personalInfoFrame, text='Liability', width='10',background=backgroundColor,font=("Arial Bold",10)).grid(row=16, column = 0,columnspan=1, sticky=NSEW)
        liabCheck = Checkbutton(personalInfoFrame, variable=controller.checkOutInfo.liability, text='I promise not to shoot people with this gun.',background=backgroundColor,foreground="Red").grid(row=17,column=0,columnspan=4,sticky=NSEW)
        controller.checkOutInfo.liability.set(0)
        checkoutButton = Button(personalInfoFrame, text='Order', command=storeBackend).grid(row=18,column=0,columnspan=4,sticky=NSEW)

        gunCartSection = Label(itemDetailFrame, text='Gun Cart', width='20',background=backgroundColor,font=("Arial Bold",20)).pack()
        inc = 1
        lb = Listbox(itemDetailFrame, height=18, width=40,background=backgroundColor)
        for gun in controller.gunCart:
            lb.insert(END,'Gun %d: %s' %(inc, gun.name))
            lb.insert(END,'   Color: %s' %gun.color)
            lb.insert(END,'   Barrel: %s' %gun.barrel)
            lb.insert(END,'   Sight: %s' %gun.sight)
            lb.insert(END,'   Chamber Size: %s' % gun.chamber_size)
            lb.insert(END,'   Choke: %s' % gun.choke)
            lb.insert(END,' Price: $%d' % gun.price)
            inc=inc+1

        lb.pack()
        b = Button(itemDetailFrame, text="Continue Shopping", width='40',command=lambda: controller.startFrame(parent,controller,PageOne)).pack()
        b2 = Button(itemDetailFrame, text="Clear Cart", width='40',command=lambda: emptyCart()).pack()

        title.pack(side=TOP)
        itemDetailFrame.pack(expand=YES,side=LEFT)
        personalInfoFrame.pack(expand=YES, side=RIGHT)



app = ShoppingApp()

app.geometry("1100x600")

app.mainloop()