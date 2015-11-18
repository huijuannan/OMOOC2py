# 实现过程
## [注册新浪云](http://www.sinacloud.com/sso/register.html)
首先，得有个帐号，简单的注册步骤，不赘述了。

## [创建新应用](http://sae.sina.com.cn/?m=dashboard)
填写必要的信息，创建二级域名，选择python作为开发语言

## 编辑应用代码
### 安装SVN
- SVN是一个用来做版本控制的工具（git也是），因为SAE采用SVN作为代码部署工具，所以要先安装SVN
```bash
$ sudo apt-get install subversion	
```

### 使用svn客户端检出应用的代码
```bash
$ svn co http://svn.sinacloud.com/xieriji
```
- 我的应用的名字叫写日记(xieriji.sinaapp.com)
- 提示输入用户名和密码，分别是注册的时候用的安全邮箱和安全密码
- 运行之后看到当前目录下多了一个`xieriji`文件夹，里面包含`.svn`文件

### 安装sae-python
```bash
$ pip install sae-python-dev
```

### 建立第一个版本
- 在`xirriji`文件夹下建立第一个版本的文件夹`1`，之后在`xieriji/1`里面创建两个文件分别是config.yaml和index.wsgi
- config.yaml输入
```
name: xieriji
version: 1
```
- index.wsgi里面即是服务器的代码，即上一周写的用bottle框架的web应用的程序
- `svn ci -m "1st version"`推送到云端

### 那么问题来了
- 打开xieriji.sinaapp.com，写入一行日记之后，本来应该打印出之前所有日记，可是却报错`500 Internal Server Error`
- 查看日记发现`IOError: [Errno 13] Permission denied: 'DiaryPool.txt' yq26`，`DiaryPool.txt`是用来存储过往日记的文档
- 也就是说，想要写入文档的操作被拒绝了
  - 我的猜想是这样的：首先在本地运行是可以成功的，而通过网络则不行，说明是sae拒绝了写入DiaryPool.txt，可能是为了保护代码的安全性，因为这个文件夹是作为代码文件夹而存在的，那么如果谁都可以写入的话肯定会出问题。
  - 应该是需要用数据库的时候了kvdb
  - 那么，用txt这种做法就是不可能实现的吗？

### 利用Storage存储过往日记
- 的确，正如之前的猜想那样，直接从本地同步上去的放置代码的文件夹里的内容是不能在浏览器上进行修改的
- 而需要用到Storage，也就相当于我们的硬盘空间，不过是放在SAE上的
- 首先，可以在SAE的控制台Storage的[界面](sae.sina.com.cn)创建一个domain。domian就是下面说到的bucket，是同一个东西。
- 我直接从网页上在这个domian里上传了DiaryPool.txt
- 把原来代码的`file = open("DiaryPool.txt","a")`换成了
```python
bucket = Bucket("diarypool")
history = bucket.get_object_contents("DiaryPool.txt")
```
- 打开xieriji.sinaapp.com发现日记可以正常显示，说明storage的确是可以存储并直接用Bucket读取的
- 那么就开始将一行日记记录到DiaryPool.txt里面。首先，发现了`put_object()`这个命令
- 于是，把读进来的一行日记直接用这个命令存起来`bucket.put_object("DiaryPool.txt", 'new diary')`
- 进入网页，发现它把之前的都抹掉了，只剩下一行新的。原来put_object是全部更新的意思
- 再次改进，改为先把之前的内容都读进来，变成一个str，然后`str + 'new diary'`,在一起全部存入DiaryPool.txt里面，于是问题解决

### kvdb

### 清空历史日记
- 首先在template里面加如一个form
```html
<form action="/" method="post">
<button type="submit" name="delete_all" class="btn btn-default">清空日记本</button>
</form>
```
- 之后在index.wsgi里面加入一个if语句`if request.forms.get('delete_all') == '':`
- 如果成立，那么把日记本的内容清空
```python
bucket = Bucket("diarypool")
bucket.put_object("DiaryPool.txt", '')
return template("welcome.tpl")
```
- 任何一个操作的行为背后都有一个表单的提交（？），即Client和Server的互动是通过表单（？）



## References
- http://sae-python.readthedocs.org/en/latest/service.html#storage

