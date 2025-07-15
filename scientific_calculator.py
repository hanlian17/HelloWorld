#!/usr/bin/env python3
"""A simple scientific calculator supporting various math operations."""
import math
import sys

ALLOWED_NAMES = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
ALLOWED_NAMES.update({"abs": abs, "round": round})

def safe_eval(expr: str):
    """Safely evaluate a mathematical expression using a restricted
    set of built-in functions from the math module."""
    code = compile(expr, "<string>", "eval")
    for name in code.co_names:
        if name not in ALLOWED_NAMES:
            raise NameError(f"Use of name '{name}' is not allowed")
    return eval(code, {"__builtins__": {}}, ALLOWED_NAMES)

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if argv:
        expr = " ".join(argv)
        try:
            result = safe_eval(expr)
            print(result)
        except Exception as exc:
            print(f"Error: {exc}")
    else:
        print("Scientific Calculator. Type 'quit' or 'exit' to end.")
        while True:
            expr = input('>>> ')
            if expr.lower() in {"quit", "exit"}:
                break
            try:
                print(safe_eval(expr))
            except Exception as exc:
                print(f"Error: {exc}")

if __name__ == "__main__":
    main()
