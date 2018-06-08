# menus.py

import tdl
import textwrap

def menu(con, root, header, options, width, screen_width, screen_height):
    if len(options) > 26: raise ValueError('Cannot have a menu with more than 26 options.')

    # calc total height for the header and one line per option

    header_wrapped = textwrap.wrap(header, width)
    header_height = len(header_wrapped)
    height = len(options) + header_height + 1
    width += 2

    # create offscreen console that represents the menu's window
    window = tdl.Console(width, height)

    # print the header, with wrapped text
    window.draw_frame(0, 0, width, height, None, fg=None, bg=(120, 120, 120))
    window.draw_rect(1, 1, width-2, height-2, None, fg=None, bg=(40, 40, 40))
    for i, line in enumerate(header_wrapped):
        window.draw_str(1, 0+i, header_wrapped[i], fg=(0,0,0), bg=(120, 120, 120))

    y = header_height
    letter_index = ord('a')
    for option_text in options:
        text = '(' + chr(letter_index) + ') ' + option_text
        window.draw_str(1, y, text, fg=(180, 180, 180), bg=(40, 40, 40))
        y += 1
        letter_index += 1

    # blit the contents of "window" to the root console
    x = screen_width // 2 - width // 2
    y = screen_height // 2 - height // 2
    root.blit(window, x, y, width, height, 0, 0)

def inventory_menu(con, root, header, inventory, inventory_width, screen_width, screen_height):
    # show a menu with each item of the inventory as an option
    if len(inventory.items) == 0:
        options = ['Inventory is empty.']
    else:
        options = [item.name for item in inventory.items]

    menu(con, root, header, options, inventory_width, screen_width, screen_height)