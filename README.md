# Quicknote
An application made to allow for note-taking one button press away. 

## How to use
The application was designed and tested for Linux with the Ubuntu distibution. 
But it should in theory still work on Windows and Mac based systems as they
are compatible with Python's tkinter. 

To launch the program run `python3 <some_path>/quicknote/main.py` in a 
terminal, where `python3` should be your Python installation in PATH. 

The program can be executed in two ways. Either begining in `note mode` or 
`menu mode`. To enter `menu_mode` pass the `-m` flag when running the program.

### Program Keybinds
| Mode | Keybind | Action |
|------|---------|--------|
| Menu | `<Escape>`, `q` | Exit |
| Menu | `<Return>` | Exit and save |
| Menu | `j` | Move down |
| Menu | `k` | Move up |
| Menu | `d` | Mark for removal |
| Menu | `n` | Open note mode |
| Menu | `y` | Copy the current row |
| Note | `<Escape>`, `q` | Exit |
| Note | `<Return>` | Exit and save |
| Note | `<Control-m>` | Open menu mode |


## Requirements
Tested for Python 3.10.12.

### Dependencies
* Tkinter
* Pyperclip

