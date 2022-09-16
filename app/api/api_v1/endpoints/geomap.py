# -*- coding: utf-8 -*-

"""
Definition of the feature router for the gooseberry api service.

Description:
The schemas and routers of feature are defined in here.

History:
2022/09/12 Created by Gallon
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from core.core_config import settings
from logging import config as logger_config
from logging import getLogger

logger_config.dictConfig(settings.LOGGER_CONF)
logger = getLogger(__name__)

router: APIRouter = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def get_map(request: Request):
    return templates.TemplateResponse("map.html", {"request": request})
    # return 'success'
