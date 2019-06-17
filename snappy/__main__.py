import keyboard

from snappy.hotkeys import configure_default_keybinds
from snappy.systray import configure_systray


def main():
    # Load in default binds
    # TODO: load in user binds as well
    configure_default_keybinds()
    
    # Configure and start systray icon
    configure_systray()

    keyboard.wait()
    

if __name__ == "__main__":
    main()