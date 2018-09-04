#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import sys
import os

with open(sys.argv[1]) as ff:
    jsonObj = json.load(ff)
recentFileList = jsonObj["settings"]["new_window_settings"]["file_history"][1:10]

result = {"items": []}

for item in recentFileList:
        if not os.path.exists(item):
            continue
        temp = {}
        temp["type"] = "file"
        temp["title"] = os.path.basename(item)
        temp["autocomplete"] = temp["title"]
        temp["icon"] = {"type": "fileicon", "path": item}
        temp["subtitle"] = item
        temp["arg"] = item
        result['items'].append(temp)
if result['items']:
    print json.dumps(result)
else:
    # 列表为空时
    print '{"items": [{"title": "None Recent Record","subtitle": "(*´･д･)?"}]}'
