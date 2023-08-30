import tkinter as tk
import pyperclip

from tkutils import center_window
from const import *
from note import quick_note

menu_index = 0

def load_notes(path):
    file = open(path, "r")
    notes = []
    for line in file:
        line = line.strip("\n")
        notes.append(line)
    return notes

def save_notes(path, notes):
    file = open(path, "w")
    for note in notes:
        file.write(note+"\n")
    file.close()

def main_menu(path):
    notes = load_notes(path)
    
    window = tk.Tk()
    window.title("Quicknote")

    window.configure(bg=BG_GREY)

    note_lbls = []

    def on_exit_pressed(event):
        window.destroy()

    def on_save(event):
        items_removed = 0
        for i, label in enumerate(note_lbls):
            if label["font"] == "Consolas 20 overstrike":
                del notes[i-items_removed]
                items_removed += 1
        save_notes(path, notes)
        window.destroy()

    def on_down_pressed(event):
        global menu_index
        if menu_index < 0:
            return
        highlight_label(menu_index)
        if menu_index < len(note_lbls)-1:
            menu_index += 1
        else:
            menu_index = 0
        highlight_label(menu_index)

    def on_up_pressed(event):
        global menu_index
        if menu_index < 0:
            return
        highlight_label(menu_index)
        if menu_index > 0:
            menu_index -= 1
        else:
            menu_index = len(note_lbls)-1
        highlight_label(menu_index)

    def on_delete_pressed(event):
        global menu_index
        mark_label(menu_index)

    def on_new_pressed(event):
        window.destroy()
        quick_note(path)

    def on_yank_pressed(event):
        global menu_index
        pyperclip.copy(notes[menu_index])

    def mark_label(index):
        if note_lbls[index]["font"] == "Consolas 20":
            note_lbls[index]["font"] = ("Consolas", 20, "overstrike")
        else:
            note_lbls[index]["font"] = ("Consolas", 20)
        note_lbls[index].pack()

    def highlight_label(index):
        if note_lbls[index]["relief"] == "solid":
            note_lbls[index]["relief"] = "ridge"
        else:
            note_lbls[index]["relief"] = "solid"
        note_lbls[index].pack()

    for i in range(len(notes)):
        note_lbls.append(tk.Label(text=notes[i], fg=FG_WHITE, bg=BG_GREY,
            font=("Consolas", 20), relief="solid", borderwidth=5))
        note_lbls[i].pack()
    
    center_window(window, 0.2)

    window.bind("<Escape>", on_exit_pressed)
    window.bind("q", on_exit_pressed)
    window.bind("<Return>", on_save)
    window.bind("j", on_down_pressed)
    window.bind("k", on_up_pressed)
    window.bind("d", on_delete_pressed)
    window.bind("n", on_new_pressed)
    window.bind("y", on_yank_pressed)

    highlight_label(menu_index)

    window.mainloop()
