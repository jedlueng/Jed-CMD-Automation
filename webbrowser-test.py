import webbrowser

chrome = webbrowser.get("open -a /Applications/Chrome.app %s")
chrome.open_new('https://www.python.org')