import json, os, shutil


def unpack(base_dir, 
           target_dir, 
           train='ILSVRC2012_img_train.tar', 
           val='ILSVRC2012_img_val.tar',
           class_json='ImageNet_class_index.json',
           val_label='ImageNet_val_label.txt'):
    
    # path
    train_dir = os.path.join(base_dir, train)
    val_dir   = os.path.join(base_dir, val)
    json_dir  = os.path.join(base_dir, class_json)
    txt_dir   = os.path.join(base_dir, val_label)

    target_train_dir = os.path.join(target_dir, 'train')
    target_val_dir   = os.path.join(target_dir, 'val')

    # dictionary for class to num
    class2num = {}
    with open(json_dir) as json_file:
        json_data = json.load(json_file)
        for num in json_data:
            class2num[json_data[num][0]] = num
    
    # unzip train dataset
    shutil.unpack_archive(train_dir, target_train_dir)
    for class_zip in sorted(os.listdir(target_train_dir)):
        class_, _ = class_zip.split('.')
        shutil.unpack_archive(os.path.join(target_train_dir, class_zip), 
                              os.path.join(target_train_dir, class2num[class_]))
        os.remove(os.path.join(target_train_dir, class_zip))
        
    # unzip val dataset
    shutil.unpack_archive(val_dir, target_val_dir)
    with open(txt_dir, 'r') as txt_file:
        lines = txt_file.readlines()
        for line in lines:
            val_img, class_ = line.split()
            if not os.path.exists(os.path.join(target_val_dir, class2num[class_])):
                os.mkdir(os.path.join(target_val_dir, class2num[class_]))
            
            shutil.move(os.path.join(target_val_dir, val_img),
                        os.path.join(target_val_dir, class2num[class_]))


if __name__ == '__main__':
    base_dir   = '/Users/jason/Desktop/data'
    target_dir = '/Users/jason/Desktop/data/ImageNet'
    unpack(base_dir, target_dir)