#coding=utf-8

import os
from public.common.readconfig import ReadConfig

# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path,'config.ini'))
# 项目参数设置
prj_path = read_config.getValue('projectConfig','project_path')
# 测试地址
base_url = read_config.getValue('projectConfig', 'base_url')
# 主页地址
home_url = read_config.getValue('projectConfig', 'home_url')
# 日志路径
log_path = os.path.join(prj_path, 'report', 'log')
# 截图文件路径
img_path = os.path.join(prj_path, 'report', 'testreport' ,'image')
# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'testreport')
# 默认浏览器
browser = 'chrome'

# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'testdata')

# yaml文件路径
yaml_path = os.path.join(prj_path, 'public', 'pages')