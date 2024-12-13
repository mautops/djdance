# Dev Container(推荐)

> 使用 dev container 搭建开发环境

> 要求本地支持 docker

> [REF: dev container](https://code.visualstudio.com/docs/remote/containers)

## 1. 安装 vscode 插件

1. Dev Container
   ![Dev Container](./screenshots/devcontainer.png)

2. Remote SSH

   ![Remote SSH](./screenshots/remote-ssh.png)

## 2. 使用 dev container

![UseDev](./screenshots/use-dev.png)

# 本地开发搭建

## 1. 创建虚拟环境

> [REF: pyenv installation](https://github.com/pyenv/pyenv-installer)

```shell
# install python interpreter
pyenv install 3.10.13

# create virtual env
pyenv virtualenv 3.10.13 djDance

# activate virtual env
pyenv local djDance
```

## 2. 安装依赖

```shell
pip install -r requirements.txt
```

## 3. 配置本地环境变量

> [REF: direnv installation](https://github.com/direnv/direnv)

```shell
# create env file
echo "export RUN_ENV=DEVELOP" > .envrc

# apply env
direnv allow
```

## 4. 运行项目

```shell
make migrations
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@cvte.com --phone 16866666666
python manage.py runserver 0.0.0.0:8000
```
