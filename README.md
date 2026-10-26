# 智能聊天机器人

## 部署到 share.streamlit.io 上

- 准备项目的源代码
- 将当前项目下已安装的 python 包资源导出到 requirements.txt 文件中:
  ```bash
  $ pip freeze > requirements.txt
  ```
- 将项目源码上传发布到 `github` 上(前提是有 `github` 账号)
- 在 `github` 个人账户中，创建新的空白仓库(可以只先取仓库名称即可，其余选择默认)
- 将项目源码文件上传到刚创建的空白仓库中(可以在仓库页面中选择上传新文件的链接点击实现上传操作)
- 访问 [https://share.streamlit.io/](https://share.streamlit.io/)，使用 `github` 用户授权登录
- 登录成功后，在 `share.streamlit.io` 控制台页面右上角，点击 `create app` 按钮创建项目
- 选择第一个 `Deploy a public app from GitHub` 从 `github` 拉取发布的项目资源
- 选择并配置账号下的待部署项目所在仓库名称、分支名称、入口文件名称、域名 --> Deploy
- 如果在部署时报错，可以在部署页面的右下角管理应用，查看报错的日志信息，并根据具体错误问题进行解决即可