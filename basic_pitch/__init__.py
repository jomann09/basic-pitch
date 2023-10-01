#!/usr/bin/env python
# encoding: utf-8
#
# Copyright 2022 Spotify AB
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

import enum
import logging
import pathlib

__author__ = "Spotify"
__version__ = "0.3.0"
__email__ = "basic-pitch@spotify.com"
__demowebsite__ = "https://basicpitch.io"
__description__ = "Basic Pitch, a lightweight yet powerful audio-to-MIDI converter with pitch bend detection."
__url__ = "https://github.com/spotify/basic-pitch"


try:
    import tensorflow

    TF_PRESENT = True
except ImportError:
    TF_PRESENT = False
    logging.warning(
        "Tensorflow is not installed. "
        "If you plan to use a TF Saved Model, "
        "reinstall basic-pitch with `pip install 'basic-pitch[tf]'`"
    )

try:
    import coremltools

    CT_PRESENT = True
except ImportError:
    CT_PRESENT = False
    logging.warning(
        "Coremltools is not installed. "
        "If you plan to use a CoreML Saved Model, "
        "reinstall basic-pitch with `pip install 'basic-pitch[coreml]'`"
    )

try:
    import tflite_runtime.interpreter

    TFLITE_PRESENT = True
except ImportError:
    TFLITE_PRESENT = False
    logging.warning(
        "tflite-runtime is not installed. "
        "If you plan to use a TFLite Model, "
        "reinstall basic-pitch with `pip install 'basic-pitch tflite-runtime'` or "
        "`pip install 'basic-pitch[tf]'"
    )

try:
    import onnxruntime

    ONNX_PRESENT = True
except ImportError:
    ONNX_PRESENT = False
    logging.warning(
        "onnxruntime is not installed. "
        "If you plan to use an ONNX Model, "
        "reinstall basic-pitch with `pip install 'basic-pitch[onnx]'`"
    )


class FilenameSuffix(enum.Enum):
    tf = "nmp"
    coreml = "nmp.mlpackage"
    tflite = "nmp.tflite"
    onnx = "nmp.onnx"


if TF_PRESENT:
    _default_model_type = FilenameSuffix.tf
elif CT_PRESENT:
    _default_model_type = FilenameSuffix.coreml
elif TFLITE_PRESENT:
    _default_model_type = FilenameSuffix.tflite
elif ONNX_PRESENT:
    _default_model_type = FilenameSuffix.onnx


def build_icassp_2022_model_path(suffix: FilenameSuffix) -> pathlib.Path:
    return pathlib.Path(__file__).parent / "saved_models/icassp_2022" / suffix.value


ICASSP_2022_MODEL_PATH = build_icassp_2022_model_path(_default_model_type)
