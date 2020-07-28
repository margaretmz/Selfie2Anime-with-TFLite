# Selfie2Anime Android app

This is a sample app for TensorFlow Lite on Android with the Selfie2Anime model.   
Please read the detailed instructions on how to create the application from scratch in this blog post on Medium: [Part 3](https://medium.com/@margaretmz/selfie2anime-with-tflite-part-3-android-app-e47f8a2c92b2) Android app.

## TensorFlow Lite Model
The TensorFlow Lite Model used in the Android app is located in this project repo [here](https://github.com/margaretmz/selfie2anime-with-tflite/blob/master/ml/add-meta-data-CLI/model_with_metadata/selfie2anime.tflite).
```
|--ml  
|  |--add-meta-data-CLI  
|  |  |--model_with_metadata  
|  |  |  |-- selfie2anime.tflite  
```          
Alternatively you could use the colab to add metadata to the .tflite file.

## Requirements
* Android Studio Preview Beta version (download ([here] (https://developer.android.com/studio/preview))
* Android device in developer ode with USB debugging enabled
* USB cable to connect an Android device to computer

## Build and run
* Clone the repo
Clone this project repo:  
`git clone https://github.com/margaretmz/selfie2anime-with-tflite.git`  
* Open the Android code android/selfie2anime in Android Studio.
* Connect your Android device to computer then click on `"Run -> Run 'app'`.
* Once the app is launched on device, grant camera permission.
* Take a selfie and wait for the TensorFlow Lite model to process the selfie. 
* You will then see a screen with both the selfie and anime image.

## Download apk
If you are not familar with building the app in Android and would like to just try out the app, please download the apk file from [here](https://github.com/margaretmz/selfie2anime-with-tflite/tree/master/android/selfie2anime/app/release). Note: you will need to grant permission to install unknown apps from your Android security settings. 
