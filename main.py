import keyboard
import pygetwindow as gw


TASKBAR_HEIGHT = 32
RESOLUTION = gw._pygetwindow_win.resolution()
FULL_HEIGHT = RESOLUTION.height-TASKBAR_HEIGHT


def third(window, key):
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


def half(window, key):
    """ Snap to left or right half of display """
    half_width = RESOLUTION.width // 2
    left = 0
    right = half_width

    if window.width != half_width:
        window.resizeTo(half_width, FULL_HEIGHT)

    if key == "left":
        window.moveTo(left, 0)
    elif key == "right":
        window.moveTo(right, 0)


def center(window):
    """ Center the window, leave width as is """
    remaining_width = RESOLUTION.width - window.width
    gaps_width = remaining_width // 2
    
    remaining_height = FULL_HEIGHT - window.height
    gaps_height = remaining_height // 2
    window.moveTo(gaps_width, gaps_height)


def main():
    # Horizontal thirds
    keyboard.add_hotkey("ctrl+win+left", lambda k: third(gw.getActiveWindow(), k), 
                        args=["left"], suppress=True)
    keyboard.add_hotkey("ctrl+win+right", lambda k: third(gw.getActiveWindow(), k), 
                        args=["right"], suppress=True)

    # left and right halves
    keyboard.add_hotkey("alt+win+left", lambda k: half(gw.getActiveWindow(), k), 
                        args=["left"], suppress=True)
    keyboard.add_hotkey("alt+win+right", lambda k: half(gw.getActiveWindow(), k), 
                        args=["right"], suppress=True)

    # Center window
    keyboard.add_hotkey("alt+win+c", lambda: center(gw.getActiveWindow()), 
                        suppress=True)

    keyboard.wait()
    

if __name__ == "__main__":
    main()