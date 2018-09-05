# Recent Documents / Apps

This workflow can list documents and apps opened recently.    
Especially, it can list files opened recently by the foremost app.

System: macOS 10.13+    
It should work on 10.11 and 10.12, but no test.

[Download](https://github.com/mpco/Alfred3-workflow-recent-documents/releases) [中文说明](https://github.com/mpco/Alfred3-workflow-recent-documents/blob/master/README_CN.md)

## Usage

### Tap `rr` to list files opened recently by the foremost app.
For example:

- Recent folders will be listed when Finder is foremost.
- Recent rtf, text files will be listed when TextEdit app is foremost.
- Recent *.sketch files will be listed when Sketch app is foremost.
- Recent *.xcodeproj project files will be listed when Xcode app is foremost.

The subtitle of each result consists of **⏱modified time** and **📡path** of the file.

![rr](https://user-images.githubusercontent.com/3690653/45074732-2fda4d00-b117-11e8-87a2-55684819f826.png)

### Tap `rf` to list recent folders.

Opening recent folders is very common in use. Tapping `rf` is a more efficient way, even though you can activate Finder and then tap `rr`.

![rf](https://user-images.githubusercontent.com/3690653/45074731-2fda4d00-b117-11e8-8d66-27e9d456fb53.png)

### Tap `rd` to list recent files.  

These files were recently opened by user, not like `rr` which is just for the foremost app.

![rd](https://user-images.githubusercontent.com/3690653/45074730-2f41b680-b117-11e8-8234-fd377533f396.png)

### Tap `ra` to list apps opened recently.

![ra](https://user-images.githubusercontent.com/3690653/45076634-7a5ec800-b11d-11e8-9e1c-f16ac17875fb.png)

You can press `Enter` to open the file in result, or press `⌘CMD-Enter` to reveal it in Finder.

### Optional Setup

1. Adjust keywords `rr、rf、rd、ra` as you like.
2. Open `System Preferences - General`, change the number of `Recent items` to 15 or more.

## Donation

Feel free to donate by Wechat if this workflow is helpful.

![Wechat Reward Code](https://user-images.githubusercontent.com/3690653/45010129-68f2be80-b03e-11e8-825f-cea7b3853342.JPG)

## Dependencies:
   
* macMRU-Parser: https://github.com/mac4n6/macMRU-Parser  
* ccl_bplist.py: https://github.com/cclgroupltd/ccl-bplist
* mac\_alias: https://pypi.python.org/pypi/mac_alias
