import sns as sns

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from glob import glob

from itertools import cycle

sns.set_theme(style="white", palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
color_cyxcle = cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])