from ast import Lambda
import os,re
import functions as funct
import dearpygui.dearpygui as dpg
import theme

import create_item

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

        print(*self.data)

        self.mythemes = {}

        dpg.create_context()

        dpg.create_viewport(
            title='ASIF', 
            width=600, 
            height=800,
            x_pos = 400,
            y_pos = 25,
            )

        # create_item.exe()

        with dpg.font_registry():
            # first argument ids the path to the .ttf or .otf file
            df = os.path.join(self.DIR,'fonts','Hack Regular Nerd Font Complete Mono Windows Compatible.ttf')
            default_font = dpg.add_font(df, 14)
            
        #     with dpg.font(df, 14) as font1:
        #         dpg.add_font_range(0xf600, 0xf1ff)
        #         dpg.add_font_range(0x3100, 0x3ff0)
        #         default_font = font1
                
        #     # with dpg.add_font(df, 14) as font:
        #     #     default_font = font
        dpg.show_font_manager()


        # self.primary_window = dpg.window(tag="Primary Window",no_scrollbar=True)
        # with self.primary_window:
        with dpg.window(tag="#primary_window",no_scrollbar=True):
            dpg.bind_font(default_font)
            
            # dpg.add_button(label="Open Dialog", callback=lambda: dpg.configure_item("modal_id", show=True))

            self.mythemes = theme.get_themes()

            # dpg.add_text("😀😊☺🙄🥱🤧🧐🤓👽👾👻😼😽😽😽😽😽🦓🦓🦓")

            # menu = dpg.add_menu_bar()
            # dpg.add_menu_item(label="add", parent=menu,callback=self.hello)

            with dpg.group(horizontal=True) as row:
                reset_button = dpg.add_button(
                    label="X", 
                    width=20,
                    callback= self.clear, 
                    tag=''
                    )

                fi = dpg.add_input_text(
                    hint='filter (regex)',
                    tag='##filter',
                    width=-1,
                    # pos=(10,7),
                    label="",  
                    callback=self.refresh_results
                    )
                
                # dpg.bind_item_theme(fi,mythemes['filter_theme'])

            pb = dpg.add_progress_bar(
                default_value=1.0,
                width=-1,
                # height=-1,
                height=5,
                tag='##progress_bar'
            )
            dpg.bind_item_theme(pb,self.mythemes['progress_bar_theme'])

            self.refresh_sidepanel()
            self.refresh_results()

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("#primary_window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()

    def clear(self):
        dpg.set_value('##filter','') 
        self.refresh_results()

    def refresh_sidepanel(self):
        tag = '##sidepanel'
        try:
            dpg.delete_item(tag)
        except:
            pass

        cw = dpg.add_child_window(width=150,tag=tag)
        for index,i in enumerate(self.data):
            # print(','.join(i['dirs']))
            # print(i['regex'])

            with dpg.group(horizontal=True,parent=cw) as row:
                b = dpg.add_button(
                    label=i['name'] , 
                    width=135,
                    callback=self.perform_search, 
                    tag=i['name'] + '_' + str(index),
                    parent=row
                    )

                with dpg.tooltip(b):
                    dpg.add_text('name: {0}\ndirs: {1}\nregex: {2}'.format(i['name'],','.join(i['dirs']),i['regex']))
                
                # dpg.add_button(
                #     label="?", 
                #     width=20,
                #     callback= self.clear, 
                #     # tag=''
                #     parent=row
                # )

    def refresh_results(self):
        tag = '##result'
        try:
            dpg.delete_item(tag)
        except:
            pass

        filter_pattern = dpg.get_value('##filter').upper()
        if filter_pattern == None:
            filter_pattern = '.*'

        mw = dpg.add_child_window(
            pos=(160,40),
            tag=tag,
            parent="#primary_window"
            )           
        for index,i in enumerate(self.results):

            self.update_pb(index/len(self.results))

            # print('filter_pattern',filter_pattern)
            # print('i[\'fullpath\']',i['fullpath'])

            if re.search(pattern=filter_pattern,string=i['fullpath'].upper()):


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
                    tag='',
                    parent=mw
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
        self.refresh_results()

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
