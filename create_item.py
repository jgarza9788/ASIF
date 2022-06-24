import dearpygui.dearpygui as dpg

def exe():
    with dpg.window(label="Delete Files", modal=True, show=False, id="modal_id", no_title_bar=False):
        dpg.add_text("All those beautiful files will be deleted.\nThis operation cannot be undone!")
        dpg.add_separator()
        dpg.add_checkbox(label="Don't ask me next time")
        with dpg.group(horizontal=True):
            dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("modal_id", show=False))
            dpg.add_button(label="Cancel", width=75, callback=lambda: dpg.configure_item("modal_id", show=False))