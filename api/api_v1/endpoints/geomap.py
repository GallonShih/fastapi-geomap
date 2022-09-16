# -*- coding: utf-8 -*-

"""
Definition of the feature router for the gooseberry api service.

Description:
The schemas and routers of feature are defined in here.

History:
2022/09/12 Created by Gallon
"""

from fastapi import APIRouter, Body, Depends, status, Request
from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from crud import crud_features_library
from core.core_config import settings
# from core.db_session import get_db_session
from logging import config as logger_config
from logging import getLogger
# from sqlalchemy.orm import Session

logger_config.dictConfig(settings.LOGGER_CONF)
logger = getLogger(__name__)

router: APIRouter = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def get_map(request: Request):
    return templates.TemplateResponse("map.html", {"request": request})
