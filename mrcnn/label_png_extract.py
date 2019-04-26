from PIL import Image
import os

files_dir = 'F:/python/ErosionData/labelme_json/'
target_dir = 'F:/python/ErosionData/mask_png/'
count = os.listdir(files_dir)  # get files list in this path
print("count=", len(count))
for i in range(1, len(count) + 1):
    im = Image.open(files_dir + 'rgb_' + str(i) + '_json/' + 'label.png')  # open files named like 'i'
    im.save(target_dir + 'rgb_' + str(i) + '_json_label.png')
