from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='pyKeksik',
      version='1.2',
      url='https://github.com/Friendosie/pyKeksik',
      license='MIT',
      description='Неофициальная библиотека для работы с API https://keksik.io',
      packages=['pyKeksik'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Friendosie',
      install_requires=['requests'],
      author_email='friendosie@gmail.com',
      zip_safe=False)