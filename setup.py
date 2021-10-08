# encoding:utf8

from setuptools import setup

setup(name='parallel_processor',
      # namespace_packages=['datasci'],
      version='0.1.1',
      description='Parallelling Data Processor',
      url='',
      author='lianxiaolei,wangyue',
      author_email='lian222@foxmail.com,wangyue29@tal.com',
      license='MIT',
      include_package_data=False,
      packages=['parallel_processor'],
      install_requires=[  # 依赖列表
          'numpy>=1.14.3',
      ],
      zip_safe=False)
