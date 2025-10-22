from .models import (
    HeartRateMeasurement,
    MeasurementsList,
    RespiratoryRateMeasurement,
    TemperatureMeasurement,
)


def calculate_score(measurement_list: MeasurementsList) -> int:
    score = 0
    for measurement in measurement_list.measurements:
        match measurement:
            case TemperatureMeasurement(value=value):
                score += _temperature_score(value)
            case HeartRateMeasurement(value=value):
                score += _heart_rate_score(value)
            case RespiratoryRateMeasurement(value=value):
                score += _respiratory_rate_score(value)
    return score


def _temperature_score(value: int) -> int:
    if 31 < value <= 35:
        return 3
    if 35 < value <= 36:
        return 1
    if 36 < value <= 38:
        return 0
    if 38 < value <= 39:
        return 1
    if 39 < value <= 42:
        return 2
    raise ValueError("Temperature measurement outside valid range")


def _heart_rate_score(value: int) -> int:
    if 25 < value <= 40:
        return 3
    if 40 < value <= 50:
        return 1
    if 50 < value <= 90:
        return 0
    if 90 < value <= 110:
        return 1
    if 110 < value <= 130:
        return 2
    if 130 < value <= 220:
        return 3
    raise ValueError("Heart rate measurement outside valid range")


def _respiratory_rate_score(value: int) -> int:
    if 3 < value <= 8:
        return 3
    if 8 < value <= 11:
        return 1
    if 11 < value <= 20:
        return 0
    if 20 < value <= 24:
        return 2
    if 24 < value <= 60:
        return 3
    raise ValueError("Respiratory rate measurement outside valid range")
