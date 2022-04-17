import os


def check(ImageNet_dir):
    train_dir = os.path.join(ImageNet_dir, 'train')
    val_dir   = os.path.join(ImageNet_dir, 'val')
    
    train_cnt, val_cnt = 0, 0

    for c in os.listdir(train_dir):
        c_dir = os.path.join(train_dir, c)
        train_cnt += len(os.listdir(c_dir))

    for c in os.listdir(val_dir):
        c_dir = os.path.join(val_dir, c)
        val_cnt += len(os.listdir(c_dir))

    ImageNet_train, ImageNet_val = 1281167, 50000

    print('Train Images from ImageNet : {}'.format(ImageNet_train))
    print('Train Images Detected : {}'.format(train_cnt))
    print('Same : {}'.format(ImageNet_train == train_cnt))
    print()

    print('Val Images from ImageNet : {}'.format(ImageNet_val))
    print('Val Images Detected : {}'.format(val_cnt))
    print('Same : {}'.format(ImageNet_val == val_cnt))


if __name__ == '__main__':
    ImageNet_dir = '/Users/jason/Desktop/data/ImageNet/'
    check(ImageNet_dir)