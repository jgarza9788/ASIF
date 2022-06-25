import dearpygui.dearpygui as dpg

def get_themes():

    result = {}

    # with dpg.theme() as red_text_theme:
    #     with dpg.theme_component(dpg.mvAll):
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])

    # with dpg.theme() as yellow_text_theme:
    #     with dpg.theme_component(dpg.mvAll):
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 211, 67])

    # with dpg.theme() as green_text_theme:
    #     with dpg.theme_component(dpg.mvAll):
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, [121, 184, 81])

    # with dpg.theme() as reset_button_theme:
    #     with dpg.theme_component(dpg.mvAll):
            # dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_TabActive, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_Button, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_WindowBg, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_ChildBg, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_DockingPreview, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_Border, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_DockingEmptyBg, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_Header, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_PopupBg, [255, 0, 0])

            # dpg.add_theme_color(dpg.mvThemeCol_PlotLines, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_PlotLinesHovered, [255, 0, 0])

            # dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_FrameBg, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_PlotHistogram, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_Separator, [255, 0, 0])

            # dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_PlotHistogramHovered, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_SeparatorHovered, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_SeparatorActive, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_TitleBg, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_TableBorderStrong, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip, [255, 0, 0])

            # dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_TableBorderLight, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_TableRowBg, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_TableRowBgAlt, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_Tab, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_TabHovered, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_DragDropTarget, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_NavHighlight, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_NavWindowingHighlight, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_CheckMark, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_NavWindowingDimBg, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, [255, 0, 0])
            # dpg.add_theme_color(dpg.mvThemeCol_ModalWindowDimBg, [255, 0, 0])
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, [0, 0, 0])
    #         dpg.add_theme_color(dpg.mvThemeCol_Button, [200, 0, 0])
    #         dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 0, 0])

    with dpg.theme() as progress_bar_theme:
        with dpg.theme_component(dpg.mvAll):

            # dpg.add_theme_color(dpg.mvThemeCol_PlotHistogram, [0, 255, 0])
            dpg.add_theme_color(dpg.mvThemeCol_PlotHistogram, [88, 209, 235])

            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (0, 0, 0,0), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
    result['progress_bar_theme'] = progress_bar_theme

    with dpg.theme() as filter_theme:
        with dpg.theme_component(dpg.mvAll):
            # dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (150, 100, 100,255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
    result['filter_theme'] = filter_theme

    return result