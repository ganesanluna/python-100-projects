#example8.py
import webbrowser as browser                                    #1
web="http:\\www."                                               #2
site=str(input('enter your website name (ex:google.com) : '))   #3
website=str(web)+site                                           #4
browser.open(website)                                           #5
