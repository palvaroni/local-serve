import sys
import os
from flask import Flask, redirect, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/index.html')

@app.route('/<path:filename>')
def serve_file(filename):
	return send_from_directory(rootPath, filename)

if __name__ == '__main__':
	global rootPath

	rootPath = os.getcwd()
	for i, arg in enumerate(sys.argv):
		if arg == '-p':
			rootPath = os.path.join(rootPath, sys.argv[i + 1])
			break
	
	app.run(debug=False)
