import ast

from term_classifier import TermClassifier


class AstTreeParser(TermClassifier):


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

    def get_all_functions_names(self, tree):

        return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]

    def get_all_variables_names(self, tree):

        return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]

    def get_verbs_from_function_name(self, function_name):

        return [word for word in function_name.split('_') if self.is_verb(word)]

    def get_noun_from_function_name(self, function_name):

        return [word for word in function_name.split('_') if self.is_noun(word)]

    def split_snake_case_name_to_words(self, name):

        return [n for n in name.split('_') if n]

    def get_target_functions(self, node_names):

        return [f for f in node_names if not (f.startswith('__') and f.endswith('__'))]

    def parse_node_names(self, trees):

        node_names = []
        for t in trees:
            node_names += [node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)]

        return node_names

