#!/bin/python3

# Copyright (C) 2021, Michigan State University.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import csv
import json
import argparse
import sys
import datetime
from dateutil.parser import parse

def calc_row(u):
    created_date = parse(u['created_at'])
    t = today - created_date.date()

    # Prevent divide by zero
    ff_ratio = 0
    if int(u['friends_count']) != 0: ff_ratio = int(u['followers_count'])/int(u['friends_count'])

    # Force conversions to int, as you never know with Twitter
    return {'Twitter_ID':u['id'], 'Handle':u['screen_name'], 'Followed':u['friends_count'], 'Followers':u['followers_count'], 'Followers/Followed':ff_ratio, 'Tweets':u['statuses_count'], 'Days_old':int(t.days), 'Tweets/Days_old':int(u['statuses_count'])/int(t.days), 'Followers/Days_old':int(u['followers_count'])/int(t.days)}

def process_csv(inp, out):
    # Uses a Tuple to ensure a specific column order
    csv_writer = csv.DictWriter(out, fieldnames=('Twitter_ID', 'Handle', 'Followed', 'Followers', 'Followers/Followed', 'Tweets', 'Days_old', 'Tweets/Days_old', 'Followers/Days_old'))

    csv_writer.writeheader()

    for line in inp:
        csv_writer.writerow(calc_row(json.loads(line)))

def process_json(inp, out):
    for line in inp:
        j = json.loads(line)
        out.write(json.dumps(calc_row(j))+"\n")

parser = argparse.ArgumentParser(description='Convert JSON to CSV', epilog='P.S. Trust The Plan')
parser.add_argument('--format', help='either JSON or CSV', required=True)
parser.add_argument('input', help='JSON File, or stdin if not specified', type=argparse.FileType('r', encoding='utf-8'), default=sys.stdin)
parser.add_argument('output', help='output to File, or stdout if not specified', type=argparse.FileType('w', encoding='utf-8'), default=sys.stdout)
args = parser.parse_args()

today = datetime.date.today()

if args.format.upper() == 'CSV':
    process_csv(args.input, args.output)
elif args.format.upper() == 'JSON':
    process_json(args.input, args.output)
else:
    print(f"Error: '{args.format}' is an invalid format, must be CSV or JSON.", end="\n\n")
    parser.print_help()
    exit(-1)