# function_call.py

if __name__ == "__main__":
    from node import Node
elif __name__ == "function_call":
    from node import Node
else:
    from .node import Node


class FunctionCall(Node):
    def __init__(self, function_identifier, arguments):
        super().__init__()
        self.identifier = function_identifier
        self.arguments = arguments

    # TODO
    def visit(self):
        return self.identifier

    def __repr__(self):
        return f"[FunctionCall: {self.identifier}, {self.arguments}]"