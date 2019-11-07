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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow_addons.utils.resource_loader import get_path_to_datafile

_activation_ops_so = tf.load_op_library(
    get_path_to_datafile("custom_ops/activations/_activation_ops.so"))


@tf.keras.utils.register_keras_serializable(package='Addons')
@tf.function
def lisht(x):
    """LiSHT: Non-Parameteric Linearly Scaled Hyperbolic Tangent Activation Function.

    Computes linearly scaled hyperbolic tangent (LiSHT): `x * tanh(x)`

    See [LiSHT: Non-Parameteric Linearly Scaled Hyperbolic Tangent Activation Function for Neural Networks](https://arxiv.org/abs/1901.05894).

    Args:
        x: A `Tensor`. Must be one of the following types:
            `float16`, `float32`, `float64`.
    Returns:
        A `Tensor`. Has the same type as `x`.
    """
    x = tf.convert_to_tensor(x)
    return _activation_ops_so.addons_lisht(x)


@tf.RegisterGradient("Addons>Lisht")
def _lisht_grad(op, grad):
    return _activation_ops_so.addons_lisht_grad(grad, op.inputs[0])