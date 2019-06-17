import keyboard
import pygetwindow as gw

from .sizes import center, h_third, v_third, half


def configure_default_keybinds():
    """ Configure the default Spectacle keybinds """
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

    # Top and bottom halves (or 2/3rds)
    keyboard.add_hotkey("alt+win+up", lambda k: half(gw.getActiveWindow(), k), 
                        args=["up"], suppress=True)
    keyboard.add_hotkey("alt+win+down", lambda k: half(gw.getActiveWindow(), k), 
                        args=["down"], suppress=True)

    # Center window
    keyboard.add_hotkey("alt+win+c", lambda: center(gw.getActiveWindow()), 
                        suppress=True)

    # TODO
    # Multimonitor support (send to next monitor)
    # keyboard.add_hotkey("ctrl+win+alt+left", lambda k: next_monitor(gw.getActiveWindow()), 
    #                     args=["left"], suppress=True)
    # keyboard.add_hotkey("ctrl+win+alt+right", lambda k: next_monitor(gw.getActiveWindow()), 
    #                     args=["right"], suppress=True)