#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "get_stock_price"
default_task = "publish"


@init
def set_properties(project):
    project.build_depends_on("requests_mock")
    project.build_depends_on("BeautifulSoup4")
    project.build_depends_on("Flask")
    project.build_depends_on("requests")
