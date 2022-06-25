left_window = dpg.generate_uuid()
right_window = dpg.generate_uuid()
top_window = dpg.generate_uuid()
bottom_window = dpg.generate_uuid()
center_window = dpg.generate_uuid()

with dpg.window(label="Left", id=left_window):
    pass

with dpg.window(label="Right", id=right_window):
    pass

with dpg.window(label="Top", id=top_window):
    pass

with dpg.window(label="Bottom", id=bottom_window):
    pass

with dpg.window(label="Center", id=center_window):
    pass

with dpg.window(label="Temporary Window"):
    dpg.ad