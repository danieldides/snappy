import keyboard
import pygetwindow as gw


TASKBAR_HEIGHT = 32
RESOLUTION = gw._pygetwindow_win.resolution()


def third(window, key):
    third_width = RESOLUTION.width // 3
    left = 0
    middle = third_width
    right = 2*third_width

    if window.width != third_width:
        # Make window height of monitor and one third width
        window.resizeTo(third_width, RESOLUTION.height-TASKBAR_HEIGHT)

    pos = window.left

    if pos == left:
        # Window is along left edge
        if key == "right":
            window.moveTo(middle, 0)
        elif key == "left":
            window.moveTo(right, 0)
    elif pos == middle:
        # Window is in center third
        if key == "right":
            window.moveTo(right, 0)
        elif key == "left":
            window.moveTo(left, 0)
    elif pos == right:
        # Windows is in final third
        if key == "right":
            window.moveTo(left, 0)
        elif key == "left":
            window.moveTo(middle, 0)
    else:
        window.moveTo(0, 0)


def main():
    # Horizontal thirds
    keyboard.add_hotkey("ctrl+win+left", lambda k: third(gw.getActiveWindow(), k), 
                        args=["left"], suppress=True)
    keyboard.add_hotkey("ctrl+win+right", lambda k: third(gw.getActiveWindow(), k), 
                        args=["right"], suppress=True)

    # keyboard.add_hotkey('ctrl+win+right', print, args=["PRESSED"], suppress=True)
    keyboard.wait()
    

if __name__ == "__main__":
    main()