import os
from glob import glob
from sklearn.model_selection import train_test_split

name = 'busi'

root = r'/data/' + name
print(root)

img_ids = glob(os.path.join("/home/ankita/Multi-Level-Global-Context-Cross-Consistency"+root, 'images', '*.png'))
# print(img_ids)
img_ids = [os.path.splitext(os.path.basename(p))[0] for p in img_ids]
   
count = 1
for i in [41, 64, 1337]:
    train_img_ids, val_img_ids = train_test_split(img_ids, test_size=0.3, random_state=i)
    filename = "/home/ankita/Multi-Level-Global-Context-Cross-Consistency"+root + '/{}_train{}.txt'.format(name, count)
    # print(filename)
    with open(filename, 'w') as file:
        for i in train_img_ids:
            file.write(i + '\n')

    filename = "/home/ankita/Multi-Level-Global-Context-Cross-Consistency"+root + '/{}_val{}.txt'.format(name, count)
    with open(filename, 'w') as file:
        for i in val_img_ids:
            file.writelines(i + '\n' )

    print(train_img_ids)
    print(val_img_ids)
    count += 1
#/home/tej/workplace/Multi-Level-Global-Context-Cross-Consistency/data/busi/images