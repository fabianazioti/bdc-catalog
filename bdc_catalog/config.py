#
# This file is part of BDC-Catalog.
# Copyright (C) 2020 INPE.
#
# BDC-Catalog is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Config for BDC-Catalog."""
import os

CURRENT_DIR = os.path.dirname(__file__)


class Config:
    BDC_ACTIVE_SCHEMA = os.environ.get('BDC_ACTIVE_SCHEMA', 'bdc')
