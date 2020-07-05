package com.mzm.sample.selfie2anime.fragments

import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.navArgs
import com.bumptech.glide.Glide
import com.mzm.sample.selfie2anime.R
import kotlinx.android.synthetic.main.fragment_selfie2anime.*
import kotlinx.coroutines.*
import org.tensorflow.lite.support.image.TensorImage
import java.io.File
import com.mzm.sample.selfie2anime.ml.Selfie2anime

/**
 * A simple [Fragment] subclass.
 * Use the [Selfie2animeFragment.newInstance] factory method to
 * create an instance of this fragment.
 *
 * This is where we show both the captured selfie image and the anime image created by the tflite model
 */
class Selfie2animeFragment : Fragment() {

    private val args: Selfie2animeFragmentArgs by navArgs()
    private lateinit var filePath: String

    //    private var animeBitmap: Bitmap? = null
    private val parentJob = Job()
    private val coroutineScope = CoroutineScope(
        Dispatchers.Main + parentJob
    )

    private fun getAnimeAsync(bitmap: Bitmap): Deferred<Bitmap> =
        // use async() to create a coroutine in an IO optimized Dispatcher for model inference
        coroutineScope.async(Dispatchers.IO) {
            val model =
                Selfie2anime.newInstance(
                    requireContext()
                )

            // Creates inputs for reference.
            val selfieImage = TensorImage.fromBitmap(bitmap)

            // Runs model inference and gets result.
            val outputs = model.process(selfieImage)
            val animeImage = outputs.animeImageAsTensorImage
            val animeImageBitmap = animeImage.bitmap

            // Releases model resources if no longer used.
//        model.close()

            return@async animeImageBitmap
        }

    private fun loadAnimeImage(animeBitmap: Bitmap) {
        progressbar.visibility = View.GONE
        imageview_anime?.setImageBitmap(animeBitmap)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        retainInstance = true
        filePath = args.rootDir
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_selfie2anime, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val photoFile = File(filePath)

        Glide.with(view)
            .load(photoFile)
            .into(imageview_selfie)

        val selfieBitmap = BitmapFactory.decodeFile(filePath)
        coroutineScope.launch(Dispatchers.Main) {
            val animeBitmap = getAnimeAsync(selfieBitmap).await()
            loadAnimeImage(animeBitmap)
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        // clean up coroutine job
        parentJob.cancel()
    }

}