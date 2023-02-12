# ImageNet-1K

This repo explains how to download & process ImageNet-1K train/val dataset for using as a dataset


## 1. Data Download

- Download ImageNet-1K train/val dataset from academic torrents : [train link](https://academictorrents.com/details/a306397ccf9c2ead27155983c254227c0fd938e2), [val link](https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5)
- Check-out my velog post for download on linux server : [link](https://velog.io/@jasonlee1995/Linux-Server-Download-ImageNet-1K)
- Check-out more informations on original ImageNet website : [link](https://image-net.org/index.php)


## 2. Data Processing
### 2.1. About Data
#### 2.1.1. ImageNet-1K Train Dataset

- ImageNet-1K train dataset zip contains zips like below

```bash
└── ILSVRC2012_img_train.tar
    ├── n01440764.tar
    ├── n01443537.tar
    ├── n01484850.tar
    ├── ...
    └── n15075141.tar
```


### 2.1.2. ImageNet-1K Val Dataset

- ImageNet-1K val dataset zip contains images like below

```bash
└── ILSVRC2012_img_val.tar
    ├── ILSVRV2012_val_00000001.JPEG
    ├── ILSVRV2012_val_00000002.JPEG
    ├── ILSVRV2012_val_00000003.JPEG
    ├── ...
    └── ILSVRV2012_val_00050000.JPEG
```



### 2.2. Files Explain

- `ImageNet_class_index.json` : include class infos
  - **Caution** : same label with different class num exists
    - crane : 134, 517
    - maillot : 638, 639
- `ImageNet_val_label.txt` : include validation image label
- `check.py` : check if unpacked right or not
- `unpack.py` : make clean file trees of `ILSVRC2012_img_train.tar`, `ILSVRC2012_img_val.tar` for using as a dataset


### 2.3. Run
---

1. Assume all the required files are in same directory like below (base_dir)

```bash
└── base_dir
    ├── ILSVRC2012_img_train.tar
    ├── ILSVRC2012_img_val.tar
    ├── ImageNet_class_index.json
    └── ImageNet_val_label.txt
```

---

2. From `unpack.py`, change `base_dir` and `target_dir` variables

---

3. Run `unpack.py` and it makes file trees in specific directory like below (target_dir)

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

---

4. From `check.py`, change `ImageNet_dir` variable and run for double-check 

<img width="350" alt="image" src="https://user-images.githubusercontent.com/49643709/163708613-da5fd5e3-2ab2-442a-8028-b9ef20ad7880.png">

---
