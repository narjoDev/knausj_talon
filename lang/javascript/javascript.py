from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
code.language: javascript
code.language: typescript
code.language: javascriptreact
code.language: typescriptreact
"""

ctx.lists["user.code_common_function"] = {
    "fetch": "fetch",
    "log": "console.log",
    "print": "console.log",
    # classes
    "struck": "constructor",
    "super": "super",
    # Math
    "abs": "Math.abs",
    "ceiling": "Math.ceil",
    "seal": "Math.ceil",
    "floor": "Math.floor",
    "max": "Math.max",
    "min": "Math.min",
    "random": "Math.random",
    "round": "Math.round",
    # numbers
    "is nan": "Number.isNaN",
    "parse int": "parseInt",
    # Object
    "entries": "Object.entries",
    "from entries": "Object.fromEntries",
    "keys": "Object.keys",
    "values": "Object.values",
    # VENDOR SPECIFIC
    # browser
    "prompt": "prompt",
    # node
    "require": "require",
}

mod.list("code_common_member_function", "Function to use in a dotted chain, eg .foo()")

ctx.lists["user.code_common_member_function"] = {
    "catch": "catch",
    "concat": "concat",
    "filter": "filter",
    "finally": "finally",
    "find": "find",
    "flat map": "flatMap",
    "for each": "forEach",
    "join": "join",
    "includes": "includes",
    "map": "map",
    "pop": "pop",
    "push": "push",
    "reduce": "reduce",
    "slice": "slice",
    "some": "some",
    "split": "split",
    "substring": "substring",
    "then": "then",
    # maps and sets
    "add": "add",
    "delete": "delete",
    "get": "get",
    "has": "has",
    "set": "set",
    # regular expressions and strings
    "match": "match",
    "test": "test",
}

ctx.lists["user.code_keyword"] = {
    "a sink": "async ",
    "await": "await ",
    "break": "break",
    "class": "class ",
    "const": "const ",
    "continue": "continue",
    "default": "default ",
    "export": "export ",
    "false": "false",
    "function": "function ",
    "import": "import ",
    "let": "let ",
    "nan": "NaN",
    "new": "new ",
    "null": "null",
    "private": "private ",
    "protected": "protected ",
    "public": "public ",
    "return": "return ",
    "throw": "throw ",
    "true": "true",
    "try": "try ",
    "undefined": "undefined",
    "yield": "yield ",
}


@ctx.action_class("user")
class UserActions:
    def code_insert_is_not_null():
        actions.auto_insert(" !== null")

    def code_insert_is_null():
        actions.auto_insert(" === null")

    def code_block():
        actions.user.insert_between("{", "}")
        actions.key("enter")

    def code_state_if():
        actions.user.insert_between("if (", ")")

    def code_state_else_if():
        actions.user.insert_between(" else if (", ")")

    def code_state_else():
        actions.user.insert_between(" else {", "}")
        actions.key("enter")

    def code_self():
        actions.auto_insert("this")

    def code_operator_object_accessor():
        actions.auto_insert(".")

    def code_state_while():
        actions.user.insert_between("while (", ")")

    def code_state_do():
        actions.auto_insert("do ")

    def code_state_return():
        actions.insert("return ")

    def code_state_for():
        actions.user.insert_between("for (", ")")

    def code_state_switch():
        actions.user.insert_between("switch (", ")")

    def code_state_case():
        actions.user.insert_between("case ", ":")

    def code_state_go_to():
        actions.auto_insert("")

    def code_import():
        actions.auto_insert("import ")

    def code_define_class():
        actions.auto_insert("class ")

    def code_state_for_each():
        actions.user.insert_between(".forEach(", ")")

    def code_break():
        actions.auto_insert("break;")

    def code_next():
        actions.auto_insert("continue;")

    def code_insert_true():
        actions.auto_insert("true")

    def code_insert_false():
        actions.auto_insert("false")

    def code_insert_null():
        actions.auto_insert("null")

    def code_operator_lambda():
        actions.auto_insert(" => ")

    def code_operator_subscript():
        actions.user.insert_between("[", "]")

    def code_operator_assignment():
        actions.auto_insert(" = ")

    def code_operator_subtraction():
        actions.auto_insert(" - ")

    def code_operator_subtraction_assignment():
        actions.auto_insert(" -= ")

    def code_operator_addition():
        actions.auto_insert(" + ")

    def code_operator_addition_assignment():
        actions.auto_insert(" += ")

    def code_operator_multiplication():
        actions.auto_insert(" * ")

    def code_operator_multiplication_assignment():
        actions.auto_insert(" *= ")

    def code_operator_exponent():
        actions.auto_insert(" ** ")

    def code_operator_division():
        actions.auto_insert(" / ")

    def code_operator_division_assignment():
        actions.auto_insert(" /= ")

    def code_operator_modulo():
        actions.auto_insert(" % ")

    def code_operator_modulo_assignment():
        actions.auto_insert(" %= ")

    def code_operator_equal():
        actions.auto_insert(" == ")

    def code_or_operator_assignment():
        actions.auto_insert(" ||= ")

    def code_operator_not_equal():
        actions.auto_insert(" != ")

    def code_operator_greater_than():
        actions.auto_insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.auto_insert(" >= ")

    def code_operator_less_than():
        actions.auto_insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.auto_insert(" <= ")

    def code_operator_and():
        actions.auto_insert(" && ")

    def code_operator_or():
        actions.auto_insert(" || ")

    def code_operator_bitwise_and():
        actions.auto_insert(" & ")

    def code_operator_bitwise_and_assignment():
        actions.auto_insert(" &= ")

    def code_operator_bitwise_or():
        actions.auto_insert(" | ")

    def code_operator_bitwise_or_assignment():
        actions.auto_insert(" |= ")

    def code_operator_bitwise_exclusive_or():
        actions.auto_insert(" ^ ")

    def code_operator_bitwise_exclusive_or_assignment():
        actions.auto_insert(" ^= ")

    def code_operator_bitwise_left_shift():
        actions.auto_insert(" << ")

    def code_operator_bitwise_left_shift_assignment():
        actions.auto_insert(" <<= ")

    def code_operator_bitwise_right_shift():
        actions.auto_insert(" >> ")

    def code_operator_bitwise_right_shift_assignment():
        actions.auto_insert(" >>= ")

    def code_comment_line_prefix():
        actions.auto_insert("//")

    def code_insert_function(text: str, selection: str):
        text += f"({selection or ''})"
        actions.user.paste(text)
        actions.edit.left()

    def code_default_function(text: str):
        """Inserts function declaration without modifiers"""
        result = "function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    # def code_private_static_function(text: str):
    #     """Inserts private static function"""
    #     result = "private static void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_private_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)

    def code_protected_function(text: str):
        result = "function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    # def code_protected_static_function(text: str):
    #     result = "protected static void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_protected_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)

    def code_public_function(text: str):
        result = "function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    # def code_public_static_function(text: str):
    #     result = "public static void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_public_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)
