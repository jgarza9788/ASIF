# import dearpygui.dearpygui as dpg

# dpg.create_context()

# with dpg.window(label="about", width=400, height=400):
#     dpg.add_button(label="Press me")
#     dpg.draw_line((0, 10), (100, 100), color=(255, 0, 0, 255), thickness=1)

# # print children
# print(dpg.get_item_children(dpg.last_root()))

# # print children in slot 1
# print(dpg.get_item_children(dpg.last_root(), 1))

# # check draw_line's slot
# print(dpg.get_item_slot(dpg.last_item()))

# dpg.create_viewport(title='Custom Title', width=800, height=600)
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()

##############################################################


# import dearpygui.dearpygui as dpg

# dpg.create_context()

# w = dpg.add_window(label="Main")
# w2 = dpg.add_window(label="Main2",no_move=True,no_resize=True,width=400,height=300,pos=(400,500))
# # w3 = dpg.add_window(label="Main3")


# mb = dpg.add_menu_bar(parent=w)


# themes = dpg.add_menu(label="Themes", parent=mb)
# dpg.add_menu_item(label="Dark", parent=themes)
# dpg.add_menu_item(label="Light", parent=themes)

# other_themes = dpg.add_menu(label="Other Themes", parent=themes)
# dpg.add_menu_item(label="Purple", parent=other_themes)
# dpg.add_menu_item(label="Gold", parent=other_themes)
# dpg.add_menu_item(label="Red", parent=other_themes)

# tools = dpg.add_menu(label="Tools", parent=mb)
# dpg.add_menu_item(label="Show Logger", parent=tools)
# dpg.add_menu_item(label="Show About", parent=tools)

# oddities = dpg.add_menu(label="Oddities", parent=mb)
# dpg.add_button(label="A Button", parent=oddities)
# dpg.add_simple_plot(label="A menu plot", default_value=(0.3, 0.9, 2.5, 8.9), height=80, parent=oddities)

# dpg.create_viewport(title='Custom Title', width=800, height=600)
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()

##############################################################


# import dearpygui.dearpygui as dpg

# dpg.create_context()

# with dpg.window(label="Example Window", width=500, height=150):
#     dpg.add_text("Hello, world")

# dpg.create_viewport(title='Custom Title', width=600, height=200)  # create viewport takes in config options too!

# # must be called before showing viewport
# dpg.set_viewport_small_icon("path/to/icon.ico")
# dpg.set_viewport_large_icon("path/to/icon.ico")

# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()

##############################################################

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)

demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


##############################################################

# import re

# # string = r'D:\Torrents\Movies\V.For.Vendetta.2005.720p.Bluray.x264.DTS.DXVA-FLAWL3SS\V.For.Vendetta.2005.720p.Bluray.x264.DTS.DXVA-FLAWL3SS.mkv'
# strings = [
#     'abbbbbc',
#     'ausdbfayfg',
#     'fasgfdafgadfg'
#     ]

# for s in strings:
#     # if re.search('^.*(?!b).*$',s):
#     # if re.match('^((?!b).)*$',s):
#     if re.match('^.*(?!b).*$',s):
#         print(s,'Y')
#     else:
#         print(s,'N')
