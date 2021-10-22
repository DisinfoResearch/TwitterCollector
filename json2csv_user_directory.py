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
import glob

def douser(u):
    return {'id':u['id'], 'screen_name':u['screen_name'], 'statuses_count':u['statuses_count'], 'description':u['description'], 'url':u['url'], 'verified':u['verified'], 'favourites_count':u['favourites_count'], 'followers_count':u['followers_count'], 'friends_count':u['friends_count'], 'name':u['name'], 'location':u['location'], 'protected':u['protected'], 'created_at':u['created_at'], 'verified':u['verified']}


def process(inp, out):
    csv_writer = csv.writer(out)
    l = inp.readline()
    if len(l) <= 0:
        return
    t = douser(json.loads(l))

    csv_writer.writerow(t.keys())
    csv_writer.writerow(t.values())

    for line in inp:
        t = douser(json.loads(line))
        csv_writer.writerow(t.values())

parser = argparse.ArgumentParser(description='Convert JSON to pretty CSV', epilog='P.S. Trust The Plan')
parser.add_argument('out', help='Path to directory', type=str, default="")
args = parser.parse_args()

for e in glob.glob(f"{args.out}/*.json"):
    with open(e, 'r', encoding='UTF-8') as fin, open(e.replace('json', 'csv'), 'w', encoding='UTF-8') as fou:
        print(f"PROCESSING -> {e}")
        process(fin, fou)
