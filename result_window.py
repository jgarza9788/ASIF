import dearpygui.dearpygui as dpg

tag = '##text'

def result_window(self):
    with dpg.window(tag=self.result_window,
        label='results',
        no_close=True,
        # no_title_bar=True,
        no_collapse=True
        ):
        pass

        dpg.add_text(
            default_value='{0} / {1} | {2:.2f}%'.format(
                self.filtered_results_count,
                len(self.results),
                (self.filtered_results_count/len(self.results))*100
            ),
            tag=tag)

        # pb = dpg.add_progress_bar(
        #     default_value=1.0,
        #     width=-1,
        #     # height=-1,
        #     height=5,
        #     tag='###progress_bar'
        # )
        # dpg.bind_item_theme(pb,self.mythemes['progress_bar_theme'])

        # self.refresh_results_window()

        # tag = '###'
        # self.result_tags.append(tag)
        # dpg.add_text('please wait',tag=tag)
    self.refresh_results_window()

def update_text(self):
    dpg.configure_item(
        item=tag,
        default_value='{0} / {1} | {2:.2f}%'.format(
            self.filtered_results_count,
            len(self.results),
            (self.filtered_results_count/len(self.results))*100
        ),
        )