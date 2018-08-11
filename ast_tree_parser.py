import ast

from term_classifier import TermClassifier


class AstTreeParser(TermClassifier):

    def get_all_names(self, tree):

        return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]

    def get_verbs_from_function_name(self, function_name):

        return [word for word in function_name.split('_') if self.is_verb(word)]

    def split_snake_case_name_to_words(self, name):

        return [n for n in name.split('_') if n]

    def get_target_functions(self, node_names):

        return [f for f in node_names if not (f.startswith('__') and f.endswith('__'))]

    def parse_node_names(self, trees):

        node_names = []
        for t in trees:
            node_names += [node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)]

        return node_names

