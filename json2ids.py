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

def extract_user_id(input, output):
    # extract the data object from the output. This will hold the list of user objects we need
    data = json.loads(input.readline()).get('data')

    for line in data:
        # extract id
        user_id = line.get('id')
        output.write('{}\n'.format(user_id))


parser = argparse.ArgumentParser(description='Extract the user IDs from following/followers output', epilog='P.S. Trust The Plan')
parser.add_argument('--input', help='JSONL File, or stdin if not specified', type=argparse.FileType('r', encoding='utf-8'), default=sys.stdin)
parser.add_argument('--output', help='Any file, or stdout if not specified', type=argparse.FileType('w', encoding='utf-8'), default=sys.stdout)
args = parser.parse_args()

extract_user_id(args.input, args.output)