import fnmatch
import os
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "crypto"
default_task = ["install dependencies", "analyze","publish"]
summary = 'Python Crypto lib from https://cryptopals.com/'
description = 'playpen project'
authors = [Author("Dwight J. Browne")]
version = '0.00.1'


@init
def set_properties(project):
      project.set_property('coverage_break_build', True)
      project.set_property("flake8_break_build", True)
      project.set_property("flake8_ignore", "E731,E402")
      project.set_property("flake8_include_test_sources", True)
      project.set_property("integrationtest_parallel", True)
      project.depends_on_requirements("requirements.txt")
      project.build_depends_on_requirements("requirements_build.txt")
  
#⚠     for root, dirnames, filenames in os.walk('src/main/python'):
#          root = root.replace('src/main/python/', '')
#          root = root.replace('/', '.')
#          for filename in fnmatch.filter(filenames, '*.xxxx'):
#              project.include_file(root, filename)
#      project.set_property('coverage_exceptions', [
#          'something here'
#      ])

