#!/usr/bin/python3
import importlib.util
if __name__ == "__main__":
    module_name = 'hidden_4'
    module_path = 'hidden_4.pyc'
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for name in dir(module):
        if name[:2] == "__":
            continue
        print(name)
