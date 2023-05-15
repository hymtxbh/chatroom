# 工程介绍
tornado聊天室

## 1.安装依赖包
    pip install -r requirements.txt
    tornado:服务器端web框架
    mysql-connector-python:mysql数据库连接驱动
    sqlalchemy:数据库ORM
    sockjs-tornado:websocket通信库
    wtforms:表单验证库
    weekzeug:wsgi工具箱，主要用加密机制

## 2.构建项目目录
    app 存放MTV包
        __init__.py 初始化模块，自定义应用
        configs.py 配置信息模块
        urls.py 路由
        params.py 公共参数模块
        models 模型包
            __init__.py 初始化模块
            crud.py 增删改查
            models.py 数据库表模型
        templates 模板目录
            layout.html 公共布局模板
            regist.html 会员注册模板
            login.html 会员登录模板
            userprofile.html 会员中心模板
            chat.html 聊天室模板
        views 视图包
            __init__.py 初始化
            views_regist.py 注册视图
            views_login.py 登录视图
            views_layout.py 退出视图
            views_userprofile.py 修改个人资料视图
            views_uploads.py 上传模块
            views_user.py 会员权限控制视图
            views_common.py 公共视图模块
            views_chat.py 聊天室模块
            views_chatroom.py websocket全双工通信视图
            views_msg.py 获取历史消息视图
        static 静态资源
            css 样式
            dist bootstrap依赖
            images 图片
            js 脚本
                chat.js websocket聊天
                request.js ajax请求
                upload.js 上传图片文件
            pages 原始模板目录
            ue ueditor编辑器
            uploads 上传图片保存目录
            constellation 星座素材
        tools 工具包
            __init__.py 初始化
            forms.py 表单校验器
            orm.py 数据库驱动连接