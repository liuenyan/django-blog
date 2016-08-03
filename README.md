# Django Blog

一个使用Django框架开发的博客程序。

## 依赖包安装

1. 安装virtualenv和virtualenvwrapper。
2. 使用virtualenvwrapper创建虚拟环境：

   ```shell
   mkvirtualenv django-blog
   ```

3. 切换到虚拟环境并安装依赖。

   ```shell
   workon django-blog
   pip install -r requirements.txt
   ```

4. 安装前端开发工具依赖：

   ```shell
   npm install
   ```

## 数据库初始化

1. 执行数据库迁移：
   
   ```shell
   ./manage.py migrate
   ```

2. 创建超级用户，根据提示完成用户的创建：
   
   ```shell
   ./manage.py createsuperuser
   ```
    
