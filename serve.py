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
	
	rootPath = '.'
	for i, arg in enumerate(sys.argv):
		if arg == '-p':
			rootPath = sys.argv[i + 1]
			break

	print('Serving files from', rootPath)
	
	app.run(debug=False)
