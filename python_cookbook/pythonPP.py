import glob
import os

pyfiles = glob.glob('somedir/*.py')
from fnmatch import fnmatch

pyfiles = [name for name in os.listdir('somedir')
           if fnmatch(name, '*.py')]
