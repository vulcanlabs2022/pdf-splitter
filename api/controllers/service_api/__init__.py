# -*- coding:utf-8 -*-
from flask import Blueprint
from libs.external_api import ExternalApi

bp = Blueprint('api', __name__, url_prefix='/api')
api = ExternalApi(bp)

from . import check