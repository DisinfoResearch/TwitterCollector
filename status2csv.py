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

parser = argparse.ArgumentParser(description='Statuses to JSON', epilog='P.S. Trust The Plan')
parser.add_argument('--input', help='JSON File, else stdin', type=argparse.FileType('r', encoding='utf-8'), default=sys.stdin)
parser.add_argument('--out', help='JSON File, else stdout', type=argparse.FileType('w', encoding='utf-8'), default=sys.stdout)
args = parser.parse_args()

s = []
for line in args.input:
    e = json.loads(line)
    j = {'created_at':e['created_at'], \
         'id':e['id'], \
         'full_text':e['full_text'], \
         'source':e['source'], \
         'is_quote_status':e['is_quote_status'], \
         'retweet_count':e['retweet_count'], \
         'favorite_count':e['favorite_count'], \
         'lang':e['lang'], \
         'user_id':e['user']['id'], \
         'screen_name':e['user']['screen_name'], \
         'user_name':e['user']['name'], \
         'user_location':e['user']['location'], \
         'user_description':e['user']['description'], \
         'user_url':e['user']['url'], \
         'user_followers_count':e['user']['followers_count'], \
         'user_following_count':e['user']['friends_count'], \
         'user_created_at':e['user']['created_at'], \
         'user_favourites_count':e['user']['favourites_count'], \
         'user_status_count':e['user']['statuses_count'], \
         'user_verified':e['user']['verified'], \
         'user_protected':e['user']['protected']}
    s.append(j)

csv_writer = csv.writer(args.out)
csv_writer.writerow(s[0].keys())

for e in s:
    csv_writer.writerow(e.values())
