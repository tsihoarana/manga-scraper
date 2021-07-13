import requests
import dir
import os

def download(path, folder_Name, url):
    folder_Name = dir.ref_str(folder_Name)
    dir.create_Folder(path, folder_Name)
    save_path = (path + '\\' + folder_Name).replace('\\', '/') + '/'
    r = requests.get(url, stream=True)
    filename = folder_Name + ".zip"
    with open(save_path + filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 256):
            if chunk:
                f.write(chunk)

def test_code(code, it : int, key):
	res = it
	if(it > len(code) - 1):
		return 0
	if code[it] == key:
		res += 1
		return res
	else:
		if key == code[0]:
			return 1
		return 0

def last_downloaded(path: str)->int:
    arr = []
    img_ext = [".jpg", ".png"]
    for root, dirs, files in os.walk(path):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in img_ext:
                try:
                   arr.append(int(os.path.splitext(file)[0]))
                except ValueError:
                    continue

    if len(arr) == 0:
    	return 0
    return max(arr)
