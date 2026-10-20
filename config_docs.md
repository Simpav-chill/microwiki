# config documentation

it is a list all values in config(on linux: ~/.config/microwiki/config.json, on mac: ~/Library/Application Suport/Microwiki/config.json):

wikistorage value - path to directory with all notes/wikis

theme value - theme to set after running microwiki

editor - what editor will open on hotkey(`open_editor` hotkey in config) in wiki - set to "Built-in" if you dont need external editor or to editor command(example: for neovim set to "nvim")

css_path - path to a custom .tcss file, set to "Default" if you want a default stylesheet

language - a language to use ine ditor, currently only russian and english are available.

keymap - a dictionary with following values:

- force_mod - a modifier to force perform action(used in some cases when widget grabbing focus on himself, not for all keybinds)

- go_back - a hotkey to go back in UI

- open_fm - a hotkey to open built-in wiki file manager

- confirm - a hotkey to confirm action

- rename - a hotkey to rename file/wiki

- delete - a hotkey to delete file/wiki

- create - a hotkey to create file/wiki

- open_editor - a hotkey to open vuilt in or external editor

- write_changes - a hotkey to write changes to file

- movement - a another dictionary in `keymap` dictionary with movement keymaps, here ios all values in it:

- - up - move up
- - down - move down
- - left - move left
- - right - move right

