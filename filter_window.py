import dearpygui.dearpygui as dpg


def filter_window(self):
    with dpg.window(tag=self.filter_window,
        label='filter',
        no_close=True,
        # no_title_bar=True,
        no_collapse=True
        ):
        with dpg.group(horizontal=True) as row:
            reset_button = dpg.add_button(
                label="X", 
                width=20,
                callback= self.clear, 
                tag=''
                )
            # dpg.bind_item_theme(fi,self.mythemes['filter_theme'])

            fi = dpg.add_input_text(
                hint='filter (regex)',
                tag='##filter',
                width=-1,
                # pos=(10,7),
                label="",  
                callback=self.refresh_results_window
                )
        
        dpg.bind_item_theme(fi,self.mythemes['filter_theme'])
        pb = dpg.add_progress_bar(
            default_value=1.0,
            width=-1,
            # height=-1,
            height=5,
            tag='##progress_bar'
        )
        dpg.bind_item_theme(pb,self.mythemes['progress_bar_theme'])