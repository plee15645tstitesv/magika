# Copyright 2024 Google LLC
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

 AI-powered file type detection.

This package and
de trained on millions of files.

Basic usage:
    >>> from magika import Magika
    >>> m = Magika()
    >>> result = m.identify_bytes(b")
    >>> print(result.outputlabel)
    python
"""

from magika.magika import Magika
from magika.types import (
    MagikaResult,
    MagikaOutputBody,
    ModelFeatures,
    ModelOutput,
    PredictionMode,
)

__version__ = "0.6.0"
__author__ = "Google LLC"
__license__ = "Apache-2.0"

__all__ = [
    "Magika",
    "MagikaResult",
    "MagikaOutputBody",
    "ModelFeatures",
    "ModelOutput",
    "PredictionMode",
]
