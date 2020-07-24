# Selfie2Anime with TensorFlow Lite

This is the GitHub repo for an end-to-end tutorial from TFLite model conversion, to model deployment on an Android App. Links to the three-part tutorial on Medium: [Part 1](https://medium.com/@margaretmz/selfie2anime-with-tflite-part-1-overview-f97500800ffe) | [Part 2](https://medium.com/@margaretmz/selfie2anime-with-tflite-part-2-tflite-model-84002cf521dc) | [Part 3](https://medium.com/@margaretmz/selfie2anime-with-tflite-part-3-android-app-e47f8a2c92b2). 

*Selfie2Anime with TensorFlow Lite* is one of the tutorial series of [awesome-tflite](https://github.com/margaretmz/awesome-tflite).

**Authors**: (ML GDEs: Google Developer Experts for Machine Learning)  [Margaret Maynard-Reid](https://twitter.com/margaretmz) and [Sayak Paul](https://twitter.com/RisingSayak)   
**Reviewers**: (Google TensorFlow team) [Khanh LeViet](https://twitter.com/khanhlvg) and [Hoi Lam](https://twitter.com/hoitab) 

<div align="center"><img src='https://miro.medium.com/max/700/1*CqpaYfiixTwnYsD0r_3oNw.png')</img></div>

This repository is structured in the following way:

```
|--ml  
|  |--add-meta-data-Colab             // How to add metadata via Colab  
|  |--add-meta-data-CLI               // How to add metadata via command line  
|  |--Selfie2Anime_Model_Conversion   // How to convert and save to TFLite model  
|--android  
|  |--selfie2anime                    // TFLite model on Androi app  
```

## The Selfie2Anime model
We used a Generative Adversarial Network (GAN) model proposed in this paper [Unsupervised Generative Attentional Networks with Adaptive Layer-Instance Normalization for Image-to-Image Translation](https://arxiv.org/abs/1907.10830) (also known as **U-GAT-IT**). The paper provides two generators: one that converts a selfie to anime-style image and the other one from anime to selfie. Here we only implemented the Selfie2Anime model since it better resembles the real-world scenario. The GitHub repository of the paper is available [here](https://github.com/taki0112/UGATIT). 

## Citation
The original authors of U-GAT-IT: Junho Kim, Minjae Kim, Hyeonwoo Kang, Kwanghee Lee.

```
@inproceedings{
Kim2020U-GAT-IT:,
title={U-GAT-IT: Unsupervised Generative Attentional Networks with Adaptive Layer-Instance Normalization for Image-to-Image Translation},
author={Junho Kim and Minjae Kim and Hyeonwoo Kang and Kwang Hee Lee},
booktitle={International Conference on Learning Representations},
year={2020},
url={https://openreview.net/forum?id=BJlZ5ySKPH}
} 
```
## Acknowledgement
We would like to thank Khanh LeViet and Lu Wang (TensorFlow Lite team), Hoi Lam (Android ML), and Soonson Kwon (ML GDEs Google Developer Expert Program), for their collaboration and continuous support.
