from distutils.core import setup

setup(name='gnome-maintainer',
      version='0.9',
      description='Python script to collate release information for GNOME projects',
      author='Martyn Russell',
      author_email='martyn@lanedo.com',
      url='https://github.com/curlybeast/gnome-maintainer',
      scripts = [
        'gnome-maintainer.py'
      ]
)
