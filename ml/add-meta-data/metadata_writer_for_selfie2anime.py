# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Writes metadata for the selfie2anime model.

The selfie2anime model takes an selfie image as input and then output an anime image.

This metadata writer writes metadata to the selfie2anime model.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl import app
from absl import flags

import tensorflow as tf

from tflite_support import flatbuffers
from tflite_support import metadata as _metadata
from tflite_support import metadata_schema_py_generated as _metadata_fb

# Updated by Margaret
FLAGS = flags.FLAGS
flags.DEFINE_string("model_file", None,
                    "Path and file name to the TFLite model file.")
flags.DEFINE_string("export_directory", None,
                    "Path to save the TFLite model files with metadata.")


class MetadataPopulatorForGANModel(object):
  """Populates the metadata for the selfie2anime model."""

  def __init__(self, model_file):
    self.model_file = model_file
    self.metadata_buf = None

  def populate(self):
    """Creates metadata and thesn populates it for a style transfer model."""
    self._create_metadata()
    self._populate_metadata()

  def _create_metadata(self):
    """Creates the metadata for the selfie2anime model."""

    # Creates model info.
    model_meta = _metadata_fb.ModelMetadataT()
    model_meta.name = "Selfie2Anime" 
    model_meta.description = ("Convert selfie to anime.")
    model_meta.version = "v1"
    model_meta.author = "TensorFlow"
    model_meta.license = ("Apache License. Version 2.0 "
                          "http://www.apache.org/licenses/LICENSE-2.0.")

    # Creates info for the input, selfie image.
    input_image_meta = _metadata_fb.TensorMetadataT()
    input_image_meta.name = "selfie_image"
    input_image_meta.description = (
        "The expected image is 256 x 256, with three channels "
        "(red, blue, and green) per pixel. Each value in the tensor is between"
        " 0 and 1.")
    input_image_meta.content = _metadata_fb.ContentT()
    input_image_meta.content.contentProperties = (
        _metadata_fb.ImagePropertiesT())
    input_image_meta.content.contentProperties.colorSpace = (
        _metadata_fb.ColorSpaceType.RGB)
    input_image_meta.content.contentPropertiesType = (
        _metadata_fb.ContentProperties.ImageProperties)
    input_image_normalization = _metadata_fb.ProcessUnitT()
    input_image_normalization.optionsType = (
        _metadata_fb.ProcessUnitOptions.NormalizationOptions)
    input_image_normalization.options = _metadata_fb.NormalizationOptionsT()
    input_image_normalization.options.mean = [0.0]
    input_image_normalization.options.std = [255]
    input_image_meta.processUnits = [input_image_normalization]
    input_image_stats = _metadata_fb.StatsT()
    input_image_stats.max = [1.0]
    input_image_stats.min = [0.0]
    input_image_meta.stats = input_image_stats


    # Creates output info, anime image
    output_image_meta = _metadata_fb.TensorMetadataT()
    output_image_meta.name = "anime_image"
    output_image_meta.description = "Image styled."
    output_image_meta.content = _metadata_fb.ContentT()
    output_image_meta.content.contentProperties = _metadata_fb.ImagePropertiesT()
    output_image_meta.content.contentProperties.colorSpace = (
        _metadata_fb.ColorSpaceType.RGB)
    output_image_meta.content.contentPropertiesType = (
        _metadata_fb.ContentProperties.ImageProperties)
    output_image_normalization = _metadata_fb.ProcessUnitT()
    output_image_normalization.optionsType = (
        _metadata_fb.ProcessUnitOptions.NormalizationOptions)
    output_image_normalization.options = _metadata_fb.NormalizationOptionsT()
    output_image_normalization.options.mean = [0.0]
    output_image_normalization.options.std = [0.003921568627]  # 1/255
    output_image_meta.processUnits = [output_image_normalization]
    output_image_stats = _metadata_fb.StatsT()
    output_image_stats.max = [1.0]
    output_image_stats.min = [0.0]
    output_image_meta.stats = output_image_stats

    # Creates subgraph info.
    subgraph = _metadata_fb.SubGraphMetadataT()
    subgraph.inputTensorMetadata = [input_image_meta] # Updated by Margaret
    subgraph.outputTensorMetadata = [output_image_meta] # Updated by Margaret
    model_meta.subgraphMetadata = [subgraph]

    b = flatbuffers.Builder(0)
    b.Finish(
        model_meta.Pack(b),
        _metadata.MetadataPopulator.METADATA_FILE_IDENTIFIER)
    self.metadata_buf = b.Output()

  def _populate_metadata(self):
    """Populates metadata to the model file."""
    populator = _metadata.MetadataPopulator.with_model_file(self.model_file)
    populator.load_metadata_buffer(self.metadata_buf)
    populator.populate()


def populate_metadata(model_file):
  """Populates the metadata using the populator specified.

  Args:
      model_file: valid path to the model file.
      model_type: a type defined in StyleTransferModelType .
  """

  # Populates metadata for the model.
  model_file_basename = os.path.basename(model_file)
  export_path = os.path.join(FLAGS.export_directory) #Margaret
  tf.io.gfile.copy(model_file, export_path, overwrite=True)

  populator = MetadataPopulatorForGANModel(export_path) # Updated by Margaret
  populator.populate()

  # Displays the metadata that was just populated into the tflite model.
  displayer = _metadata.MetadataDisplayer.with_model_file(export_path)
  export_json_file = os.path.join(
      FLAGS.export_directory,
      os.path.splitext(model_file_basename)[0] + ".json")
  json_file = displayer.get_metadata_json()
  with open(export_json_file, "w") as f:
    f.write(json_file)
  print("Finished populating metadata and associated file to the model:")
  print(export_path)
  print("The metadata json file has been saved to:")
  print(
      os.path.join(FLAGS.export_directory,
                   os.path.splitext(model_file_basename)[0] + ".json"))


def main(_):
  """Writes metadata to the selfie2anime model."""

  populate_metadata(FLAGS.model_file)


if __name__ == "__main__":
  app.run(main)