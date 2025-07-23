import pygetwindow as gw

def get_client():
    resize_x = 936
    resize_y = 611

    for title in gw.getAllTitles():
        if title != "":
            print(title)
        if title == 'Old School RuneScape':
            osrs = gw.getWindowsWithTitle('Old School RuneScape')[0]
            osrs.resizeTo(resize_x,resize_y)
            osrs.activate()
            osrs.moveTo(10,10)
            break

get_client()