import os

URL_PREFIX = 'http://infinite-code.com'

def run():
    for i in os.walk('www'):
        dirpath, dirnames, filenames = i
        if 'index.html' in filenames:
            full_path = '%s%s/' % (URL_PREFIX, dirpath.replace('www', ''))
            print full_path

if __name__ == '__main__':
    run()
