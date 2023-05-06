from setuptools import setup, find_packages

setup(
  name = 'global-contrast-factor-python',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'Global contrast Factor  - Python',
  author = 'Jinwon Kim',
  author_email = 'code.eric22@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/jinwonkim93/global-contrast-factor-python',
  keywords = [
    'contrast',
    'image'
  ],
  install_requires=[
    'opencv-python',
    'numpy',
  ],
)