import sys
from mypy import build
from mypy.main import process_options

def get_ast():
    sources, options = process_options(sys.argv[1:])
    res = build.build(sources, options)
    for module_name, f in res.files.items():
        if f.path == sys.argv[1]:
            print(str(f))
            return

    print('Module not found after analysis.')

if __name__ == '__main__':
    get_ast()
