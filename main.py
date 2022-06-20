import os,re
import functions as funct
import dearpygui.dearpygui as dpg
# https://dearpygui.readthedocs.io/en/latest/index.html



class MainWindow():

    def __init__(self):
        self.DIR = os.path.dirname(os.path.realpath(__file__))
        self.dfile = os.path.join(self.DIR,'data.json')
        self.data = funct.get_data(self.dfile)

        self.config = funct.get_data(os.path.join(self.DIR,'config.json'))
        self.always_exlcude =self.config['always_exclude']
        
        self.results = []
        self.results = funct.search(self.data[0])

        print(*self.data)

        dpg.create_context()

        dpg.create_viewport(
            title='ASIF', 
            width=600, 
            height=800,
            x_pos = 400,
            y_pos = 25,
            )

        # self.primary_window = dpg.window(tag="Primary Window",no_scrollbar=True)
        # with self.primary_window:
        with dpg.window(tag="#primary_window",no_scrollbar=True):
            # dpg.add_text("Hello, world")

            menu = dpg.add_menu_bar()
            dpg.add_menu_item(label="add", parent=menu,callback=self.hello)

            dpg.add_progress_bar(
                default_value=1.0,
                width=-1,
                height=-1,
                #height=3,
                pos=(0,20),
                tag='##progress_bar'
            )

            cw = dpg.add_child_window(width=150)
            for index,i in enumerate(self.data):
                print(','.join(i['dirs']))
                print(i['regex'])
                b = dpg.add_button(
                    label=i['name'] , 
                    width=135,
                    callback=self.perform_search, 
                    tag=i['name'] + '_' + str(index),
                    parent=cw
                    )
                with dpg.tooltip(b):
                    dpg.add_text('name: {0}\ndirs: {1}\nregex: {2}'.format(i['name'],','.join(i['dirs']),i['regex']))

            dpg.add_input_text(hint='filter (regex)',tag='##filter',width=440,pos=(160,25),label="", default_value=".*", callback=self.refresh_results)

            # for x in range(100):
            #     dpg.add_button(label="Reset1", callback=self.hello, tag='',parent=cw)  

            self.refresh_results()


            # with dpg.group(horizontal = False,pos=(10,25)) as vlayout:
            #     for x in range(100):
            #         dpg.add_button(label="Reset1", callback=self.hello, tag='')
            #     dpg.add_button(label="Reset1", callback=self.hello, tag='')
            #     dpg.add_button(label="Reset1", callback=self.hello, tag='')
            #     dpg.add_button(label="Reset1", callback=self.hello, tag='')
            #     dpg.add_button(label="Reset1", callback=self.hello, tag='')
            #     dpg.add_button(label="Reset1", callback=self.hello, tag='')

            # with dpg.group(horizontal = False,pos=(100,25)) as vlayout:
            #     dpg.add_button(label="Reset2", callback=self.hello, tag='')
            #     dpg.add_button(label="Reset2", callback=self.hello, tag='')
            #     dpg.add_button(label="Reset2", callback=self.hello, tag='')
            #     dpg.add_button(label="Reset2", callback=self.hello, tag='')
            #     dpg.add_button(label="Reset2", callback=self.hello, tag='')
            #     dpg.add_button(label="Reset2", callback=self.hello, tag='')


        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("#primary_window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()

    def refresh_results(self):
        tag = '##result'
        try:
            dpg.delete_item(tag)
        except:
            pass

        filter_pattern = dpg.get_value('##filter').upper()
        if filter_pattern == None:
            filter_pattern = '.*'

        mw = dpg.add_child_window(pos=(160,50),tag=tag,parent="#primary_window")           
        for index,i in enumerate(self.results):

            self.update_pb(index/len(self.results))

            print('filter_pattern',filter_pattern)
            print('i[\'fullpath\']',i['fullpath'])

            if re.search(pattern=filter_pattern,string=i['fullpath'].upper()):

                file_str = funct.string_reduce(i['file'],start_percent=0.6)
                dir_str = funct.string_reduce(i['parent_dir'],start_percent=0.6)

                b = dpg.add_button(
                    label=(file_str + '\n' + dir_str + ' '*200)[:150], 
                    user_data=i['fullpath'],
                    width=400,
                    callback=self.open_video, 
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
        self.results = funct.search(self.data[index],self.always_exlcude,callback=self.update_pb)
        self.results = funct.sortby(self.results,reverse=False,column='file')
        self.refresh_results()

    def open_video(self,sender,app_data, user_data):
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
