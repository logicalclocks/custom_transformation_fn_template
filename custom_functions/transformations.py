#
#   Copyright 2022 Logical Clocks AB
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import numpy as np


def min_max_scaler(value, min_value, max_value):
    if value is None:
        return None
    elif np.float64(max_value - min_value) == np.float64(0):
        return np.float64(0)
    else:
        return np.float64((value - min_value) / (max_value - min_value))


def standard_scaler(value, mean, std_dev):
    if value is None:
        return None
    elif np.float64(std_dev) == np.float64(0):
        return np.float64(0)
    else:
        return np.float64((value - mean) / std_dev)


def robust_scaler(value, p25, p50, p75):
    if value is None:
        return None
    elif np.float64(p75 - p25) == np.float64(0):
        return np.float64(0)
    else:
        return np.float64((value - p50) / (p75 - p25))
