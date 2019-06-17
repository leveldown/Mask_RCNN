import os
path = 'F:/python/ErosionData/test'  # path为json文件存放的路径
json_file = os.listdir(path)
for file in json_file:
    cmd = str('labelme_json_to_dataset' + ' ' + path + '/' + file)
    os.system(cmd)

