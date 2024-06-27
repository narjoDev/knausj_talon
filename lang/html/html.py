# fully lifted from Andreas
from talon import Module, Context

mod = Module()
mod.list("code_tag", desc="HTML tags")

ctx = Context()
ctx.matches = r"""
code.language: html
code.language: javascriptreact
code.language: typescriptreact
"""

# TODO: see Andreas code_inserts.py
# ctx.lists["user.code_insert"] = {
#     "doctype": "<!DOCTYPE html>\n",
#     "blank": "&nbsp;",
# }

tag_names_list = {
    "html",
    "head",
    "body",
    "header",
    "footer",
    "main",
    "aside",
    "div",
    "span",
    "table",
    "template",
    "script",
    "nav",
    "button",
    "input",
    "textarea",
    "select",
    "option",
    "form",
    "label",
    "Link",
    "hr",
    "em",
    "strong",
}

# fmt: off
tag_names = {
    "anchor":           "a",
    "table headers":    "thead",
    "table body":       "tbody",
    "table foot":       "tfoot",
    "table row":        "tr",
    "table head":       "th",
    "table cell":       "td",
    "olist":            "ol",
    "unlist":           "ul",
    "list item":        "li",
    "image":            "img",
    "harp one":         "h1",
    "harp two":         "h2",
    "harp three":       "h3",
    "harp four":        "h4",
    "harp five":        "h5",
    "harp six":         "h6",
    "break":            "br",
    "graph":            "p",
    "pea":              "p",
    "lick":             "em"
}
# fmt: on

ctx.lists["user.code_tag"] = {
    **{n: n for n in tag_names_list},
    **tag_names,
}
