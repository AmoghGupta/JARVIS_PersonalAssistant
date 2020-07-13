# -*- coding: utf-8 -*-
from datetime import datetime
import pytz



IST = pytz.timezone('Asia/Kolkata')
print(IST.zone)
print(datetime.now(IST))
