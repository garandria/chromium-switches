import sys
import tree_sitter_cpp as tscpp
from tree_sitter import Language, Parser
import json


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


def get_code_range(source, start, end):
    return source[start:end].decode("utf8")


def get_code(source, node):
    return get_code_range(source, node.start_byte, node.end_byte)


def get_description(source, node):
    npc = node.parent.parent.prev_sibling
    st = []
    while npc is not None and npc.type == "comment":
        if get_code(source, npc).startswith("//"):
            st.append(npc)
            npc = npc.prev_sibling
    if st:
        coms = get_code_range(source, st[-1].start_byte, st[0].end_byte)
        return coms.split("\n\n").pop().replace("//", "").replace("\n", " ")
    return ""


def switches_from_file(filepath):
    parser = Parser(CPP_LANGUAGE)
    src = filepath
    code = file2bytes(src)
    tree = parser.parse(code)
    query = CPP_LANGUAGE.query(QUERY)
    matches = query.matches(tree.root_node)
    switches = dict()
    for c, m in matches:
        sw_node = m['value'][0]
        switch = get_code(code, sw_node).strip('"')
        variable = get_code(code, m['name'][0])
        switches[switch] = {'preproc': '',
                            'location': src,
                            'description': get_description(code, sw_node),
                            'variable': variable}
        if c == 1:
            cond = get_code(code, m['cond'][0]).replace("\\\n", "")
            switches[switch]['preproc'] = cond
    return switches


def main():
    params = list(set(sys.argv[1:]))
    switches = dict()
    for p in params:
        sw_ = switches_from_file(p)
        for k, v in sw_.items():
            if k in switches:
                if switches[k]["preproc"] == "":
                    if sw_[k]["preproc"] != "":
                        switches[k] = sw_[k]
                    elif switches[k]["description"] == "":
                        if sw_[k]["description"] != "":
                            switches[k] = sw_[k]
            else:
                switches[k] = v
        # switches.update(switches_from_file(p))
    with open("switches.json", "w") as out_stream:
        json.dump(dict(sorted(switches.items())), out_stream, indent=4)
if __name__ == "__main__":
    main()
