'''

You need to install all these libraries in order to run this.
Use "pip install library-name" command to install any the below libraries.
Replace 'library-name' with the library you wanna download.

'''

from tkinter import *
import tkinter as tk
import re
import smtplib
import webbrowser
from time import sleep
from random import randint as ri


#Created a window
y=Tk()
y.withdraw()
warns=PhotoImage(file=r'warning.png')

#To open the window on the center of our screen
def center(screen,width,height):
        wid=screen.winfo_screenwidth()  #To get screen dimensions
        high=screen.winfo_screenheight()
        x=(wid//2)-(width//2)
        y=(high//2)-(height/2)
        screen.geometry("%dx%d+%d+%d"%(width,height,x,y))

#To open incognito browser
def ok(b):
    global access
    
    url="https://myaccount.google.com/lesssecureapps?gar=1"     #Link to allow less secure apps.
    
    # MacOS
    #chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    # Windows
    # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'
    try:
        while(1):
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito").open(url)
            access.withdraw()
            sleep(1)
            break
        
        if(b=="SignIn & Allow"):
            wind.deiconify()
            obj=design()
            center(wind,400,600)
            
    except Exception:
        error=Tk()
        error.resizable(0,0)
        error.iconphoto(False,warns)
        error.configure(bg="#f5f5f5")
        error.title("Warning")
        center(error,300,150)
        
        l=Label(wind,text="Network Error/Import Module Error",bg="#f5f5f5",fg="red",font=("Bahnschrift SemiBold",12))
        l.place(x=20,y=50)

        wind.withdraw()
        access.deiconify()

        
#LogIn Window       
wind=Toplevel(y)
wind.resizable(0,0)
wind.configure(bg="#F5F5F5")
wind.title("Krishna's Spammer")
icon=PhotoImage(file=r"gmail.png")
wind.iconphoto(False,icon)
bground=PhotoImage(file=r'hacker.png')
wind.withdraw()

#Access Window
def aces(a,b):
    global access
    
    access=Toplevel(y)
    access.resizable(0,0)
    access.configure(bg="#008080")
    access.iconphoto(False,warns)
    access.title("Warning")

    center(access,700,200)      #Call senter function to center window.

    txt=Label(access,bg="#008080",fg="white",text=a,justify=LEFT)
    txt.place(x=80,y=30)
    
    allow=Button(access,text=b,bg="white",fg="black",command=lambda:ok(b))
    allow.configure(width=20,height=1)
    
    if(b=="SignIn & Allow"):
        allow.place(x=290,y=140)
    else:
        allow.place(x=290,y=100)
        
#Creating Login Window
class design:

    def __init__(self):
        
        def erase(event):
            if(event.widget.cget('fg')=='grey'):
                event.widget.delete(0,"end")
                event.widget.configure(fg='black')
        
        self.win=wind
        #TopBorder Line
        line_canvas=Canvas(self.win,width=400,height=3,bg="#7B68EE")
        line_canvas.place(x=0,y=0)

        #UserAvatar
        self.user=PhotoImage(file="user.png")
        img_canvas=Canvas(self.win,width=32,height=32,bg="#F5F5F5")
        img_canvas.place(x=50,y=50,anchor=NW)
        img_canvas.create_image(2,2,anchor=NW,image=self.user)

        #Log In Label
        LogIn = Label(self.win,bg="#F5F5F5",text="Sign In",font=("Bahnschrift SemiBold",18))
        
        LogIn.place(x=95,y=50)

        #Border Line
        line1_canvas=Canvas(self.win,width=300,height=1,bg='grey')
        line1_canvas.place(x=50,y=90)

        #Profile Label
        profile = Label(self.win,bg="#F5F5F5",text="Profile",font=("Bahnschrift SemiBold",13))
        profile.place(x=50,y=110)

        #Count Label
        Count = Label(self.win,bg="#F5F5F5",text="COUNT",font=("Bahnschrift SemiBold",8),fg='grey')
        Count.place(x=50,y=145)

        #Allow Label
        Allow = Label(self.win,bg="#F5F5F5",text="ALLOW",font=("Bahnschrift SemiBold",8),fg='grey')
        Allow.place(x=210,y=145)
        
        #Email Label
        RxEmail = Label(self.win,bg="#F5F5F5",text="EMAIL",font=("Bahnschrift SemiBold",8),fg='grey')
        RxEmail.place(x=50,y=220)

        #Border Line
        line2_canvas=Canvas(self.win,width=300,height=1,bg='grey')
        line2_canvas.place(x=50,y=295)

        #Account Label
        Account = Label(self.win,bg="#F5F5F5",text="Account",font=("Bahnschrift SemiBold",13))
        Account.place(x=50,y=315)

        #Username Label
        Username = Label(self.win,bg="#F5F5F5",text="USERNAME",font=("Bahnschrift SemiBold",8),fg='grey')
        Username.place(x=50,y=350)

        #Password Label
        Password = Label(self.win,bg="#F5F5F5",text="PASSWORD",font=("Bahnschrift SemiBold",8),fg='grey')
        Password.place(x=50,y=425)

        #Count Entry
        CountEntry = Entry(self.win,bg="white",fg='grey',font=("Bahnschrift SemiBold",8),relief=FLAT)
        CountEntry.insert(0,"e.g: Max: 20")
        CountEntry.place(x=53,y=170,width=130,height=35)
        CountEntry.bind('<Button-1>',erase)

        #Allow Entry
        AllowEntry = Entry(self.win,bg="white",fg='grey',font=("Bahnschrift SemiBold",8),relief=FLAT)
        AllowEntry.insert(0,"e.g: Type Allow")
        AllowEntry.place(x=210,y=170,width=130,height=35)
        AllowEntry.bind('<Button-1>',erase)

        #Email Entry
        EmailEntry = Entry(self.win,bg="white",fg='grey',font=("Bahnschrift SemiBold",8),relief=FLAT)
        EmailEntry.insert(0,"e.g: xyz@gmail.com")
        EmailEntry.place(x=53,y=245,width=290,height=35)
        EmailEntry.bind('<Button-1>',erase)

        #Username Entry
        UsernameEntry = Entry(self.win,bg="white",fg='grey',font=("Bahnschrift SemiBold",8),relief=FLAT)
        UsernameEntry.insert(0,"e.g: xyz@gmail.com")
        UsernameEntry.place(x=53,y=375,width=290,height=35)
        UsernameEntry.bind('<Button-1>',erase)

        #Password Entry
        PasswordEntry = Entry(self.win,bg="white",fg='grey',font=("Bahnschrift SemiBold",8),show="$",relief=FLAT,bd=4)
        PasswordEntry.insert(0,"Password")
        PasswordEntry.place(x=53,y=450,width=290,height=35)
        PasswordEntry.bind('<Button-1>',erase)

        #Border Line
        line3_canvas=Canvas(self.win,width=300,height=1,bg='grey')
        line3_canvas.place(x=50,y=510)

        self.lis=self.win.winfo_children()[12:-1]   #to store variable names in list
        
        #Login
        LoginButton=Button(self.win,bg="#32cd32",fg="white",text="LOGIN",relief=RIDGE,font=("Bahnschrift SemiBold",10),command=self.login)
        LoginButton.place(x=250,y=530,width=100,height=40)

    def decision(self,opt):
        
        if(opt=='N'):
            wind.withdraw()
            warn='''We recommend you to trun off access for less secure apps in order to protect your account
from unforeseeable attacks.'''
            self.noti.withdraw()
            aces(warn,"SignIn & Deny Access")
            
        else:
            self.noti.withdraw()
            self.win.deiconify()
            

    def msg(self,msge):
        self.noti=Toplevel(y)
        center(self.noti,400,180)
        self.noti.resizable(0,0)
        self.noti.title("Message")
        self.noti.iconphoto(False,icon)
        self.noti.configure(bg="#b3e7dc")

        mesg=Label(self.noti,text=msge,fg="red",bg="white",font=("Bahnschrift SemiBold",12))
        mesg.place(x=130,y=30)

        again=Label(self.noti,text="Do you want to try again?",fg="black",bg="#b3e7dc",font=("Bahnschrift SemiBold",12))
        again.place(x=110,y=70)

        yes=Button(self.noti,text="Yes",bg="white",fg="black",command=lambda:self.decision("Y"),width=5,height=1)
        yes.place(x=140,y=115)

        no=Button(self.noti,text="No",bg="white",fg="black",command=lambda:self.decision("N"),width=5,height=1)
        no.place(x=200,y=115)

    def login(self):
        
        if(self.checkers()):
            count=int(self.lis[0].get())
            
            for i in range(count):          #Generating otp as per the count given by the user
                msg=''
                otp=''
                x=str(ri(0,100))
                if(len(x)<2):
                    x='0'+x
                    otp=x
                else:
                    otp=x
                x=chr(ri(65,91))
                otp+=x
                x=chr(ri(97,123))
                otp+=x
                otp=otp+str(ri(100,999))
                msg+=(otp+'\n')
                msg=msg+"These are the automated OTP's generated by python."
            
                try:                                #Sending mail using smtplib
                    sender=str(self.lis[3].get())   #"rpkrishnak@gmail.com"
                    receiver=str(self.lis[2].get()) #"pavankrish16@gmail.com"
                    psw=str(self.lis[4].get())  
                    smtpobj=smtplib.SMTP('smtp.gmail.com',587)
                    smtpobj.starttls()
                    smtpobj.login(sender,psw)
                    smtpobj.sendmail(sender,receiver,msg)
                    smtpobj.quit()
                    sleep(1)
                    self.win.withdraw()
                    wind.withdraw()
                    self.msg("Succesfully Sent")
                except Exception:
                    self.msg("UnSuccessful")


    def checkers(self):     #Checking all user entries.
        
        checker=['[0-9]','^allow','^[a-z0-9]+[\._]?[a-z0-9]+@gmail.com','^[a-z0-9]+[\._]?[a-z0-9]+@gmail.com']
        c=0
        j=0
        for i in self.lis[:-1]:
            x=i.get()
            if(j==1):
                x=x.lower()
            if(re.search(checker[j],x)):
                c+=1
            else:
                i.configure(fg='red')
            j+=1
        if(c==4):
            return True
        return False


#Main Function
if __name__=='__main__':
    access=0
    warn='''\nNOTE: This is for Professional Purpose only and the Author is not responsible for any unauthorised/Illegal activities.
As we are not providing any security related code in this, you need to allow access for less secure apps
in your gmail account. SO Please click ALLOW button to continue.

PS: If you skip this step you can't send mails.'''

    aces(warn,"SignIn & Allow")
