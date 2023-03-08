# figure generator

generate figures with command
```bash
python generate.py [(str) directory in `generated` directory] [(int) number of figure sets]
```
example

```bash
python generate.py test 1000
```
this will generate 1000 * number of figures (circle, triangle...) in directory `test`

# YOLOv5 training
copy YOLOv5 repo

copy `figures.yaml` to `data` directory in yolov5 repo directory

run training 
```bash
python train.py --data figures.yaml --weights yolov5l.pt --epochs 10 --batch-size 8
```

# integrate yolo + tesseract for text reading 