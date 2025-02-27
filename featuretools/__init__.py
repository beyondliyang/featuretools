# flake8: noqa
import warnings
from .config_init import config
from . import variable_types
from .entityset.api import *
from . import primitives
from .synthesis.api import *
from .primitives import list_primitives
from .computational_backends.api import *
from . import tests
from .utils.time_utils import *
from .utils.cli_utils import show_info
from .version import __version__
import featuretools.demo
import featuretools.wrappers
from . import feature_base
from .feature_base import AggregationFeature, DirectFeature, Feature, FeatureBase, IdentityFeature, TransformFeature, GroupByTransformFeature, save_features, load_features

import pkg_resources
import sys
# Call functions registered by other libraries when featuretools is imported
for entry_point in pkg_resources.iter_entry_points('featuretools_initialize'):
    try:
        method = entry_point.load()
        if callable(method):
            method()
    except Exception:
        pass

# Load in submodules registered by other libraries into Featuretools namespace
for entry_point in pkg_resources.iter_entry_points('featuretools_plugin'):
    try:
        sys.modules["featuretools." + entry_point.name] = entry_point.load()
    except Exception:
        pass
