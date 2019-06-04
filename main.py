import keyboard
import pygetwindow as gw


TASKBAR_HEIGHT = 32
RESOLUTION = gw._pygetwindow_win.resolution()
FULL_HEIGHT = RESOLUTION.height-TASKBAR_HEIGHT


def h_third(window, key):
    """ Snap to horizontally tiled thirds """
    third_width = RESOLUTION.width // 3
    left = 0
    middle = third_width
    right = 2*third_width

    if window.width != third_width:
        # Make window height of monitor and one third width
        window.resizeTo(third_width, FULL_HEIGHT)

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


def v_third(window, key):
    """ Snap to vertically tiled thirds """
    third_height = RESOLUTION.height // 3
    top = 0
    middle = third_height
    bottom = 2*third_height

    if window.width != third_height:
        # Make window width of monitor and one third height
        window.resizeTo(RESOLUTION.width, third_height)

    pos = window.top

    if pos == top:
        # Window is along top edge
        if key == "up":
            window.moveTo(0, bottom)
        elif key == "down":
            window.moveTo(0, middle)
    elif pos == middle:
        # Window is in center third
        if key == "up":
            window.moveTo(0, top)
        elif key == "down":
            window.moveTo(0, bottom)
    elif pos == bottom:
        # Windows is in bottom third
        if key == "up":
            window.moveTo(0, middle)
        elif key == "down":
            window.moveTo(0, top)
    else:
        window.moveTo(0, 0)


def half(window, key):
    """ 
    Snap to left or right half of display
    Repeating the command grows the window to 2/3
    """
    half_width = RESOLUTION.width // 2
    third_width = RESOLUTION.width // 3
    left = 0
    right = half_width

    if window.width != half_width:
        window.resizeTo(half_width, FULL_HEIGHT)
    elif window.width == half_width:
        window.resizeTo(2*third_width, FULL_HEIGHT)

    pos = window.left

    if key == "left":
        window.moveTo(left, 0)
    elif key == "right":
        if window.width == half_width:
            window.moveTo(right, 0)
        elif window.width == 2*third_width:
            window.moveTo(third_width, 0)


def center(window):
    """ Center the window, leave width as is """
    remaining_width = RESOLUTION.width - window.width
    gaps_width = remaining_width // 2
    
    remaining_height = FULL_HEIGHT - window.height
    gaps_height = remaining_height // 2
    window.moveTo(gaps_width, gaps_height)


def main():
    # Horizontal thirds
    keyboard.add_hotkey("ctrl+win+left", lambda k: h_third(gw.getActiveWindow(), k), 
                        args=["left"], suppress=True)
    keyboard.add_hotkey("ctrl+win+right", lambda k: h_third(gw.getActiveWindow(), k), 
                        args=["right"], suppress=True)

    # Veritcal thirds
    keyboard.add_hotkey("ctrl+win+up", lambda k: v_third(gw.getActiveWindow(), k), 
                        args=["up"], suppress=True)
    keyboard.add_hotkey("ctrl+win+down", lambda k: v_third(gw.getActiveWindow(), k), 
                        args=["down"], suppress=True)


    # left and right halves (or 2/3rds)
    keyboard.add_hotkey("alt+win+left", lambda k: half(gw.getActiveWindow(), k), 
                        args=["left"], suppress=True)
    keyboard.add_hotkey("alt+win+right", lambda k: half(gw.getActiveWindow(), k), 
                        args=["right"], suppress=True)

    # Center window
    keyboard.add_hotkey("alt+win+c", lambda: center(gw.getActiveWindow()), 
                        suppress=True)

    # TODO
    # Multimonitor support (send to next monitor)
    # keyboard.add_hotkey("ctrl+win+alt+left", lambda k: next_monitor(gw.getActiveWindow()), 
    #                     args=["left"], suppress=True)
    # keyboard.add_hotkey("ctrl+win+alt+right", lambda k: next_monitor(gw.getActiveWindow()), 
    #                     args=["right"], suppress=True)

    keyboard.wait()
    

if __name__ == "__main__":
    main()