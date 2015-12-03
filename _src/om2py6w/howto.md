# 微信公众号版日记
## 从sae转移到aws
### 本地设置虚拟python环境
- 安装AWS Elastic Beanstalk CLI `pip install awsebcli`
- 用它可以创建、配置和部署应用程序
- `eb --version`来测试安装是否成功
- 安装virtualenv安装包`pip install virtualenv`
- 安装成功，下一步设置虚拟环境`virtualenv -p python2.7 /tmp/onelinediary/`,其中onelinediary是应用的名字作为文件夹的名称
- 报错，安装不成功，考虑可能是因为现在系统默认的是canopy python
- 重新用绝对路径选择正常的python `virtualenv -p /usr/bin/python /tmp/onelinediary/`，报错说文件已存在
- 把`/tmp/onelinediary`文件夹全部删除，重新安装，成功

### 安装django
- `pip install django`
- `pip freeze`检查安装上了没
- `django-admin startproject django_eb`创建项目
- `tree`检查建立的目录
```bash
django_eb
    ├── django_eb
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
    ```
    - `cd django_eb`
    - `python manage.py migrate`这个我也不知道是在干啥，回头再研究
    
    ### 为AWS Elastic Beanstalk 配置Django应用程序
    - 将虚拟环境中的安装包的名称和版本复制到requirements.txt, AWS会加载该文件以安装应用程序需要的程序包
    - 停用虚拟环境
    ```bash
    pip freeze > requirements.txt
    deactivate
    ```
   - 使用`eb init --region us-west-2`来创建一个AWS EB配置
     - 其中`us-west-2是要使用AWS区域`，我的页面打开发现地址栏也是这个，所以就用了
     - 输入之后它会提示要输入一个`aws-access-id`,这个要到`IAM用户证书-访问密钥`页面去创建，在自己账户的控制台就能找到
     - 然后输入`aws-secret-key`就是刚刚创建的那个
     - 之后选择应用程序，就成功了，文件夹里多了好多东西
     - 在`onelinediary`文件夹下创建了一个`.ebextentions`目录，在其中创建一个`01-django_eb.config`的新文件，内容为：
     ```
     option_settings:
  "aws:elasticbeanstalk:application:environment":
    DJANGO_SETTINGS_MODULE: "django_eb.settings"
    PYTHONPATH: "/opt/python/current/app/eb_django_app/django_eb:$PYTHONPATH"
  "aws:elasticbeanstalk:container:python":
    WSGIPath: "eb_django_app/django_eb/django_eb/wsgi.py"
     ```
     -对比doc里面的内容把路径改了一下，因为我的多一层`eb_django_app`，不知道是不是会成功

- 部署Django应用程序
  - `eb create`，提示的环境和cname都用默认值，就开始部署了
  - `eb open`就打开了一个浏览器，打开了网页啦，但是还是aws默认的那些，看来django没有配置成功呢
  -

     