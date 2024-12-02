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

## In-painting Visualization

The details of the following models can be found on the project [website](https://www.google.com/), but here's a visual representation of the results obtained. The masks in the first two models are only representatives and do not reflect the true masks over which the inpainted results shown here were generated.

![baseline](/figures/baseline.png)

![ours_1](/figures/ours_1.png)

![ours_2b](/figures/ours_2b.png)

![ours_3](/figures/ours_3.png)

## Uncertainty Quantification

One of the major limitations of MAT was its inability to report the uncertainty of predictions. This is an important piece in robotics planning owing to the conservativeness/safety of the planned path. Hence, we have now included a script that runs the inference script in an ensemble. The Style Manipulation Module (SMM) in MAT allowed us to generate N different inferences for the same masked images. The disagreement between the outputs can thus be used to quantify the uncertainty.

## License and Acknowledgement
The code and models in this repo are for research purposes only. Our code is bulit upon [MAT](https://github.com/fenglinglwb/MAT).
