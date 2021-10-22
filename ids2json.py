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
import glob
import redis
import requests
from datetime import date
from twarc import Twarc

with open(os.path.expanduser('~/.twitter_config'), 'r') as f:
	keys = json.load(f)

twarc = Twarc(keys['Consumer_Key'], keys['Consumer_Secret'], keys['Access_Token'], keys['Access_Secret'])

r = redis.Redis()

def fetchncheck(ids):
    toget = []
    for i in ids:
        if r.exists(f"TWITUSER{i}") == 0:
            toget.append(i)
    try: # Sometimes all these user ids can be suspended / deactivated or protected, causing 404/403 exception throws
        for i in twarc.user_lookup(toget, id_type='user_id'):
            r.set(f"TWITUSER{i['id_str']}", json.dumps(i), 28800) # 8 hours = 28800
    except requests.exceptions.HTTPError:
        pass

def pullfromredis(ids):
    ret = []
    for i in ids:
        u = r.get(f"TWITUSER{i}")
        if u != None:
            ret.append(u.decode('utf-8'))
    return ret

parser = argparse.ArgumentParser(description='Convert IDs to JSON', epilog='P.S. Trust The Plan')
parser.add_argument('out', help='Path to directory', type=str, default="")
args = parser.parse_args()

for e in glob.glob(f"{args.out}/*.ids"):
    jfile = e.replace('ids', 'json')
    if os.path.exists(jfile) == False:
        print(f"PROCESSING -> {e}")
        with open(e, 'r', encoding='utf-8') as fin, open(jfile, 'w', encoding='utf-8') as fou:
            ids = []
            for line in fin:
                ids.append(line.strip())
            fetchncheck(ids)
            for u in pullfromredis(ids):
                fou.write(f"{u}\n")
