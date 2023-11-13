from argparse import ArgumentParser


description='Rohde & Schwarz Trace History Graphical User Interface'


def parse_args():
    parser = ArgumentParser(description=description)
    parser.add_argument('-d', '--demo',     action='store_true', help='Run in demo mode')
    parser.add_argument('-i', '--interact', action='store_true', help='Enter REPL for debugging after application has exited')
    return parser.parse_args()
