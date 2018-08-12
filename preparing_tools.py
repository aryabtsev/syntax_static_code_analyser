import os
import logging
import ast

from git import Repo

curr_path = os.path.dirname(os.path.abspath(__file__))

logger = logging.getLogger('preparing tools')
hdlr = logging.FileHandler(os.path.join(curr_path, 'error.log'))
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


class PrepareCode():


    def fetch_git_repo(self, git_link, local_path):

        try:
            Repo.clone_from(git_link, local_path)
        except Exception as e:
            print('Unable to clone remote git repo to local dir')
            logging.error(f'error: {e}')
            return False
        return local_path


    def get_filename_path (self, path, file_format = '.py'):
        '''принимает на вход путь -> список путей до каждого из .py файлов'''
        pathways = []

        for dirname, dirs, files in os.walk(path, topdown=True):
            for file in files:
                if file.endswith(file_format):
                    pathways.append(os.path.join(dirname, file))

        print('total %s files' % len(pathways))

        return pathways
