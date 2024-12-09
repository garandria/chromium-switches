use tree_sitter::{Language, Parser};
use tree_sitter_cpp::{LANGUAGE};
use std::env;
use std::fs;

fn main() {
    let mut parser = Parser::new();
    let language = LANGUAGE;
    parser
	.set_language(&language.into())
	.expect("Error loading C++ parser");
    let filename = std::env::args().nth(1).expect("No filename provided");
    let content = fs::read_to_string(filename).expect("Failed to read the file");
    let mut tree = parser.parse(content, None).unwrap();
    let root_node = tree.root_node();
}
