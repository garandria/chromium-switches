import sys
import tree_sitter_cpp as tscpp
from tree_sitter import Language, Parser


CPP_LANGUAGE = Language(tscpp.language())
QUERY_SIMPLE = """
(
  (namespace_definition
    name: [(namespace_identifier)
    	   (nested_namespace_specifier)] @namespace_name
    body: (declaration_list
      (declaration
        type: (primitive_type) @type
        declarator: (init_declarator
          declarator: (array_declarator
            declarator: (identifier) @name)
          value: (string_literal) @value
        ))
      (#eq? @type "char")
    )
  )
  (#match? @namespace_name ".*switch.*")
)
"""
QUERY_PREPROC = """
(
  (namespace_definition
    name: [(namespace_identifier)
    	   (nested_namespace_specifier)] @namespace_name
    body: (declaration_list
    ((preproc_if
    	condition: [(call_expression) (binary_expression)] @cond
        _
      (declaration
        type: (primitive_type) @type
        declarator: (init_declarator
          declarator: (array_declarator
            declarator: (identifier) @name)
          value: (string_literal) @value
        ))))
      (#eq? @type "char")
    )
  )
  (#match? @namespace_name ".*switch.*")
)
"""


def file2bytes(f_input):
    with open(f_input, 'rb') as f_in:
        content = f_in.read()
    return content


def get_code(source, node):
    return source[node.start_byte:node.end_byte].decode("utf8")


def main():
    parser = Parser(CPP_LANGUAGE)
    src = sys.argv[1]
    code = file2bytes(src)
    tree = parser.parse(code)
    query_simple = CPP_LANGUAGE.query(QUERY_SIMPLE)
    matches_simple = query_simple.matches(tree.root_node)
    query_prepro = CPP_LANGUAGE.query(QUERY_PREPROC)
    matches_preproc = query_prepro.matches(tree.root_node)
    for elt in matches_simple:
        content = get_code(code, elt[1]['value'][0])
        print(f"{content},")
    for elt in matches_preproc:
        content = get_code(code, elt[1]['value'][0])
        cond = get_code(code, elt[1]['cond'][0])
        print(f"{content},{cond}")


if __name__ == "__main__":
    main()
