# django实战
## 准备工作
安装完python后，要把python的路径添加到环境变量中， 才可以在命令行中直接使用python。pip是python的模块管理工具，在python文件夹的Scripts中，直接安装完成后并不可以直接使用，因此要把Scripts这个文件夹也添加到环境变量中才可以使用。
>使用pip安装的模块都会在Scripts中有一个执行的环境，因此把Scripts添加到环境变量中很重要。
### 安装virtualenv
virtualenv是一个虚拟的python运行环境。目的是为了保证项目所依赖的模块不会发生变动。
- 安装：pip install virtualenv
- 使用：
    - 先创建一个存储所有virtualenv的目录
    - 然后创建一个新的虚拟环境：virtualenv 目录/projectname --no-site-packages(这个参数的意思是不安装本机安装过的模块，为了创建一个干净的环境)
    - 激活虚拟环境：
        - cd 目录/projectname/Scripts
        - source activate
        - (我在安装的时候source命令不识别)
    - 停止使用：deactivate
### 安装Django
Django是python下面一个很流行的web开发框架，是一个MTV框架。Django的每一个模块在内部被称之为APP，在每个APP里都有自己的三层结构。
- 安装：pip install django
- 使用：
    - 新建一个项目：django-admin startproject blog
    - 运行内部服务器：python manage.py runserver 127.0.0.1:8000
    - Django后台
    这是Django自带的一套后台管理系统。
        - python manage.py migrate(先迁移数据库)
        - python manage.py createsuperuser(创建用户名和密码)
### 第一次提交
- git add . 提交所有文件
- git reset filename    重置某个文件的状态
- 添加忽略名单.gitignore文件：
- git reset .   重置所有文件状态
- 然后就可以：git commit -m 'msg'     git push    提交了

### django连接mysql
测试成功的情况是在python3.6和mysql5.7的情况下。其他情况未尝试。
1. 安装mysql，可以按照教程来安装，最新版的mysql里面包含的内容比较多，所以可以选择只安装MySQL server。
2. （在Python、django已经安装好的情况下，如果未安装好，请先分别安装这两个。）使用pip安装mysqlclient（暂时只在python3.6下安装成功了，python2.7下安装会报Microsoft Visual C++ 9.0没有安装，安装完之后还会报一个其他的错误，可能是版本不兼容）。
3. 使用django创建项目，django-admin startproject projectname。在settings.py里面配置数据库连接
```python
django-admin startproject name
cd name
python manage.py startapp appname
```
4. 在app里面的models创建类（就是要在数据库里面生成的表）。创建完成后要
```python
python manage.py makemigrations(要在类有修改之后使用。1)
python manage.py migrate(类建好之后使用。2)
```
5. 要是用的时候，
```python
from appname.models import Classname
Classname.obejcts.all() #就可以获取Classname里面的所有数据
```
至此django连接mysql是可以正常使用了。

### django使用virtualenv
virtualenv是一个虚拟的python运行环境，他可以和系统的共享库和其他的virtualenv隔离开，因此当我们需要在同一台电脑上使用不同的版本的库的时候，就需要安装一个virtualenv虚拟环境，接下来是总结的在windows下使用virtualenv的一些情况，以记录我之前一直尝试不成功的情况。
1. 安装：直接使用pip install virtualenv，安装就好，安装完成后，他会在python的site-packages里面。
2. 使用：virtualenv name，可以直接创建一个虚拟环境，默认参数是--no-site-packages。指的是不使用系统的库。cd name    Scripts\activate.bat(即可以激活虚拟环境[目前的尝试只在cmd中可以使用，在powershell中没有效果。])，deactivate.bat，即可以关闭虚拟环境。(用的是直接Scripts下面的activate.bat激活的虚拟环境，不是source，可能在linux环境下是用的source，在windows下无法使用)

