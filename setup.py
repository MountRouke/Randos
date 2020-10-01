import setuptools

setuptools.setup(name='derk_randos.py',
  py_modules=['derk_randos'],
  version='0.1.0',
  author='Fredrik Norén',
  author_email='contact@mountrouke.com',
  packages=setuptools.find_packages(),
  install_requires=[
    'gym-derk',
  ],
  include_package_data=True,
  python_requires='>=3.6')
