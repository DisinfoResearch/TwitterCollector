# Twitter Collector
Python scripts for the collection and transformations of datasets from Twitter

## Requirements

* [Redis](https://redis.io/)
* [redis-py](https://github.com/andymccurdy/redis-py)
* [twarc](https://github.com/DocNow/twarc)
* [Twitter Developer Access](https://developer.twitter.com/en/apply-for-access)

## Usage Notes

All JSON is expected to follow and be from twarc captures using *grabuser.sh*.

## Methodology with twarc and redis

For doing mass lookups and capture of an accounts [followers by Account ID](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids) and [following by Account ID](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids), the Account IDs only API can pull considerable more accounts within the call limits than the normal calls with account MetaData. This is also true for [lookup users](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) call, allowing large amounts of MetaData to be queried by Account ID. Temporarily caching these lookups can drastically increase speed and lower the amount of requests needed to the Twitter API. This allows the capture of accounts with followers and following in the millions with ease.

The *twarc* utility and python library handles and is designed to be used this way, as it is with a focus on Social Media Analysis, which makes it perfect for this application. The more common *tweepy* python library has a bug preventing pulling more than one frame from the Account ID based calls.

## List of Scripts

**fetchdata-justids.py** - Takes JSON list as input and fetches the IDs of followers/following, output to directory
**ids2json.py** - Converts directory of IDs to JSON, using Redis to cache looked up accounts
**dumpredis.py** - Dumps all the Twitter accounts from redis to *redis.json.xz*
**json2csv_user_directory.py** - Converts directory of JSON lists of accounts to csv format
**json2csv_user.py** - Convert a JSON list of accounts to CSV format.
**jsondiff.py** - Compares two JSON lists of accounts for differences, and displays them.
**jsonsame.py** - Compares two JSON lists of accounts, and displays entries that are the same.
**grabuser.sh** - Grabs the IDs and Metadata in JSON of an account's followers and following.

## Configuration
The Twitter API Keys is stored as standard JSON file with the following format.
```
{
	"Screen_Name":"XXX",
	"Consumer_Key":"XXX",
	"Consumer_Secret":"XXX",
	"Access_Token":"XXX",
	"Access_Secret":"XXX"
}
```
This should be in _~/.twitter_config_

## License
Copyright (C) 2021, Michigan State University.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.