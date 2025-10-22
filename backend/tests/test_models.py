import pytest
from pydantic import ValidationError

from app.models import (
    HeartRateMeasurement,
    MeasurementsList,
    RespiratoryRateMeasurement,
    TemperatureMeasurement,
)


def test_that_we_cannot_create_empty_measurement_list() -> None:
    with pytest.raises(ValidationError):
        MeasurementsList(measurements=[])


def test_that_passing_incomplete_list_raises() -> None:
    with pytest.raises(ValidationError):
        MeasurementsList(measurements=[HeartRateMeasurement(value=60)])


def test_that_passing_duplicates_raises() -> None:
    with pytest.raises(ValidationError):
        MeasurementsList(
            measurements=[
                HeartRateMeasurement(value=60),
                TemperatureMeasurement(value=37),
                RespiratoryRateMeasurement(value=8),
                RespiratoryRateMeasurement(value=9),
            ]
        )


def test_that_passing_valid_input_does_not_raise() -> None:
    assert MeasurementsList(
        measurements=[
            HeartRateMeasurement(value=60),
            TemperatureMeasurement(value=37),
            RespiratoryRateMeasurement(value=8),
        ]
    )
