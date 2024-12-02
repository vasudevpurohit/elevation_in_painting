# CPSC - 8810 Machine Learning Based Image Synthesis
  The aim of this work is to enable in-painting on occluded and incomplete 2.5 dimensional elevation maps. The idea is to then utilize these in-painted maps for a more informed vision-aware planning. The in-painting model is a mask-aware transformer (MAT) borrowed directly from ([here](https://arxiv.org/abs/2203.15270)).

#### Benjamin Johnson, Vasudev Purohit

#### [\[Website\]](https://arxiv.org/abs/2203.15270)
---

## **Project Changes**

- The original work on MAT loaded random masks. We changed this part of the code to now load custom masks that are correlated to the elevations seen on the 2.5d maps. Changes had to be made to the training and validation scripts to load the correct masks too.

- We trained and validated with a smaller dataset owing to the project timelines, and hence had to change the metrics script during validation.

- For any further queries and questions, you can contact Benjamin Johnson (bij@g.clemson.edu) or Vasudev Purohit (vpurohi@g.clemson.edu). As detailed on the project ([website]), the evaluation metrics for the different models trained are shown as follows:

![metrics](/figures/metrics.png)

---

## Visualization

We present a transformer-based model (MAT) for large hole inpainting with high fidelity and diversity.

![large hole inpainting with pluralistic generation](/figures/baseline.png)

Compared to other methods, the proposed MAT restores more photo-realistic images with fewer artifacts.

![comparison with sotas](/figures/sota.png)

## Usage

It is highly recommanded to adopt Conda/MiniConda to manage the environment to avoid some compilation errors.

1. Clone the repository.
    ```shell
    git clone https://github.com/fenglinglwb/MAT.git 
    ```
2. Install the dependencies.
    - Python 3.7
    - PyTorch 1.7.1
    - Cuda 11.0
    - Other packages
    ```shell
    pip install -r requirements.txt
    ```

## Quick Test

1. We provide models trained on CelebA-HQ, FFHQ and Places365-Standard at 512x512 resolution. Download models from [One Drive](https://mycuhk-my.sharepoint.com/:f:/g/personal/1155137927_link_cuhk_edu_hk/EuY30ziF-G5BvwziuHNFzDkBVC6KBPRg69kCeHIu-BXORA?e=7OwJyE) and put them into the 'pretrained' directory. The released models are retrained, and hence the visualization results may slightly differ from the paper.

2. Obtain inpainted results by running
    ```shell
    python generate_image.py --network model_path --dpath data_path --outdir out_path [--mpath mask_path]
    ```
    where the mask path is optional. If not assigned, random 512x512 masks will be generated. Note that 0 and 1 values in a mask refer to masked and remained pixels.

    For example, run
    ```shell
    python generate_image.py --network pretrained/CelebA-HQ.pkl --dpath test_sets/CelebA-HQ/images --mpath test_sets/CelebA-HQ/masks --outdir samples
    ```

    Note. 
    - Our implementation only supports generating an image whose size is a multiple of 512. You need to pad or resize the image to make its size a multiple of 512. Please pad the mask with 0 values.
    - If you want to use the CelebA-HQ-256 model, please specify the parameter 'resolution' as 256 in generate\_image.py.

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

## Evaluation

We provide evaluation scrtips for FID/U-IDS/P-IDS/LPIPS/PSNR/SSIM/L1 metrics in the 'evaluation' directory. Only need to give paths of your results and GTs.

We also provide our masks for CelebA-HQ-val and Places-val [here](https://mycuhk-my.sharepoint.com/:f:/g/personal/1155137927_link_cuhk_edu_hk/EuY30ziF-G5BvwziuHNFzDkBVC6KBPRg69kCeHIu-BXORA?e=7OwJyE).


## Citation

    @inproceedings{li2022mat,
        title={MAT: Mask-Aware Transformer for Large Hole Image Inpainting},
        author={Li, Wenbo and Lin, Zhe and Zhou, Kun and Qi, Lu and Wang, Yi and Jia, Jiaya},
        booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
        year={2022}
    }

## License and Acknowledgement
The code and models in this repo are for research purposes only. Our code is bulit upon [StyleGAN2-ADA](https://github.com/NVlabs/stylegan2-ada-pytorch).
