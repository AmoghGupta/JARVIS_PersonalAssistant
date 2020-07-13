# -*- coding: utf-8 -*-

import os
output = os.popen("find / -iname *.app").read()

print(output)