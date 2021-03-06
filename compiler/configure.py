API_VERSION = '2.1'

import sys
try:
  from ambuild2 import run
  if not run.HasAPI(API_VERSION):
    raise Exception()
except:
  sys.stderr.write('AMBuild {0} must be installed to build this project.\n'.format(API_VERSION))
  sys.stderr.write('http://www.alliedmods.net/ambuild\n')
  sys.exit(1)

builder = run.BuildParser(sourcePath = sys.path[0], api=API_VERSION)

builder.options.add_option('--default-script', action='store_true', dest='default', default=False,
                        help='Hardcodes test.x as the compilation script')
builder.options.add_option('--debug-all', action='store_true', dest='debugall', default=False,
                        help='Enables all debug prints')
builder.options.add_option('--debug-parser', action='store_true', dest='debugparser', default=False,
                        help='Enables parser debug prints')

builder.Configure()