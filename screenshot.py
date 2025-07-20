import pygetwindow as gw

def getClient():
    resizeX = 949
    resizeY = 619

    for title in gw.getAllTitles():
        if title != "":
            print(title)
        if title == 'Old School RuneScape':
            osrs = gw.getWindowsWithTitle('Old School RuneScape')[0]
            osrs.resizeTo(resizeX,resizeY)
            osrs.activate()
            break

getClient()