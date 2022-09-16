# -*- coding: utf-8 -*-

"""
Definition the APP Settings in here.

Description:
The Settings will try to find the arguments from os.environ.
If the argument is missing in os.environ, ValidationError
will be raised.

History:
2022/09/12 Created by Gallon
"""

from typing import Any, Dict, Optional
from pydantic import BaseSettings, validator
import pathlib
import os
import json

# NFS_ROOT_PATH = "/mnt"

# Set key path to env to enable GCS operation.
# if 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ:
#     pass
# else:
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f'{NFS_ROOT_PATH}/google_key.json'

class Settings(BaseSettings):
    """
    Collect arguments from os.environ in this class.

    It try to find the arguments from os.environ.
    If the argument is missing, ValidationError will be raised.
    """
    # Arguments for APP routers
    API_V1_STR: str = "/api/v1"
    API_ROOT_PATH: str = None

    # logger conf file path
    LOGGER_CONF_PATH: Optional[str] = None
    LOGGER_CONF: Optional[Dict] = None
    LOGGER_LEVEL: str = "INFO"

    # Api-server version (From env)
    API_VERSION = os.environ.get('api-version', 'testing')

    @validator("LOGGER_CONF_PATH", pre=True)
    def gen_logger_conf_path(cls, file_path: Optional[str], values: Dict) -> str:
        """
        Generate the path of logger_conf.json, if it is not set.

        The default file path:
        artichoke_server/backend/app/core/conf/logger_conf.json

        Returned:
            A path string of the logger_conf.json
        """
        if isinstance(file_path, str):
            return file_path
        current_path = pathlib.Path(__file__).parent.absolute()
        file_path = os.path.join(current_path, "logger_conf.json")
        return file_path

    # DB_URL: str = os.environ.get("db_url", "bigquery://testrite-edt")

    class Config:
        """letter case checking."""

        case_sensitive = True

_settings = Settings()
with open(_settings.LOGGER_CONF_PATH, 'r') as f:
    logger_conf = json.load(f)
_settings.LOGGER_CONF = logger_conf
settings = _settings
