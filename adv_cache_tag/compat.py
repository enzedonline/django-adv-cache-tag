try:
    import cPickle as pickle
except ImportError:
    import pickle

try:
    from django.core.cache import caches
except ImportError:
    # Django < 1.7
    from django.core.cache import get_cache
else:
    def get_cache(name):
        return caches[name]

try:
    from django.template import BLOCK_TAG_START
except ImportError:
    # Django >= 1.8
    from django.template import base as template
else:
    from django import template


def get_template_libraries():
    try:
        from django.template.base import libraries
    except ImportError:
        # Django >= 1.9
        from django.template import engines
        engine = engines['django'].engine
        libraries = engine.get_template_libraries(engine.libraries)

    return libraries
