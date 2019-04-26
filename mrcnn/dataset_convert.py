import os
path = 'F:/python/ErosionData/json'  # path为json文件存放的路径
json_file = os.listdir(path)
for file in json_file:
    os.system(""
              " %s" % (path + '/' + file))