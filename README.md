# Editing...
# ImageNet-1K

This repo explains how to download/process ImageNet-1K train/val dataset


## 1. Data Download

- Download ImageNet-1K train/val dataset from academic torrents
- ImageNet-1K train dataset [[link](https://academictorrents.com/details/a306397ccf9c2ead27155983c254227c0fd938e2)]
- ImageNet-1K val dataset [[link](https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5)]
- Check-out more informations on original ImageNet website [[link](https://image-net.org/index.php)]


## 2. Data Processing
### 2.1. Run
```bash
└── base_dir
    ├── ILSVRC2012_img_train.tar
    ├── ILSVRC2012_img_val.tar
    ├── ImageNet_class_index.json
    └── ImageNet_val_label.txt
```
- Assume all the required files are in same directory (base_dir)

```bash
└── target_dir
    ├── train
    │   ├── 0
    │   │   ├── n01440764_18.JPEG
    │   │   ├── n01440764_36.JPEG
    │   │   └── ...
    │   ├── 1
    │   ├── ...
    │   └── 999
    └── val
        ├── 0
        │   ├── ILSVRC2012_val_00000293.JPEG
        │   ├── ILSVRC2012_val_00002138.JPEG
        │   └── ...
        ├── 1
        ├── ...
        └── 999
```
- Data preprocessing code `unpack.py` will make file trees as above


### 2.2. Details
#### 2.2.1. ImageNet-1K Train Dataset

```bash
└── ILSVRC2012_img_train.tar
    ├── n01440764.tar
    ├── n01443537.tar
    ├── n01484850.tar
    ├── ...
    └── n15075141.tar
```
- ImageNet-1K train dataset zip contains zips like above
- Part of the `unpack.py` code unzip all the zips and convert to 0~999 referencing `ImageNet_class_index.json`

### 2.2.2. ImageNet-1K Val Dataset

