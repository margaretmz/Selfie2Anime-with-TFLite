package com.mzm.sample.selfie2anime

import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.FrameLayout
import com.tflite.selfie2anime.R
import java.io.File

/**
 * Author: Margaret Maynard-Reid
 *
 * This is an Android sample app that showcases the following:
 *
 * 1. Jetpack navigation component - navigate between Fragments
 * 2. CameraX - permission check, camera setup, and image capture use case
 * 3. ML Model binding - easy import of .tflite model in Android Studio
 * 4. Transform a selfie image to an anime image with selfie2anime.tflite model
 *
 * This MainActivity.kt is the main entry point into the sample app.
 * There is one single Activity with 3 Fragments:
 *
 * 1. PermissionsFragment.kt - check camera permission
 * 2. CameraFragment.kt - capture photo
 * 3. Selfie2animeFragment.kt - display the selfie & anime images
 */
class MainActivity : AppCompatActivity() {

    private lateinit var container: FrameLayout

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    companion object {

        /** Use external media if it is available, our app's file directory otherwise */
        fun getOutputDirectory(context: Context): File {
            val appContext = context.applicationContext
            val mediaDir = context.externalMediaDirs.firstOrNull()?.let {
                File(it, appContext.resources.getString(R.string.app_name)).apply { mkdirs() } }
            return if (mediaDir != null && mediaDir.exists())
                mediaDir else appContext.filesDir
        }
    }
}