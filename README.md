# CPSC - 8810 Machine Learning Based Image Synthesis
  The aim of this work is to enable in-painting on occluded and incomplete 2.5 dimensional elevation maps. The idea is to then utilize these in-painted maps for a more informed vision-aware planning. The in-painting model is a mask-aware transformer (MAT) borrowed directly from ([here](https://arxiv.org/abs/2203.15270)).

#### Benjamin Johnson, Vasudev Purohit

#### [\[Website\]](https://arxiv.org/abs/2203.15270)
---

## **Project Changes**

- The original work loads random masks. We changed this part of the code to now load custom masks that are correlated to the elevations seen on the 2.5d maps. Changes had to be made to the training and validation scripts to load the correct masks too.

- We trained and validated with a smaller dataset owing to the project timelines, and hence had to change the metrics script during validation.

- For any further queries and questions, you can contact Benjamin Johnson (bij@g.clemson.edu) or Vasudev Purohit (vpurohi@g.clemson.edu). As detailed on the project ([website]), the evaluation metrics for the different models trained are shown as follows:

![metrics](/figures/metrics.png)

- To utilize the original work, refer ([MAT](https://github.com/fenglinglwb/MAT)). This code works specifically with the masks and images shown below.
---

## Visualization

![baseline](/figures/baseline.png)

![ours_1](/figures/ours_1.png)

![ours_2b](/figures/ours_2b.png)

![ours_3](/figures/ours_3.png)

## Train

For example, if you want to train a model on Places, run a bash script with
```shell
python train.py \
    --outdir=output_path \
    --gpus=8 \
    --batch=32 \
    --metrics=fid36k5_full \
    --data=training_data_path \
    --data_val=val_data_path \
    --dataloader=datasets.dataset_512.ImageFolderMaskDataset \
    --mirror=True \
    --cond=False \
    --cfg=places512 \
    --aug=noaug \
    --generator=networks.mat.Generator \
    --discriminator=networks.mat.Discriminator \
    --loss=losses.loss.TwoStageLoss \
    --pr=0.1 \
    --pl=False \
    --truncation=0.5 \
    --style_mix=0.5 \
    --ema=10 \
    --lr=0.001
```

Description of arguments:
- outdir: output path for saving logs and models
- gpus: number of used gpus
- batch: number of images in all gpus
- metrics: find more metrics in 'metrics/metric\_main.py'
- data: training data
- data\_val: validation data
- dataloader: you can define your own dataloader
- mirror: use flip augmentation or not 
- cond: use class info, default: false
- cfg: configuration, find more details in 'train.py'
- aug: use augmentation of style-gan-ada or not, default: false
- generator: you can define your own generator
- discriminator: you can define your own discriminator
- loss: you can define your own loss
- pr: ratio of perceptual loss
- pl: use path length regularization or not, default: false
- truncation: truncation ratio proposed in stylegan
- style\_mix: style mixing ratio proposed in stylegan
- ema: exponoential moving averate, ~K samples
- lr: learning rate

## License and Acknowledgement
The code and models in this repo are for research purposes only. Our code is bulit upon [MAT](https://github.com/fenglinglwb/MAT).
