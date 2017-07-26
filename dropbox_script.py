__author__ = 'raviteja'


from dropbox import client, rest, session

APP_KEY = 'uj4v8hqnpm3qdsb' #u need to change to your's
APP_SECRET = 'oh7543hw9mqgkzi' #u need to change to your's
ACCESS_TYPE = 'dropbox'
TOKENS = 'dropbox_token.txt'

sess = session.DropboxSession(APP_KEY,APP_SECRET, ACCESS_TYPE )

request_token = sess.obtain_request_token()

# Make the user sign in and authorize this token
url = sess.build_authorize_url(request_token)
print "url:", url
print "Please authorize in the browser. After you're done, press enter."
raw_input()

# This will fail if the user didn't visit the above URL and hit 'Allow'
access_token = sess.obtain_access_token(request_token)
TOKENS = 'dropbox_token.txt'
token_file = open(TOKENS,'w')
token_file.write("%s|%s" % (access_token.key,access_token.secret) )
token_file.close()
token_file = open(TOKENS)
token_key,token_secret = token_file.read().split('|')
token_file.close()
sess.set_token(token_key,token_secret)
client = client.DropboxClient(sess)
#stored_creds = open(CONF_DIR + self.TOKEN_FILE).read()
uploading of a file
f = open('today.txt')
response = client.put_file('/magnum_opus.txt', f)
#listing of the files
folder_metadata = client.metadata('/')

#downloading the files
f, metadata = client.get_file_and_metadata('/magnum_opus.txt')
out = open('magnum_opus.txt', 'wb')
out.write(f.read())
out.close()

