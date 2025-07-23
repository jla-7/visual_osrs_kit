import pyautogui as ag
import pygetwindow as gw
import time
import screenshot

def cursor_pos():
    x, y = ag.position()
    position_str = 'X: '+str(x).rjust(4)+' Y: '+str(y).rjust(4)
    print(position_str+"\n", end='')
    time.sleep(0.5)

def main():
    ag.FAILSAFE = True
    screenshot.get_client()

    time.sleep(2)
    ag.leftClick(751, 502)
    ag.leftClick(751, 502)
    ag.leftClick(751, 502)
    cursor_pos()

if __name__ == "__main__":
    main()