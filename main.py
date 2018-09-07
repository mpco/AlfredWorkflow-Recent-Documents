#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ~/Library/Application Support/com.apple.sharedfilelist/
# https://www.mac4n6.com/blog/2017/10/17/script-update-for-macmrupy-v13-new-1013-sfl2-mru-files

import ccl_bplist
from mac_alias import Bookmark
import sys
import os
import json
import time


def BLOBParser_human(blob):
    # As described in:
    # http://mac-alias.readthedocs.io/en/latest/bookmark_fmt.html
    # http://mac-alias.readthedocs.io/en/latest/alias_fmt.html
    try:
        b = Bookmark.from_bytes(blob)
        return "/" + u"/".join(b.get(0x1004, default=None))
    except Exception as e:
        print e


# for 10.13
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
                        itemLink = BLOBParser_human(attributes["Bookmark"]['NS.data'])
                    itemsLinkList.append(itemLink)
            return itemsLinkList
    except Exception as e:
        print e


# for 10.11, 10.12
def ParseSFL(MRUFile):
    itemsLinkList = []
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)
        plistfile.close()
        plist_objects = ccl_bplist.deserialise_NsKeyedArchiver(plist, parse_whole_structure=True)

        if plist_objects["root"]["NS.keys"][2] == "items":
            items = plist_objects["root"]["NS.objects"][2]["NS.objects"]
            for n, item in enumerate(items):
                # item["URL"]['NS.relative'] file:///xxx/xxx/xxx
                filePath = item["URL"]['NS.relative'][7:]
                # /xxx/xxx/xxx/ the last "/" make basename func not work
                if filePath[-1] == '/':
                    filePath = filePath[:-1]
                itemsLinkList.append(filePath)
            return itemsLinkList
    except Exception as e:
        print e


# for Finder
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
            # exclude / path
            if itemLink == "/":
                continue
            itemsLinkList.append(itemLink)
        return itemsLinkList
    except Exception as e:
        print e


# for Sublime Text 3
def ParseSublimeText3Session(sessionFile):
    with open(sys.argv[1]) as ff:
        jsonObj = json.load(ff)
    itemsLinkList = jsonObj["settings"]["new_window_settings"]["file_history"][0:15]
    return itemsLinkList


def checkFilesInExcludedFolders(fileList):
    folderListStr = os.environ["ExcludedFolders"]
    folderList = folderListStr.split(":")
    for folderPath in folderList:
        folderPath = os.path.expanduser(folderPath)
        if os.path.exists(folderPath) and os.path.isdir(folderPath):
            # 为了防止 /xxx/xx 和 /xxx/xx x/xx 误判
            if folderPath[-1] != "/":
                folderPath += "/"
            for i, filePath in enumerate(fileList):
                if os.path.isdir(filePath):
                    filePath += "/"
                if filePath.startswith(folderPath):
                    del fileList[i]
    return fileList


if __name__ == '__main__':
    allItemsLinkList = []
    for filePath in sys.argv[1:]:
        if filePath.endswith(".sfl2"):
            itemsLinkList = ParseSFL2(filePath)
        elif filePath.endswith("com.apple.finder.plist"):
            itemsLinkList = ParseFinderPlist(filePath)
        elif filePath.endswith(".sfl"):
            itemsLinkList = ParseSFL(filePath)
        elif filePath.endswith(".sublime_session"):
            itemsLinkList = ParseSublimeText3Session(filePath)
        allItemsLinkList.extend(itemsLinkList)
    allItemsLinkList = checkFilesInExcludedFolders(allItemsLinkList)

    result = {"items": []}
    for item in allItemsLinkList:
        # 滤除不存在的条目
        if not os.path.exists(item):
            continue
        modifiedTimeSecNum = os.path.getmtime(item)
        modifiedTime = time.strftime("%d/%m %H:%M", time.localtime(modifiedTimeSecNum))
        temp = {}
        temp["type"] = "file"
        temp["title"] = os.path.basename(item)
        temp["autocomplete"] = temp["title"]
        temp["icon"] = {"type": "fileicon", "path": item}
        temp["subtitle"] = u"🕒 " + modifiedTime + u" 📡 " + item.replace(os.environ["HOME"], "~")
        temp["arg"] = item
        result['items'].append(temp)
    if result['items']:
        print json.dumps(result)
    else:
        # 列表为空时
        print '{"items": [{"title": "None Recent Record","subtitle": "(*´･д･)?"}]}'
