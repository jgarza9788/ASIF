import dearpygui.dearpygui as dpg



def menu(self):
    with dpg.viewport_menu_bar():

        # with dpg.menu(label='File'):
        #     # with dpg.add_menu_item(label='new Search'):
        #     with dpg.popup(label="Delete?", modal=True):
        #         dpg.add_text('hello')


            # with dpg.add_menu_item(
            #     label='new Search'
            #     #,
            #     # callback=lambda: self.show_window(self.new_search_window)
            #     ):
            #     with dpg.popup("Delete..##modals##demo", "Delete?", modal=True):
            #         dpg.add_text('hello')

        with dpg.menu(label="Settings"):
            
            dpg.add_menu_item(label="Save Layout", 
                callback=lambda: dpg.save_init_file(self.layout), 
                )