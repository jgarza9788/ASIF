from ast import Lambda
import os,re
import functions as funct
import dearpygui.dearpygui as dpg
import theme

import shutil
# import create_item

# https://dearpygui.readthedocs.io/en/latest/index.html



class MainWindow():

    def __init__(self):
        self.DIR = os.path.dirname(os.path.realpath(__file__))
        self.dfile = os.path.join(self.DIR,'data.json')
        self.data = funct.get_data(self.dfile)

        # self.config = funct.get_data(os.path.join(self.DIR,'config.json'))
        # self.always_exlcude =self.config['always_exclude']
        
        self.results = []
        self.results = funct.search(self.data[0])

        # print(*self.data)

        self.mythemes = {}

        
        # uc_layout = os.path.join(self.DIR,'user_custom_layout.ini')
        c_layout = os.path.join(self.DIR,'layout.ini')
        # if not os.path.exists(uc_layout):
        #     shutil.copy(c_layout, uc_layout)

        dpg.create_context()
        self.mythemes = theme.get_themes()

        dpg.configure_app(
            docking=True, 
            docking_space=True,
            load_init_file=c_layout
            ) 
        
        dpg.create_viewport(title='ASIF', width=600, height=800,x_pos = 400,y_pos = 25,)

        with dpg.viewport_menu_bar():
            
            with dpg.menu(label="Settings"):
                dpg.add_menu_item(label="Save Layout", 
                    callback=lambda: dpg.save_init_file(c_layout), 
                    )

        dpg.setup_dearpygui()


        self.filter_window = dpg.generate_uuid()
        self.item_window = dpg.generate_uuid()
        self.items_tags = []
        self.result_window = dpg.generate_uuid()
        self.result_tags = []

        with dpg.window(tag=self.filter_window,
            # label='filter_window',
            no_close=True,
            no_title_bar=True,
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

        
        with dpg.window(tag=self.item_window,
            # label='search_items',
            no_close=True,
            no_title_bar=True,
            no_collapse=True
            ):
            self.refresh_item_window()


        with dpg.window(tag=self.result_window,
            # label='results',
            no_close=True,
            no_title_bar=True,
            no_collapse=True
            ):
            self.refresh_results_window()



        dpg.show_viewport()

        # dpg.set_primary_window("#primary_window", True)
        # dpg.start_dearpygui()

        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
        dpg.destroy_context()

    def clear(self):
        dpg.set_value('##filter','') 
        self.refresh_results_window()

    def delete_ui_objects(self,tag_list):
        for tag in tag_list:
            try:
                dpg.delete_item(tag)
            except:
                pass

    def refresh_item_window(self):
        self.delete_ui_objects(self.items_tags)

        # with self.item_window:

        for index,i in enumerate(self.data):
            # print(','.join(i['dirs']))
            # print(i['regex'])

            tag = i['name'] + '_' + str(index)
            self.items_tags.append(tag)

            with dpg.group(horizontal=True,parent=self.item_window):
                b = dpg.add_button(
                    label=i['name'] , 
                    width=135,
                    callback=self.perform_search, 
                    tag=i['name'] + '_' + str(index),
                    )

                with dpg.tooltip(b):
                    dpg.add_text('name: {0}\ndirs: {1}\nregex: {2}'.format(i['name'],','.join(i['dirs']),i['regex']))
                    # dpg.add_text('name: {0}'.format(i['name']))
                    # dpg.add_text('dirs: {0}'.format(','.join(i['dirs'])))
                    # dpg.add_text('regex: {0}'.format(i['regex']))
                
                # dpg.add_button(
                #     label="?", 
                #     width=20,
                #     callback= self.clear, 
                #     # tag=''
                #     parent=row
                # )

    def refresh_results_window(self):
        self.delete_ui_objects(self.result_tags)

        filter_pattern = '.*'
        try:
            filter_pattern = dpg.get_value('##filter').upper()
            if filter_pattern == None:
                filter_pattern = '.*'
        except:
            pass

        for index,i in enumerate(self.results):

            self.update_pb(index/len(self.results))

            # print('filter_pattern',filter_pattern)
            # print('i[\'fullpath\']',i['fullpath'])

            if re.search(pattern=filter_pattern,string=i['fullpath'].upper()):

                tag = i['file'] + str(index)
                self.result_tags.append(tag)

                # icon = funct.get_icon(i['file'])
                # icon = '🍿'
                file_str = funct.string_reduce(i['file'],start_percent=0.6)
                dir_str = funct.string_reduce(i['parent_dir'],start_percent=0.6)

                b = dpg.add_button(
                    # label=(file_str + '\n' + dir_str + ' '*200)[:150], 
                    label=(f"{file_str}\n{dir_str}" + " "*200)[:150],
                    user_data=i['fullpath'],
                    width=400,
                    callback=self.open_item, 
                    tag=tag,
                    parent=self.result_window
                    )  
                with dpg.tooltip(b):
                    dpg.add_text('file: {0}\ndir: {1}\ncreated: {2}'.format(i['file'],i['parent_dir'],str(i['created'])))
        
        self.update_pb(0)

    def update_pb(self,value):
        dpg.set_value('##progress_bar',value)

    def perform_search(self,sender):
        s = sender.split('_')
        name,index = s[0], int(s[1])
        print(name,index)
        print(self.data[index])
        self.data[index]['used_count'] += 1
        funct.save(data=self.data,file=self.dfile)
        self.results = funct.search(self.data[index],callback=self.update_pb)
        self.results = funct.sortby(self.results,reverse=False,column='file')
        self.refresh_results_window()

    def open_item(self,sender,app_data, user_data):
        print(sender)
        print(user_data)
        os.startfile(user_data)

    def hello(self):
        print('hello')


if __name__ == "__main__":
    MW = MainWindow()

    # import dearpygui.dearpygui as dpg

    # dpg.create_context()

    # with dpg.window(tag="Primary Window"):
    #     dpg.add_text("Hello, world")

    # dpg.create_viewport(title='Custom Title', width=600, height=200)
    # dpg.setup_dearpygui()
    # dpg.show_viewport()
    # dpg.set_primary_window("Primary Window", True)
    # dpg.start_dearpygui()
    # dpg.destroy_context()
