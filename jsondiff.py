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

parser = argparse.ArgumentParser(description='Difference between two JSON lists of Twitter Accounts', epilog='P.S. Trust The Plan')
parser.add_argument('input1', help='JSON File', type=argparse.FileType('r', encoding='utf-8'))
parser.add_argument('input2', help='JSON File', type=argparse.FileType('r', encoding='utf-8'))
args = parser.parse_args()

accs1 = []
for line in args.input1:
    j = json.loads(line)
    accs1.append(j['id'])

for line in args.input2:
    j = json.loads(line)
    if j['id'] not in accs1:
        print(j['screen_name'])
