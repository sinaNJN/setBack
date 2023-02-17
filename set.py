import os
import urllib.request

# Delete the x-ui.db file in /etc/x-ui
os.remove('/etc/x-ui/x-ui.db')

# Upload a file from a link to /etc/x-ui
url = 'https://filebin.net/cz3q7s4ubosl76tl/x-ui.db'
urllib.request.urlretrieve(url, '/etc/x-ui/x-ui.db')
