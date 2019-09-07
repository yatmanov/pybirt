import argparse

import lxml.html

from pybirt import ParameterGroup


def main(birt_report) -> None:
    try:
        content = bytes(birt_report.read(), encoding='utf_8')
        xml = lxml.html.fromstring(content)
        root_group = ParameterGroup.build(xml)
    except Exception as exc:
        print(exc)
    else:
        print(root_group)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Show detailed information about report parameters')
    parser.add_argument(
        'file',
        metavar='BIRT report file',
        type=argparse.FileType(mode='r', encoding='utf_8')
    )
    args = parser.parse_args()

    main(args.file)
