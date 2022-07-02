
import dearpygui.dearpygui as dpg

dirs = []

def add_dir(d):
    dirs.append(d)
    print(d)

def new_search_window(self):
    with dpg.window(
        tag=self.new_search_window,
        label='new search',
        # width=500,
        # height=500,
        show=True
        # no_close=True,
        # no_title_bar=True,
        # no_collapse=True
        ):
        # dpg.add_text('hello')
        dpg.add_input_text(                    
            hint='name',
            tag='##ns_name',
            width=-1,
            label='Name:'
            )
        with dpg.group(horizontal=True) as row:
            dpg.add_button(
                label="+", 
                width=20,
                callback= lambda: add_dir(dpg.get_value('##ns_dir')), 
                tag='##ns_add_dir'
                )
            dpg.add_input_text(                    
                hint='directory',
                tag='##ns_dir',
                width=-1,
                label='dirs:'
                )
        dpg.add_listbox(
            tag='##ns_dirs_list', 
            width=-1,
            items=dirs,
            num_items=3, 
            # callback=log_callback
            )
        dpg.add_input_text(                    
            hint='regex',
            tag='##ns_regex',
            width=-1,
            label='Regex:'
            )
        with dpg.group(horizontal=True) as row:
            dpg.add_button(
                label='Clear',
                width=100,
                # self
                )
            dpg.add_button(
                label='Add',
                width=100,
                # callback=self.add_new_search
                )
