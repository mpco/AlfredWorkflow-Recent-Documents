#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ~/Library/Application Support/com.apple.sharedfilelist/
# https://www.mac4n6.com/blog/2017/10/17/script-update-for-macmrupy-v13-new-1013-sfl2-mru-files

import ccl_bplist
from mac_alias import Bookmark
import sys
import os
import json


def BLOBParser_human(blob):
    # As described in:
    # http://mac-alias.readthedocs.io/en/latest/bookmark_fmt.html
    # http://mac-alias.readthedocs.io/en/latest/alias_fmt.html
    try:
        b = Bookmark.from_bytes(blob)
        return "/" + u"/".join(b.get(0x1004, default=None))
    except Exception as e:
        print e


def ParseSFL2(MRUFile):

    itemsLinkList = []
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)
        plistfile.close()
        plist_objects = ccl_bplist.deserialise_NsKeyedArchiver(
            plist, parse_whole_structure=True)

        if plist_objects["root"]["NS.keys"][0] == "items":
            items = plist_objects["root"]["NS.objects"][0]["NS.objects"]

            for n, item in enumerate(items):
                attribute_keys = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.keys"]
                attribute_values = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.objects"]
                attributes = dict(zip(attribute_keys, attribute_values))

                if "Bookmark" in attributes:
                    # print(type(attributes["Bookmark"]))
                    # print(attributes["Bookmark"])
                    if isinstance(attributes["Bookmark"], str):
                        itemLink = BLOBParser_human(attributes["Bookmark"])
                    else:
                        itemLink = BLOBParser_human(
                            attributes["Bookmark"]['NS.data'])
                    itemsLinkList.append(itemLink)
            return itemsLinkList
    except Exception as e:
        print e


# Finder 的最近访问列表与一般应用的存储方式不同，需特别处理
def ParseFinderPlist(MRUFile):
    itemsLinkList = []
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)
        plistfile.close()
        # print "Parsing FXRecentFolders Key"
        # print "[MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
        for n, item in enumerate(plist["FXRecentFolders"]):
            # print "    [Item Number: " + str(n) + "] '" + item["name"] + "'"
            # print item.keys()
            if "file-bookmark" in item:
                blob = item["file-bookmark"]
            elif "file-data" in item:
                blob = item["file-data"]["_CFURLAliasData"]
            itemLink = BLOBParser_human(blob)
            itemsLinkList.append(itemLink)
        return itemsLinkList
    except Exception as e:
        print e


if __name__ == '__main__':
    filePath = sys.argv[1]

    if filePath.endswith(".sfl2"):
        itemsLinkList = ParseSFL2(filePath)
    # Finder 的最近访问列表与一般应用的存储方式不同，需特别处理
    elif filePath.endswith("com.apple.finder.plist"):
        itemsLinkList = ParseFinderPlist(filePath)

    result = {"items": []}
    for item in itemsLinkList:
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
