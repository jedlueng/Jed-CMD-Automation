#Started 13 July 2021 
#Jedsada Luengaramsuk (Jedsada.io)
#Goal: Type {JCW.py} {Name} to get to the right browser and right webpage 

#Use sys.arge for cmd
#Use Sherbang Line to run python automatically 
#Use webbrowser module 


#! /usr/bin/env python3

import webbrowser, pyperclip, sys

chrome = webbrowser.get("open -a /Applications/Chrome.app %s")
brave =  webbrowser.get("open -a /Applications/Brave.app %s")
Firefox = webbrowser.get("open -a /Applications/Developer.app %s")
Safari = webbrowser.get("open -a /Applications/Safari.app %s")


if len(sys.argv) > 1: 
    #Get address from command line 
    site = ' '.join(sys.argv[1:])
else:
    #Get address from clipboard 
    site = pyperclip.paste()

def open (a):
    if site == 'coinmarketcap': 
        brave.open_new('https://coinmarketcap.com/')
    else: 
        print(None)



