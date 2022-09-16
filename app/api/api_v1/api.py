# -*- coding: utf-8 -*-

"""
Definition of routers on gooseberry api service.

Description:
Included routers should be defined in here.

History:
2022/09/12 Created by Gallon
"""

from fastapi import APIRouter
from api.api_v1.endpoints import geomap

api_router = APIRouter()
api_router.include_router(geomap.router, prefix="/geomap", tags=["geomap"])
