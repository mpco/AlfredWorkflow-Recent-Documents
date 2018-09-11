# Recent Documents / Apps

快速打开最近访问的文档、文件夹、应用。     
快速打开当前应用的最近访问文件。

系统要求：macOS 10.11+。    
10.11 未测试

[下载 Workflow](https://github.com/mpco/Alfred3-workflow-recent-documents/releases)

## 用法说明

- 使用`上下方向键`或`Ctrl-Up/Down`或`文件名过滤`选择列表中的结果。
- 对于中文文件名，支持拼音过滤。每个字的拼音之间需加空格。    
  如：`爱国教育.mp4`对应过滤语句`ai guo jiao yu .mp4`。[详细说明](https://github.com/mpco/Alfred3-workflow-recent-documents/releases/tag/2.5) 
- 按下 回车键 打开搜索结果中的文件。
- 按下 ⌘CMD+回车键 以在访达中显示文件。

### 输入`rr`，列出当前激活应用的最近文档。

举个栗子🌰️ ：

- 访达（Finder）在最前，则列出最近访问的文件夹。这样就不用再一层层地找**最近访问过**或**刚刚关闭**的文件夹了。
- 文本编辑（TextEdit）在最前，则列出最近打开过的 rtf、txt 文件。
- Sketch 在最前，则列出最近打开过的 Sketch 设计文档。
- Xcode 在最前，则列出最近打开过的 Xcode 工程。

每个条目的子标题由该文件的**⏱修改日期**与**📡路径**组成。

这个功能本质上是列出应用菜单栏中` 文件 - 打开最近使用 `内的最近文档列表。所以只要应用的菜单栏中存在` 文件 - 打开最近使用 `菜单项，就能正常工作。点击` 文件 - 打开最近使用 `中的`清除菜单` 则可清理列表。清理后，输入`rr`会显示`没有最近文件记录（None Recent Record）`。

![rr](https://user-images.githubusercontent.com/3690653/45074732-2fda4d00-b117-11e8-87a2-55684819f826.png)

### 输入`rf`，列出最近访问的文件夹。

工作过程中，常常需要打开最近访问的文件夹。虽然可以切换至访达而后输入`rr`，但为了更加高效，故额外增加了该功能。

![rf](https://user-images.githubusercontent.com/3690653/45074731-2fda4d00-b117-11e8-8d66-27e9d456fb53.png)

### 输入`rd`，列出最近打开的各种文件。  
该功能与第一个`rf`的区别在于，`rd`会列出全局的最近文档，而非针对当前应用。

![rd](https://user-images.githubusercontent.com/3690653/45074730-2f41b680-b117-11e8-8234-fd377533f396.png)

### 输入`ra`，列出最近打开的应用。

![ra](https://user-images.githubusercontent.com/3690653/45076634-7a5ec800-b11d-11e8-9e1c-f16ac17875fb.png)

### 排除隐私文件夹

你可能希望某些文件或文件夹不要出现在结果中，比如 *.avi 之类的。可以在 Workflow 环境变量`ExcludedFolders`中加入以冒号分隔的文件夹路径。这些文件夹以及其中的任何文件都不会出现在结果中。

举例：`~/privateFolder1/:/Users/G/privateFolder2/`

![excludedfolders](https://user-images.githubusercontent.com/3690653/45142715-c1b38a00-b1eb-11e8-9ace-3abeeb99f425.png)

### 可选配置：

1. 调整`rr、rf、rd、ra`这些关键词，以更加符合你的习惯或需要。
2. 打开`系统偏好设置 - 通用`，将`最近使用的项目`调整至 15 个或更多。这是因为默认的数量是 10 个，而最近使用的项目记录中有时存在已删除的文件，该 Workflow 会滤除这些已删除的结果，可能导致显示的结果偏少。

## 互助互爱

哈哈哈，这个 Workflow 是不是很棒，简直想给自己一个么么哒~    
如果这个 Workflow 让你感到很好用，请慷慨赞助（微信扫码）。

![微信赞赏码](https://user-images.githubusercontent.com/3690653/45010129-68f2be80-b03e-11e8-825f-cea7b3853342.JPG)



## 依赖项目
 
* macMRU-Parser: https://github.com/mac4n6/macMRU-Parser   
* ccl_bplist.py: https://github.com/cclgroupltd/ccl-bplist
* mac\_alias: https://pypi.python.org/pypi/mac_alias
