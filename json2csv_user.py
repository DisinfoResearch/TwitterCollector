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

import json
import csv
import argparse
import sys

def douser(u):
    return {'id':u['id'], 'screen_name':u['screen_name'], 'statuses_count':u['statuses_count'], 'description':u['description'], 'url':u['url'], 'verified':u['verified'], 'favourites_count':u['favourites_count'], 'followers_count':u['followers_count'], 'friends_count':u['friends_count'], 'name':u['name'], 'location':u['location'], 'protected':u['protected'], 'created_at':u['created_at'], 'verified':u['verified']}


def process(inp, out):
    csv_writer = csv.writer(out)
    t = douser(json.loads(inp.readline()))

    csv_writer.writerow(t.keys())
    csv_writer.writerow(t.values())

    for line in inp:
        t = douser(json.loads(line))
        csv_writer.writerow(t.values())

parser = argparse.ArgumentParser(description='Convert JSON to CSV', epilog='P.S. Trust The Plan')
parser.add_argument('input', help='JSON File, or stdin if not specified', type=argparse.FileType('r', encoding='utf-8'), default=sys.stdin)
parser.add_argument('output', help='CSV File, or stdout if not specified', type=argparse.FileType('w', encoding='utf-8'), default=sys.stdout)
args = parser.parse_args()

process(args.input, args.output)