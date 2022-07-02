
import os,re,json
from datetime import datetime

DIR = os.path.dirname(os.path.realpath(__file__))

def string_reduce(string,limit=50,start_percent=0.5):

    if limit < 20:
        return string

    if len(string) >= limit:
        spn = int(limit*(1.0-start_percent))
        return string[:limit-spn] + '...' + string[-(spn-3):]
    else:
        return string

def get_data(file):
    try:
        with open(file,'r',encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def set_data(data,file):
    # self.sort()
    with open(file,'w',encoding='utf-8') as f:
        json.dump(data,f,indent=4)
        

def save(data,file):
    set_data(data,file)

def check_search_00(i):
    keys = list(i.keys())

    if 'dirs' in keys and 'regex' in keys and 'name' in keys:
        return True
    else:
        return False

def convertUnixDateTime(t,return_as_int = True):
    dt = datetime.utcfromtimestamp(t)
    y = dt.strftime('%Y')
    m = dt.strftime('%m')
    d = dt.strftime('%d')
    H = dt.strftime('%H')
    M = dt.strftime('%M')
    # S = dt.strftime('%S')
    if return_as_int == False:
        return '{0}.{1}.{2} {3}:{4}'.format(y,m,d,H,M)
    else:
        return int(''.join([y,m,d,H,M]))


def sortby(this_list,reverse=False,column='file'):
    def _sortby(i):
        return i[column]
    this_list.sort(key=_sortby,reverse=reverse)
    return this_list

def search(item,callback=None):
    # https://www.tutorialspoint.com/python/os_stat.htm

    if check_search_00(item) == False:
        return 0

    result = []
    for d in item['dirs']:

        wlength = len(list(os.walk(d)))
        for index,(root,dirs,files) in enumerate(os.walk(d)):

            if callback != None:
                try:
                    callback(index/wlength)
                except:
                    pass

            for file in files:

                if file.startswith('.'):
                    continue

                if re.search(pattern=item['regex'],string=file):
                    f = os.path.join(root,file)
                    result.append(
                        {
                            'file': file,
                            'parent_dir':root,
                            'fullpath':f,
                            'created': convertUnixDateTime(os.stat(f).st_ctime,True)
                        }
                        )
    return result


# def get_icon(file_name):
#     from icon_dict import icon_dict
#     try:
#         return icon_dict[file_name.split('.')[-1]]
#     except:
#         return '\uf0c8'


if __name__ == '__main__':
    # import pprint as pp
    i = {
        'name': 'movies',
        'dirs':['D:\Torrents\Movies','D:\Torrents\Shows'],
        'regex':'(\.avi$|\.flv$|\.wmv$|\.mov$|\.mp4|\.mkv$|\.)',
        'used_count':0
        }
    # i = {
    #     'name': 'movies',
    #     'dirs':['C:\\Users\\JGarza\\GitHub'],
    #     # 'regex':'^((?!venv).).*main\.py$',
    #     'regex':'main.py$',
    #     'used_count':0
    #     }
    # # main()
    results = search(i)
    results = sortby(results)
    # print(*results,sep='\n\n')
    for r in results:
        # print(r['fullpath'])
        print(get_icon(r['file']))

    # i = [
    #         {
    #             'name': 'movies',
    #             'dirs':['D:\Torrents\Movies'],
    #             'regex':'(\.avi$|\.flv$|\.wmv$|\.mov$|\.mp4|\.mkv$)',
    #             'used_count':0
    #         },
    #         {
    #             'name': 'shows',
    #             'dirs':['D:\Torrents\Shows'],
    #             'regex':'(\.avi$|\.flv$|\.wmv$|\.mov$|\.mp4|\.mkv$)',
    #             'used_count':0
    #         },
    #         {
    #             'name': 'csharp',
    #             'dirs':[r'C:\Users\JGarza\GitHub'],
    #             'regex':'\.cs$',
    #             'used_count':0
    #         }
    #     ]

    # save(data=i,file=os.path.join(DIR,'data.json'))