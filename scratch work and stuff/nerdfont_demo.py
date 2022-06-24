
import os
import dearpygui.dearpygui as dpg

DIR = os.path.dirname(os.path.realpath(__file__))

dpg.create_context()

dpg.create_viewport(
    title='nerd font demo', 
    width=600, 
    height=800,
    x_pos = 400,
    y_pos = 25,
    )

with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    df = os.path.join(DIR,'fonts','Hack Regular Nerd Font Complete Mono Windows Compatible.ttf')
    
    with dpg.font(df, 14) as font1:
        dpg.add_font_range(0xf600, 0xf1ff)
#         dpg.add_font_range(0x3100, 0x3ff0)
#         default_font = font1
#     # with dpg.add_font(df, 14) as font:
#     #     default_font = font
    default_font = dpg.add_font(df, 14)

dpg.show_font_manager()


with dpg.window(tag="#primary_window",no_scrollbar=True):
    dpg.bind_font(default_font)
    dpg.add_text('hello world \uf883 0xf883 ')
    dpg.add_text('hello world \uf883 \xef\x99\x82 \ \ufd11 U+f642 0xf883')
    dpg.add_text(r"")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("#primary_window", True)
dpg.start_dearpygui()
dpg.destroy_context()