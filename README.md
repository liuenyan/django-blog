# Django Blog

一个使用Django框架开发的博客程序。

## 依赖包安装

1. 安装virtualenv和virtualenvwrapper。
2. 使用virtualenvwrapper创建虚拟环境：

   ```
   mkvirtualenv django-blog
   ```

3. 切换到虚拟环境并安装依赖。

   ```
   workon django-blog
   pip install -r requirements.txt
   ```

4. 安装前端开发工具依赖：

   ```
   npm install
   ```

## 数据库初始化

1. 执行数据库迁移：

   ```
   ./manage.py migrate
   ```

2. 创建超级用户，根据提示完成用户的创建：

   ```
   ./manage.py createsuperuser
   ```

## 部署到服务器

### 基于 ubuntu 16.04 / nginx / uwsgi 的部署

1. 安装软件包

   ```
   apt install uwsgi uwsgi-extra uwsgi-emperor uwsgi-plugin-python3 nginx
   ```

2. 创建虚拟环境，见上述的依赖包安装部分。
3. 部署配置文件。配置文件内容参考deployment目录。
