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