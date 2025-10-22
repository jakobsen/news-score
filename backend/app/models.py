from enum import StrEnum
from typing import Annotated, Literal, Self

from pydantic import BaseModel, Field, NonNegativeInt, conint, model_validator


class MeasurementType(StrEnum):
    TEMPERATURE = "TEMP"
    HEART_RATE = "HR"
    RESPIRATORY_RATE = "RR"


class TemperatureMeasurement(BaseModel):
    type: Literal[MeasurementType.TEMPERATURE] = MeasurementType.TEMPERATURE
    value: conint(gt=31, le=42)


class HeartRateMeasurement(BaseModel):
    type: Literal[MeasurementType.HEART_RATE] = MeasurementType.HEART_RATE
    value: conint(gt=25, le=220)


class RespiratoryRateMeasurement(BaseModel):
    type: Literal[MeasurementType.RESPIRATORY_RATE] = MeasurementType.RESPIRATORY_RATE
    value: conint(gt=3, le=60)


Measurement = Annotated[
    TemperatureMeasurement | HeartRateMeasurement | RespiratoryRateMeasurement,
    Field(discriminator="type"),
]


class MeasurementsList(BaseModel):
    """
    A list of measurements containing exactly one of each measurement type.

    If a measurement type is missing, an unknown measurement type is present,
    or the measurements list contains duplicate measurement types, validation
    will fail.
    """

    measurements: list[Measurement]

    @model_validator(mode="after")
    def validate_list(self) -> Self:
        seen = set()
        for measurement in self.measurements:
            if measurement.type in seen:
                raise ValueError(f"Duplicate measurement types {measurement.type}")
            seen.add(measurement.type)

        all_measurement_types = {t.value for t in MeasurementType}
        if seen != all_measurement_types:
            missing_types = all_measurement_types - seen
            raise ValueError(f"Missing measurement types {', '.join(missing_types)}")

        return self


class Result(BaseModel):
    score: NonNegativeInt
