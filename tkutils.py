from const import *

def center_window(window, y_scale=0.1):
    window.update_idletasks()

    w_width, w_height = window.winfo_width(), window.winfo_height()
    s_width, s_height = SCREEN_WIDTH, SCREEN_WIDTH
    w_width = SCREEN_WIDTH - int(SCREEN_WIDTH/3)
    inv_y_scale = int(1 / y_scale)
    
    x_pos = s_width // 2 - w_width // 2
    y_pos = s_height // inv_y_scale - w_height // 2

    window.geometry(f"{w_width}x{w_height}+{x_pos}+{y_pos}")
