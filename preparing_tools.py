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


    def generate_trees(self, pathways, with_filenames=False, with_file_content=False):

        trees = []

        for filename in pathways:
            with open(filename, 'r', encoding='utf-8') as attempt_handler:
                main_file_content = attempt_handler.read()

            try:
                tree = ast.parse(main_file_content)
            except SyntaxError as e:
                print(e)
                tree = None

            if with_filenames:
                if with_file_content:
                    trees.append((filename, main_file_content, tree))
                else:
                    trees.append((filename, tree))
            else:
                trees.append(tree)

        return trees