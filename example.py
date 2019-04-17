import time
import sys
import datetime
import subprocess
import os
import numpy
import base64
import uuid
import datetime
import traceback
import math
import random, string
import base64
import json
from time import gmtime, strftime
import numpy as np
import math
import random, string
import time
import psutil
import scipy.misc
start = time.time()

end = time.time()
row = { }
row['host'] = os.uname()[1]
row['end'] = '{0}'.format( str(end ))
row['te'] = '{0}'.format(str(end-start))
row['battery'] = psutil.sensors_battery()[0]
row['systemtime'] = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
row['cpu'] = psutil.cpu_percent(interval=1)
usage = psutil.disk_usage("/")
row['diskusage'] = "{:.1f} MB".format(float(usage.free) / 1024 / 1024)
row['memory'] = psutil.virtual_memory().percent
row['id'] = str(uuid)
json_string = json.dumps(row)
print(json_string)
