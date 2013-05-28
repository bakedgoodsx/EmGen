import urllib.request

#response = urllib.request.urlopen(page)
#html = response.read()


def grabhtml(sect,sectorpage):
    "This grabs the html from the page for each sector"
    response = urllib.request.urlopen(sectorpage)
    html = response.read()
    f = open(sect + '.html','w')
    ae = str(html)
    af = ae.replace("\\xc2\\xa0"," ")

    ab = af.replace('\\n','')
    ao = ab[2:]   
    i1 = ao.find('<div class="tabs')
    i2 = ao.find('<div id="prefooter"')
    a2 = ao[i1:i2]
    a3 = a2.replace('<a href="/content/','<a href="http://www.miequitynetwork.org/content/')
    # the string a3 is now the formatted HTML for the email.

    print("We are now grabbing content from " + sectorpage + "\n and saving it as " + sect + ".html\n")
    f.write(a3)
    f.close()
    # this worx damn well as of last writing



# build a dictionary [tag] [site]
# loop thru with a grabhtml call!
def kickstart():
        dict = {'arts-humanities','business','education','faith-communities','judicial-system','youth','government','foundations','non-profit','healthcare'}
     
        
        for i in dict:
            j = "http://www.miequitynetwork.org/sector/" + i
            grabhtml(i,j)
        print("\nCongratulations! Sector-HTML-grabbin' has succeeded successfully!\n")

