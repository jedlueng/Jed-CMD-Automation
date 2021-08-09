#Started 13 July 2021
#Finished 9 August 2021  
#Jedsada Luengaramsuk 
#Goal: Type {JCW.py} {Name} to get to the right browser and right webpage 
#Use sys.arge for cmd
#Use Sherbang Line to run python automatically 
#Use webbrowser module 
#! /usr/bin/env python3
import webbrowser, sys
#Initialize each webbrowser with each path 
chrome = webbrowser.get("open -a /Applications/Chrome.app %s")
brave =  webbrowser.get("open -a /Applications/Brave.app %s")
firefox = webbrowser.get("open -a /Applications/Developer.app %s")
Safari = webbrowser.get("open -a /Applications/Safari.app %s")

#Input box 
site = str(input('What do you want to open?'))

if site == 'coin': 
    brave.open_new('https://coinmarketcap.com/')
elif site == 'amazon':
    chrome.open_new('https://amazon.co.uk/')
elif site == 'pareto': 
    brave.open_new('https://twitter.com/')
elif site == 'jjlueng': 
    chrome.open_new('https://twitter.com/')
elif site == 'codea': 
    firefox.open_new('https://www.codecademy.com/') #codeacademy 
elif site == 'comp': 
    firefox.open_new('https://learn.comptia.org/login#study-plan/structured')#comptia-training 
elif site == 'course': 
    chrome.open_new('https://coursera.org')#coursera
else: 
    print('Not in directory')


