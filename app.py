# flask libs for api functionality
from flask import Flask, jsonify, request
# used to connect to Twitter APIv2
from twarc import Twarc2, ensure_flattened
# to read token for api
import os, json
# can't be too safe :-p
from markupsafe import escape

# create app
app = Flask(__name__)
# load config keys
with open(os.path.expanduser('~/.twitter_config'), 'r') as f:
        keys = json.load(f)
# instantiate twarc2 instance
twarc = Twarc2(bearer_token=keys['Bearer_Token'])

@app.route('/theconsole/<username>', methods=['GET'])
def following_user_ids(username):
    """This endpoints main purpose is to mimic the grabuser script. """
    # find userid of the username
    user_id = get_user_id(username, True).get('id')
    
    account_ids = []
    # iterate over pages of accounts the user followers
    for i, follower_page in enumerate(twarc.followers(user_id, user_fields=['id'])):
        for follower in ensure_flattened(follower_page.get('data')):
            account_ids.append(follower.get('id'))
        # stop for one page for testing
        break
    
    # iterate over pages of accounts the users is following
    for i, following_page in enumerate(twarc.following(user_id, user_fields=['id'])):
        for following in ensure_flattened(following_page.get('data')):
            account_ids.append(following.get('id'))
        # stop for one page for testing
        break


    users = []
    # lookup users accounts
    for i, user_page in enumerate(twarc.user_lookup(account_ids)):
        for user in ensure_flattened(user_page.get('data')):
            users.append(user)
        # stop for one page for testing
        break

    return users
        
    

def get_user_id(username, is_username):
    """ Helper function to find the user_id of the username """
    for i, user_page in enumerate(twarc.user_lookup({username}, usernames=is_username)):
        return ensure_flattened(user_page.get('data'))[0]

# driver function
if __name__ == '__main__':
    app.run(debug=True)