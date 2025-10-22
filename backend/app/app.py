from enum import StrEnum
from typing import Annotated, Literal

from litestar import Litestar, Request, post
from litestar.plugins.structlog import StructlogPlugin
from pydantic import BaseModel, Field, NonNegativeInt, conint


class MeasurementType(StrEnum):
    TEMPERATURE = "TEMP"
    HEART_RATE = "HR"
    RESPIRATORY_RATE = "RR"


class TemperatureMeasurement(BaseModel):
    type: Literal[MeasurementType.TEMPERATURE]
    value: conint(gt=31, le=42)


class HeartRateMeasurement(BaseModel):
    type: Literal[MeasurementType.HEART_RATE]
    value: conint(gt=24, le=220)


class RespiratoryRateMeasurement(BaseModel):
    type: Literal[MeasurementType.RESPIRATORY_RATE]
    value: conint(gt=3, le=60)


Measurement = Annotated[
    TemperatureMeasurement | HeartRateMeasurement | RespiratoryRateMeasurement,
    Field(discriminator="type"),
]


class MeasurementsList(BaseModel):
    measurements: list[Measurement]


class Result(BaseModel):
    score: NonNegativeInt


@post("/calculate-score")
async def calculate_score(request: Request, data: MeasurementsList) -> Result:
    request.logger.info(f"Received data {data}", data=data)
    return Result(score=2)


app = Litestar(route_handlers=[calculate_score], plugins=[StructlogPlugin()])
