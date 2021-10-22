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
import argparse
import sys
import os
import json
from datetime import date
from twarc import Twarc

with open(os.path.expanduser('~/.twitter_config'), 'r') as f:
	keys = json.load(f)

twarc = Twarc(keys['Consumer_Key'], keys['Consumer_Secret'], keys['Access_Token'], keys['Access_Secret'])

def process(fin, out):
    ids = []
    for line in fin:
        j = json.loads(line)
        if j['protected'] == False:
            ids.append(j)
    for a in ids:
        if a['protected'] != True:
            print(f"Processing -> {a['screen_name']}")
            timestr = date.today().strftime('%m%d%Y')
            following_ids = []
            follower_ids = []
            for a1 in twarc.friend_ids(a['id']):
                following_ids.append(a1)
            for a2 in twarc.follower_ids(a['id']):
                follower_ids.append(a2)
            with open(f"{out}/{a['screen_name']}-{timestr}-following.ids", 'w', encoding='utf-8') as f:
                for u in following_ids:
                    f.write(str(u)+"\n")
            with open(f"{out}/{a['screen_name']}-{timestr}-followers.ids", 'w', encoding='utf-8') as f:
                for u in follower_ids:
                    f.write(str(u)+"\n")

parser = argparse.ArgumentParser(description='Fetch user data for list of users', epilog='P.S. Trust The Plan')
parser.add_argument('file', help='List user ids to fetch followers & following, or stdin if not specified', type=argparse.FileType('r', encoding='utf-8'), default=sys.stdin)
parser.add_argument('out', help='Path to directory', type=str, default="")
args = parser.parse_args()

process(args.file, args.out)
