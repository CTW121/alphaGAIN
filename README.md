## α-GAIN: Missing data imputation using GAIN with modification on hint generator

We developed 𝛼-Generative Adversarial Imputation Networks (𝛼-GAIN) to impute the missing values in real-life dataset. 𝛼-GAIN is an improved version of the Generative Adversarial Imputation Net ([GAIN](https://arxiv.org/abs/1806.02920))

The generator (G) imputes the missing components according to observed components. The discriminator (D) then take the imputed dataset and determine which components were observed and which were imputed. The hint generator (H) generates the hint matrix as additional information to G.

To ensure that D to learn effectively when its loss is low, in turn forces G to learn, we have improved the hint mechanism in [GAIN](https://arxiv.org/abs/1806.02920) in two ways:
- we modify the fake indication in the H while generating the hint matrix,
- we provide a modified sigmoid function in the H for computing the updated hint rate based on the loss of discriminator.

We tested our model on various datasets and found that 𝛼-GAIN has slightly improvement compared with [GAIN](https://arxiv.org/abs/1806.02920) between missing rate 0.5 and 0.8.

Following is the architecture of [GAIN](https://arxiv.org/abs/1806.02920).
![GAIN architecture](https://github.com/CTW121/alphaGAIN/blob/master/images/GAIN.jpg)