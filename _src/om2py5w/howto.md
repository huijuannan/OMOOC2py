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
