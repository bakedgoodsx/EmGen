import urllib.request

#response = urllib.request.urlopen(page)
#html = response.read()


def grabhtml(sectorpage):
    "This grabs the html from the page for each sector"
    response = urllib.request.urlopen(sectorpage)
    html = response.read()
    f = open('test.html','w')
    ae = str(html)
    af = ae.replace("\\xc2\\xa0"," ")

    ab = af.replace('\\n','')
    ao = ab[2:]   
    i1 = ao.find('<div class="tabs')
    i2 = ao.find('<div id="prefooter"')
    a2 = ao[i1:i2]
    a3 = a2.replace('<a href="/content/','<a href="http://www.miequitynetwork.org/content/')
    # the string a3 is now the formatted HTML for the email.

    f.write(a3)
    f.close()
    # this worx damn well as of last writing
grabhtml('http://www.miequitynetwork.org/tags/arts')

