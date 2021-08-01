import webbrowser

#This code is for mac 
#Use this webbrowser 
chrome = webbrowser.get("open -a /Applications/Chrome.app %s")

#Use this website to open this site. 
chrome.open_new('https://www.python.org')