#!/bin/bash
thedate=$(date '+%m%d%Y')
twarc friends $1 > $1-$thedate-following.ids
twarc followers $1 > $1-$thedate-followers.ids
twarc users $1-$thedate-following.ids > $1-$thedate-following.json
twarc users $1-$thedate-followers.ids > $1-$thedate-followers.json
