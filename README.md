![snappy banner](images/banner.png)

# Snappy
A Windows "port" of [Spectacle](https://github.com/eczarny/spectacle) for Mac.

`Snappy` aims to provide more or less the same functionality of Spectacle on Windows.
Most of the keybinds are the exact same.

## Running
To run Snappy: 

1. Create a virtualenv: `pipenv --three`
2. Install all the dependencies with `pipenv install`
3. `python -m snappy`

To quit snappy, right click the systray icon and select "exit". 

## Keybinds
- `ctrl+win+left/right` snap to nearest full-height third
- `ctrl+win+up/down` snap to nearest full-width third
- `alt+win+left/right` snap to left or right half
- `alt+win+left/right` x 2 snap to left or right 2/3rds
- `alt+win+up/down` snap to top or bottom half
- `alt+win+up/down` x 2 snap to top or bottom 2/3rds
- `alt+win+c` center window