# Copyright 2015, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of the
# License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable
# law or agreed to in writing, software distributed under the License is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and
# limitations under the License.


from flask import Flask
import requests

app = Flask(__name__)

from api_key import key

# [START app]
@app.route('/get_author/<title>')
def get_author(title):
    url = 'https://www.googleapis.com/books/v1/volumes?q={}&key={}&country=US'.format(title, key)
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    json_resp = response.json()
    authors = json_resp['items'][0]['volumeInfo'].get('authors')
    if authors:
        return authors[0]
    else:
        return 'Not found'
# [END app]

if __name__ == '__main__':
    app.run(debug=True)
