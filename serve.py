import sys
import os
import time
import threading
import webbrowser 
from flask import Flask, redirect, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/index.html')

@app.route('/<path:filename>')
def serve_file(filename):
	return send_from_directory(rootPath, filename)

def open_browser_with_delay():
	time.sleep(1)
	webbrowser.open('http://localhost:5000')

if __name__ == '__main__':
	global rootPath

	rootPath = os.getcwd()
	for i, arg in enumerate(sys.argv):
		if arg == '-p':
			rootPath = os.path.join(rootPath, sys.argv[i + 1])
			break
	
	threading.Thread(target=open_browser_with_delay).start()
	app.run(debug=False)
