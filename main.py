import os
import sys

from handler import XMLProcessor, JSONProcessor, BaseProcessor


def print_result(filepath, handler: BaseProcessor):
    if handler.isValid():
        print(">> Valid Transaction in " + filepath + "\n")
    else:
        print(">> NOT Valid Transaction in " + filepath + "\n")


if __name__ == '__main__':

    filepath = sys.argv[1] if len(sys.argv) > 1 else None
    if not filepath or not os.path.exists(filepath):
        try:
            raise ValueError
        except ValueError:
            print('\n>> >> Please provide transaction file  as argument << <<')
        exit()

    if filepath.endswith('xml'):
        handler = XMLProcessor(filepath)
        handler.processXML()
        print_result(filepath, handler)
    elif filepath.endswith('json'):
        handler = JSONProcessor(filepath)
        handler.processJSON()
        print_result(filepath, handler)
    else:
        try:
            raise ValueError
        except ValueError:
            print('\n>> >> Not Support to handle ' + filepath + " << <<")
        exit()
