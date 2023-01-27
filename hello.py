#!/usr/bin/env python3

import os
import json
import cgitb
cgitb.enable()

print("Content-type:text/html\r\n\r\n")

env_json = json.dumps(dict(os.environ), indent=2)
print(env_json)

for param in os.environ.keys():
    if param == "QUERY_STRING":
        print("<br><br>%20s: %s" % (param, os.environ[param]))

for param in os.environ.keys():
    if param == "HTTP_USER_AGENT":
        print("<br><br>%20s: %s<br>" % (param, os.environ[param]))