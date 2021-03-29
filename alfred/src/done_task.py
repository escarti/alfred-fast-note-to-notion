#!/usr/local/bin/python3

import argparse
import sys

from notion_api import notion_api

try:
    parser = argparse.ArgumentParser(description='Add task')
    parser.add_argument('--query', nargs=argparse.REMAINDER, help='query')
    args = parser.parse_args(sys.argv[1].split())

    query = ' '.join(args.query)

    print(notion_api.append_task_to_notes(query, True).title, query)
except Exception as e:
    # Print out nothing on STDOUT (missing value means means operation was unsuccessful)
    sys.stderr.write(e)