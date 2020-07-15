# Selfie2Anime on Android with TensorFlow Lite

<center><img src='https://miro.medium.com/max/700/1*2xELpk3O-zTcuzCn1NUB0A.png')</img></center>

This is the GitHub repo for an end-to-end tutorial from TFLite model conversion, to deployment in form of an Android App. 

Authors: ML GDEs - [Margaret Maynard-Reid](https://twitter.com/margaretmz) and [Sayak Paul](https://twitter.com/RisingSayak)

Reviewers: [Khanh LeViet](https://twitter.com/khanhlvg) and [Hoi Lam](https://twitter.com/hoitab)

Acknowledgements: We would like to thank Khanh LeViet and Lu Wang (TensorFlow Lite team), Hoi Lam (Android ML), and Soonson Kwon (ML GDEs — Google Developers Experts Program), for their collaboration and continuous support.

We used a Generative Adversarial Network (GAN) model proposed in this paper [Unsupervised Generative Attentional Networks with Adaptive Layer-Instance Normalization for Image-to-Image Translation](https://arxiv.org/abs/1907.10830) (also known as **U-GAT-IT**). The paper provides two generators: one that converts a selfies to anime-style image and the other one from anime to selfie. Here we only implemented the Selfie2Anime model since it better resembles the real-world scenario. The GitHub repository of the paper is available [here](https://github.com/taki0112/UGATIT). 

The repository is structured in the following way:

```
|--ml  
|  |--add-meta-data-Colab              // How to add metadata via Colab  
|  |--add-meta-data-CLI               // How to add metadata via command line  
|  |--Selfie2Anime_Model_Conversion  // How to convert and save to TFLite model  
|--android  
|  |--selfie2anime                  // TFLite model on Androi app  
```
 
Links to the three-part tutorial on Medium: [Part 1](https://medium.com/@margaretmz/selfie2anime-with-tflite-part-1-overview-f97500800ffe) | [Part 2](https://medium.com/@margaretmz/selfie2anime-with-tflite-part-2-tflite-model-84002cf521dc) | [Part 3](https://medium.com/@margaretmz/selfie2anime-with-tflite-part-3-android-app-e47f8a2c92b2).
