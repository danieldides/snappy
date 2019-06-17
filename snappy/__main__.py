import keyboard

from snappy.hotkeys import configure_default_keybinds


def main():
    configure_default_keybinds()

    keyboard.wait()
    

if __name__ == "__main__":
    main()