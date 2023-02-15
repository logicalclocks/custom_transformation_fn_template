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

import os

def min_max_scaler(value, min_value, max_value):
    if value is None:
        return None
    elif max_value - min_value == 0:
        return 0
    else:
        return (value - min_value) / (max_value - min_value)

def standard_scaler(value, mean, std_dev):
    if value is None:
        return None
    elif std_dev == 0:
        return 0
    else:
        return (value - mean) / std_dev


def robust_scaler(value, p25, p50, p75):
    if value is None:
        return None
    elif p75 - p25 == 0:
        return 0
    else:
        return (value - p50) / (p75 - p25)
