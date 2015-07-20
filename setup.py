from distutils.core import setup
import py2exe
import requests

setup(
	windows = [
		{
			"script": "run.py",
			"icon_resources": [(1, "wikipedia.ico")]
		}
	],
	options = {"py2exe": {"packages": ["wikipedia", "requests"]}},
	data_files=[('',[requests.certs.where()])]
)
