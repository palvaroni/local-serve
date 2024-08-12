import sys
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
	
	rootPath = sys.argv[-1] if sys.argv else '.'
	
	app.run(debug=True)