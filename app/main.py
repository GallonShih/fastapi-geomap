# -*- coding: utf-8 -*-

"""
Definition of gooseberry api service.

Description:
The main file of gooseberry api service,
included routers should be defined in here.
It is developed by FastAPI framework.

History:
2022/09/12 Created by Gallon
"""
from typing import Optional
from fastapi import FastAPI
from api.api_v1.api import api_router
from core.core_config import settings

description = """
Shark 專案使用的 API Server
"""


app = FastAPI(
    root_path=settings.API_ROOT_PATH,
    description=description,
    title="Shark API Server",
    contact={
        "name": "Shark Maintainer",
        "email": "gallonshih0526@gmail.com"
    },
    version=settings.API_VERSION
)

app.include_router(
    api_router,
    prefix=settings.API_V1_STR,
)