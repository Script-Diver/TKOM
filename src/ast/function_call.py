# function_call.py

from .node import Node


class FunctionCall(Node):
    def __init__(self, function_identifier, arguments, line=None, column=None):
        super().__init__(line, column)
        self.identifier = function_identifier
        self.arguments = arguments
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        return (
                isinstance(other, FunctionCall) and
                self.identifier == other.identifier and
                self.arguments == other.arguments
        )

    def __repr__(self):
        return f"[FunctionCall: {self.identifier}, {self.arguments}]"

    def accept(self, visitor):
        return visitor.visit_function_call(self)
