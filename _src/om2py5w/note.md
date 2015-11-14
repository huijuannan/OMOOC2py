# 大妈演示demo要点记录

- `$ python CLI.py`
  - 显示版本号，Usage: ...
  - Usage包括 -D 或者 -U, D 是Debugging, U 是User
- `$ python CLI.py -U`
  - 和以前一样的界面，先以往日记，并提示输入新的日记
  - 比以往（打印帮助、退出、同步）多出了几个功能：
    - 标签清单
    - 设定、清除标签
    - 清空所有
  - st:标签名称可以新建一个标签，并且转到新的标签下，提示符为标签名称
  - st：什么都不加就到了默认标签
- 打开zoomquiet.sinaapp.com
- 调试和部署
  - 用开发服务器启动在本地 `dev_server.py --storage-path=log/data --kvdb-file=logs/kvdb.pkl`
  - `python CLI.py -D`
  - `vim config.py` 可以修改版本号，在运行CLI.py时显示
  - 有文件夹views，里面都是html文件，打开views/base.html，修改它就可以部署到远程`saecloud deploy`
 
 
