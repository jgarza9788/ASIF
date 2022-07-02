import dearpygui.dearpygui as dpg


def item_window(self):
    with dpg.window(tag=self.item_window,
        label='searches',
        no_close=True,
        # no_title_bar=True,
        no_collapse=True,
        # callback=self.refresh_item_window
        ):
        pass
        dpg.add_button(label='**new**',width=135)

        with dpg.popup(dpg.last_item(),
            mousebutton=dpg.mvMouseButton_Left,
            modal=True,
            ):
            dpg.add_input_text(                    
                hint='name',
                tag='##ns_name',
                width=250,
                # label='Name:'
                )
            with dpg.group(horizontal=True) as row:
                dpg.add_button(
                    label="+", 
                    width=20,
                    # callback= lambda: add_dir(dpg.get_value('##ns_dir')), 
                    tag='##ns_add_dir'
                    )
                dpg.add_input_text(                    
                    hint='directory',
                    tag='##ns_dir',
                    width=222,
                    # label='dirs:'
                    )
            dpg.add_listbox(
                tag='##ns_dirs_list', 
                width=250,
                items=[],
                num_items=3, 
                # callback=log_callback
                )
            dpg.add_input_text(                    
                hint='regex',
                tag='##ns_regex',
                width=250,
                # label='Regex:'
                )
            with dpg.group(horizontal=True) as row:
                dpg.add_button(
                    label='Clear',
                    width=121,
                    # self
                    )
                dpg.add_button(
                    label='Add',
                    width=121,
                    # callback=self.add_new_search
                    )

    self.refresh_item_window()
    
        # tag = '###'
        # self.result_tags.append(tag)
        # dpg.add_text('please wait',tag=tag)
        # self.refresh_item_window()