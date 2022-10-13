#!/bin/bash
thedate=$(date '+%m%d%Y')
twarc2 following $1 > output/$1-$thedate-following.jsonl
python json2ids.py --input output/$1-$thedate-following.jsonl --output output/$1-$thedate-following.ids 
twarc2 followers $1 > output/$1-$thedate-followers.jsonl
python json2ids.py --input output/$1-$thedate-followers.jsonl --output output/$1-$thedate-followers.ids 
twarc2 users output/$1-$thedate-following.ids > $1-$thedate-following.json
twarc2 users output/$1-$thedate-followers.ids > $1-$thedate-followers.json