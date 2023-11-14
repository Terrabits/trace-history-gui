from argparse import ArgumentParser


def parse_args():
    # init parser
    parser = ArgumentParser(
        prog        = 'trace-history-gui',
        description = 'Rohde & Schwarz Trace History Graphical User Interface'
    )

    # define args
    parser.add_argument('-d', '--demo',     action='store_true', help='Run in demo mode')
    parser.add_argument('-i', '--interact', action='store_true', help='Enter REPL for debugging after application has exited')

    # parse
    return parser.parse_args()
