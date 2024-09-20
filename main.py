import sys
import tree_sitter_cpp as tscpp
from tree_sitter import Language, Parser


CPP_LANGUAGE = Language(tscpp.language())
QUERY = """
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


def file2bytes(f_input):
    with open(f_input, 'rb') as f_in:
        content = f_in.read()
    return content


def get_code(source, node):
    return source[node.start_byte:node.end_byte].decode("utf8")


def main():
    parser = Parser(CPP_LANGUAGE)
    code = file2bytes(sys.argv[1])
    query = CPP_LANGUAGE.query(QUERY)
    tree = parser.parse(code)
    matches = query.matches(tree.root_node)
    for elt in matches:
        print(get_code(code, elt[1]["value"][0]))


if __name__ == "__main__":
    main()
