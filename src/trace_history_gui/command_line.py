from argparse import ArgumentParser



description='Rohde & Schwarz Trace History Graphical User Interface'


def parse_args():
    parser = ArgumentParser(description=description)
    parser.add_argument('-d', '--demo', action='store_true', help='Run in demo mode')
    return parser.parse_args()
