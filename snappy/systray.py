import os

from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw



def configure_systray():

    def setup(icon):
        icon.visible = True

    def exit_action(icon):
        icon.visible = False
        icon.stop()

    image = Image.open(os.path.join("images", "snappy_systray.png"))
    
    icon = Icon("snappy", icon=image, title="snappy")

    menu = Menu(
        MenuItem("exit", lambda: exit_action(icon))
    )
    icon.menu = menu

    icon.run(setup)