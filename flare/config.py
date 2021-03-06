"""
Flare configuration.
"""
from .html5 import core
from .safeeval import SafeEval
from .cache import Cache

from typing import Dict

def updateConf(other: Dict):
	"""
	Merges other into conf
	"""

	global conf
	conf.update(other)
	return conf


# Main config
conf = {
	"flare.cache": Cache(),
	"flare.icon.svg.embedding.path": "/static/svgs",
	"flare.icon.fallback.error": "icon-error",
	"flare.language.current": "de",
}

# Assign SafeEval as htmlExpressionEvaluator
core.htmlExpressionEvaluator = SafeEval()

# Merge view_conf into main config
from flare.views import conf as view_conf
updateConf(view_conf)
