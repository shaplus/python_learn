'''
*********pip的基本使用*********
安装包:
pip install package_name  # 安装最新版本
pip install package_name==1.0.0  # 安装指定版本
pip install package_name>=1.0.0  # 安装不低于指定版本

升级包:
pip install package_name --upgrade  # 升级到最新版本

卸载包:
pip uninstall package_name

查看已安装的包:
pip list
pip freeze  # 查看已安装包及其版本（可用于requirements.txt）

导出依赖:
pip freeze > requirements.txt  # 导出当前环境依赖到requirements.txt

从依赖文件安装:
pip install -r requirements.txt  # 从requirements.txt安装依赖

使用pipreqs生成项目依赖，不包含间接依赖:
- 生成 requirements.txt：
pipreqs .   # 从当前目录生成requirements.txt，包含所有直接依赖的包
自动在当前目录生成 requirements.txt
只包含你代码里 import 的库
- 覆盖已有文件 requirements.txt:
pipreqs . --force  # 覆盖已存在的 requirements.txt 文件
- 指定输出路径:
pipreqs . --savepath ./requirements/prod.txt
- 忽略某些目录:
pipreqs . --ignore ./ignore_dir,./tests,./docs
- 离线模式（不访问 PyPI，只用本地版本）:
pipreqs . --use-local
- 指定文件编码（中文注释报错时用）:
pipreqs . --encoding utf-8
- 指定输出文件名:
pipreqs . --savepath ./requirements/prod.txt --filename prod.txt

*********conda的基本使用*********
创建环境:
conda create -n env_name python=3.11.10  # 创建名为env_name的环境，Python版本为3.11.10

- 激活环境:
conda activate env_name  # 激活名为env_name的环境

- 退出环境:
conda deactivate  # 退出当前环境

- 安装包:
conda install package_name  # 安装最新版本
conda install package_name==1.0.0  # 安装指定版本
conda install package_name>=1.0.0  # 安装不低于指定版本

'''