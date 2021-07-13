import os
from pathlib import Path
import errno
import sys

ERROR_INVALID_NAME = 123


    # https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta
    
    
def is_pathname_valid(pathname: str) -> bool:
    
    try:
        fpath = pathname
        if not isinstance(pathname, str) or not pathname:
            return False

        
        _, pathname = os.path.splitdrive(pathname)

       
        root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
            if sys.platform == 'win32' else os.path.sep
        assert os.path.isdir(root_dirname)   

        
        root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep
        
        
        for pathname_part in pathname.split(os.path.sep):
            try:
                os.lstat(root_dirname + pathname_part)
            
            except OSError as exc:
                if hasattr(exc, 'winerror'):
                    if exc.winerror == ERROR_INVALID_NAME:
                        return False
                elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                    return False

        if sys.platform == 'win32':
            pathValid = False
            pathValid = os.path.exists(fpath[0:2])
            return pathValid
    
    except TypeError as exc:
        return False
    
    else:
        return True


def create_Folder(parent_dir, name):
    Path(os.path.join(parent_dir , name)).mkdir(parents=True, exist_ok=True)

def numerotate(num, l):
    ans = str(num)
    o = ''
    i = len(ans)
    while i < l:
        o += '0'
        i += 1
    ans = o + ans
    return ans

# def create_Folder(parent_dir , name):
    # path = os.path.join(parent_dir , name)
    # try:
        # os.mkdir(path)
    # except OSError as error:
        # print(error)
  
def delete_dot(str):
    if(str[-1] != '.'):
        return str
    return delete_dot(str[:-1])
                

def ref_str(str):
    test_list = [':', '\\' , '<' , '>' , '/' , '?' ,'*' , '|', '\"']
    
    for ele in test_list:
        if(ele in str):
            str = str.replace(ele, ' ')
    
    str = str[:250]
    return delete_dot(str)
    

def interval(str):

    s = str.strip().split(';')
    vect = []
    
    for i in range(len(s)):          
        if s[i].strip().isdigit():
            vect.append(int(s[i].strip()))
            
        else:
            tab = s[i].strip().split('-')
            
            if tab[0].strip().isdigit() and tab[1].strip().isdigit():
                Min = min(int(tab[0].strip()), int(tab[1].strip()))
                Max = max(int(tab[0].strip()), int(tab[1].strip()))
                
                for k in range(Min,Max+1):
                    vect.append(k)
                    
                    
    return vect
    
    
def divide(num, by):       
    count = num / by
    tab = [0,num]

    if not float(count).is_integer():
        count += 1
    
    count = int(count)
    if count > 1:
        tab.clear()
        for i in range(count):
            tab.append(i*by)
        tab.append(num)
    
    return tab

# [print(i) for i in divide(100, 32)]
# print(ref_str("☆#èù~~,;mAma"))
# print(numerotate(999,3))
# print(is_pathname_valid(input("path")))
# create_Folder(input("path: "), 'xxx')










# print(delete_dot("[Maimu-Maimu] Kanojo no Mama wa Boku no SeFrie..."))
