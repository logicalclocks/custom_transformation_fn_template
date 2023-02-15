def min_max_scaler(value, min_value,max_value):
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