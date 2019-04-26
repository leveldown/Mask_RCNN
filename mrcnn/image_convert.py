from PIL import Image
import os

images_dir = 'F:/python/ErosionData/rgb/'
count = os.listdir(images_dir)  # get files list in this path
print("count=", len(count))
n = 1
for j in count:
    oldname = os.path.join(images_dir, j)
    newname = os.path.join(images_dir, 'rgb_' + str(n) + '.jpg')
    os.rename(oldname, newname)
    n += 1

for i in range(1, len(count) + 1):
    im = Image.open(images_dir + 'rgb_' + str(i) + '.jpg')  # open files named like 'i'
    im_size = im.size
    # print("图片宽度和高度分别是{}".format(im_size))
    if (im_size[0] > im_size[1]):
        im = im.resize((1280, 896))
        im.save(images_dir + 'rgb_' + str(i) + '.jpg')
    else:
        im = im.resize((1280, 896))
        im.save(images_dir + 'rgb_' + str(i) + '.jpg')
