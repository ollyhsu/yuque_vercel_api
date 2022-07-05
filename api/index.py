# -*- coding: UTF-8 -*-
import requests
import os
from http.server import BaseHTTPRequestHandler

def githubCI(token,user,source):
    requests_path = 'https://api.github.com/repos/' + user + '/' + source + '/dispatches'
    token = 'token '+token
    r = requests.post(requests_path,
    json = {"event_type": "run-it"},
    headers = {"User-Agent":'curl/7.52.1',
              'Content-Type': 'application/json',
              'Accept': 'application/vnd.github.everest-preview+json',
              'Authorization': token})
    if r.status_code == 204:
        return "This's OK!"
    else:
        return r.status_code

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        token = os.environ.get('GITHUB_TOKEN')
        user = os.environ.get('GITHUB_USER')
        source = os.environ.get('GITHUB_SOURCE')
        text = githubCI(token,user,source)
        text = str(text)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(text.encode())
        return
    def do_GET(self):
        token = os.environ.get('GITHUB_TOKEN')
        user = os.environ.get('GITHUB_USER')
        source = os.environ.get('GITHUB_SOURCE')
        text = githubCI(token,user,source)
        text = str(text)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(text.encode())
        return
