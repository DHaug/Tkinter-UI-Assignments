
#**********************************************************
##*****        Students: Derek Haugen and Chris Tudehope      *****
# #*****       Class:  Human Factors and User Interface       *****
# #*****     Instructor:  Gamradt                             *****
# #*****     Assignment:  1                                   *****
# #*****     Due Date:  02-23-18                              *****
# #**********************************************************
# #*****  Description: This python file holds global classes
#******* That are referenced from the main file. They are the
#******* structures that hold our data from fields and the
#******* pre-defined dropdowns made for pages.
# #**********************************************************
from Tkinter import *   ## notice capitalized T in Tkinter
from PIL import Image, ImageTk
from tkMessageBox import *
#Declared Font
LARGE_FONT= ("Verdana", 12)

#Background color set for all of my frames and labels!
backgroundColor="DarkOliveGreen1"



#Class that just holds all info about a gun
class Gun():
    def __init__(self,gun_name, color, barrel, sight, chamber_size, choke,picture_filename,desc,stockPrice):
        self.name=gun_name
        self.color=color
        self.barrel=barrel
        self.sight=sight
        self.chamber_size=chamber_size
        self.choke=choke
        self.picture_filename=picture_filename
        self.description=desc
        self.stockPrice=stockPrice
        self.price = None

class CheckOutInfo():
    def __init__(self,fName,lName,address,city,state,zipCode,phone,email,cardName,cardNumber,expMonth,expYear,liability):
        self.firstName = fName
        self.lastName = lName
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.phone = phone
        self.email = email
        self.cardName = cardName
        self.cardNumber = cardNumber
        self.expMonth = expMonth
        self.expYear = expYear
        self.liability = liability
    def clear(self):
        self.firstName = StringVar()
        self.lastName = StringVar()
        self.address = StringVar()
        self.city = StringVar()
        self.state = StringVar()
        self.zipCode = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.cardName = StringVar()
        self.cardNumber = StringVar()
        self.expMonth = StringVar()
        self.expYear = StringVar()
        self.liability = IntVar()

#Predefined OptionMenu that is styled so all optionmenu's are the same
class MyOptionMenu(OptionMenu):
    def __init__(self, master, status, *options):
        self.var = StringVar(master)
        self.var.set(status)
        OptionMenu.__init__(self, master, self.var, *options)
        self.config(bg='cyan')
        self['menu'].config(bg='white', font=('Calibri',(20)))
        self.config(width=20)


DescriptionA400="The Beretta A400 XTREME Semiautomatic Shotgun with Kick-Off reliably cycles everything from light 2-3/4"\
"trap loads to hard-hitting 3-1/2 waterfowl shells. Blink gas system can cycle four shells in less than"\
"one second, while the innovative Kick Off Mega recoil-reduction system cuts felt recoil up to 70%. Gas operating with"\
"compensating exhaust valve and a self-cleaning piston offer smooth, reliable operation. Aqua Technology ensures every"\
"part of the gun is corrosion-resistant. B-Lok forend cap with only 60 deg of rotation allows fast and easy"\
"assembly/disassembly. Synthetic stock with overmolded grips has an adjustable shim system and withstands rain, snow,"\
"dust and mud. Micro-Core recoil pad absorbs shock. Crossbolt safety sports ergonomics for a better grip and is" \
"reversible for left-handed shooters. Also features a chrome-plated trigger. Fiber-optic beaded front sight. Includes"\
"three Optima-Bore HP choke tubes (full, modified and cylinder), two stock spacers and a custom-fitted carry case."

DescriptionA300="Experience Beretta's legendary performance in a sleek design with the A300 Outlander Semiautomatic " \
                "Shotguns. With only four major components, these shotguns can be quickly and easily disassembled. " \
                "A compensating gas valve and a self-cleaning piston offer smooth, reliable operation. Lightweight " \
                "aluminum-alloy receiver handles 2-3/4, 3, and 3 1/2 shells. Synthetic stock with an adjustable length-of-pull" \
                " from 13 to 14-1/2 has an adjustable shim system and withstands rain, snow, dust and mud. " \
                "Fitted rubber recoil pad absorbs shock. Crossbolt safety sports ergonomics " \
                "for a better grip and is reversible for left-handed shooters."

Description687="At the core of the 687 Silver Pigeon III Sporting is our legendary 687-series receiver. This low-profile, " \
               "positive-locking, low-maintenance action ensures that your off-hand stays as close as possible to the " \
               "bore-axis; in this manner, whatever you point to is exactly where the shot goes. The receiver is embellished " \
               "with a scroll and game scene designed by our most experienced Master Engravers in Gardone, Italy. The way " \
               "this pattern is executed on the receiver makes it virtually as striking as if it had been hand-engraved, " \
               "but without the price tag to match."