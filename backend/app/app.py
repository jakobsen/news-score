from litestar import Litestar, post
from litestar.plugins.structlog import StructlogPlugin
from litestar.config.cors import CORSConfig


from . import news
from .models import MeasurementsList, Result


@post("/calculate-score")
async def calculate_score(data: MeasurementsList) -> Result:
    score = news.calculate_score(data)
    return Result(score=score)


cors_config = CORSConfig(allow_origins=["*"])
app = Litestar(
    route_handlers=[calculate_score],
    plugins=[StructlogPlugin()],
    cors_config=cors_config,
)
