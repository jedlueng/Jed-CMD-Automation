#Started 13 July 2021 
#Jedsada Luengaramsuk (Jedsada.io)
#Goal: Type {JCW.py} {Name} to get to the right browser and right webpage 

#Use sys.arge for cmd
#Use Sherbang Line to run python automatically 
#Use webbrowser module 

import webbrowser

chrome = webbrowser.get("open -a /Applications/Chrome.app %s")
brave =  webbrowser.get("open -a /Applications/Brave.app %s")
Firefox = webbrowser.get("open -a /Applications/Developer.app %s")
Safari = webbrowser.get("open -a /Applications/Safari.app %s")

def open (page):
    if page == 'brave':
        webbrowser.get(using='').open_new('') #open page in a browser you like  
    elif page == 'firefox': 
        webbrowser.get(using='').open_new('') #Open firefox + page 
    elif page == 'chrome': 
        webbrowser.get(using='').open_new('') #chrome + page 
    else: 
        webbrowser.get(using='none').open_new('') #Use default browser and search that url. 

