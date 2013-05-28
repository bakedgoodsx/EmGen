
import grabelist
import grabhtml

def startmenu():
    ain = input("Welcome to Erix Email Newsletter Generation Program (EmGen) \n Do you want to [1] Generate an Email list or [2] Grab html from a webpage?\n")
    if ain=='1':
        grabelist.kickstart()
    if ain=='2':
        grabhtml.kickstart()

startmenu()
