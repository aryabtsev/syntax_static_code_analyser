import collections
import some_utils
from preparing_tools import PrepareCode
from ast_tree_parser import AstTreeParser
from term_classifier import TermClassifier


class CodeAnalyser (AstTreeParser, PrepareCode, TermClassifier):

    def __init__(self):
        pass

    def get_all_words_in_path(self, path):

        trees = self.generate_trees(path)
        names = some_utils.flat([self.get_all_names(t) for t in trees])
        functions = self.get_target_functions(names)
        split_name = [self.split_snake_case_name_to_words(fnctn_name) for fnctn_name in functions]

        return some_utils.flat(split_name)


    def get_top_verbs_in_path(self, path, top_size=10):
        '''сделать универсальную функцию с параметром term (выбор части речи)'''

        pathways = self.get_filename_path(path)
        trees = self.generate_trees(pathways)
        node_names = self.parse_node_names(trees)
        target_functions = self.get_target_functions(node_names)
        verbs = some_utils.flat([self.get_verbs_from_function_name(function_name) for function_name in target_functions])

        return collections.Counter(verbs).most_common(top_size)

    def get_top_functions_names_in_path(self,path, top_size=10):

        trees = self.generate_trees(path)
        node_names = self.parse_node_names(trees)
        target_functions = self.get_target_functions(node_names)

        return collections.Counter(target_functions).most_common(top_size)
