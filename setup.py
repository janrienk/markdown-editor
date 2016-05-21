from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(name = 'markdown-editor',
          license = 'GPLv2',
          author = 'Jan Rienk Hemminga',
          author_email = 'janrienk@gmail.com',

          packages = find_packages(),
          install_requires = [
              'markdown'
          ])