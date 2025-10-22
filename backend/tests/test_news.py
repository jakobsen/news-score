from app.models import (
    MeasurementsList,
    TemperatureMeasurement,
    HeartRateMeasurement,
    RespiratoryRateMeasurement,
)
from app.news import calculate_score


def test_valid_score() -> None:
    measurement_list = MeasurementsList(
        measurements=[
            TemperatureMeasurement(value=39),
            HeartRateMeasurement(value=43),
            RespiratoryRateMeasurement(value=19),
        ]
    )
    result = calculate_score(measurement_list)
    assert result == 2
