
emgen.e

def grabhtml(page):

    places to grab from:
    start at "<div class="tabs"
    and end at "<div id="prefooter""
    grab important bit.
    returns formatted HTML

def emgen
    father function,
    grabhtml(artspage)
    grabhtml(judicialpage)
    etc..
    getlistSQL(arts)
    getlistSQL(judicial)
    getlistSQL(..)

    sendmail(artsHTML, artslist)
    sendmail(judicialHTML, judicialList)

end


def getlistSQL(arts)
    access database
    grab emails by sector
    format to Commaseparatedlist
    return Commaseparatedlist


def sendmail(artsHTML, artslist)
    send artsHTML to artslist
