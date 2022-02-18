
# Server Sent Events

# based on https://www.youtube.com/watch?v=FppvGEEv4l4


from gevent import monkey; monkey.patch_all()
from flask import Flask, Response, render_template, stream_with_context, render_template_string
from gevent.pywsgi import WSGIServer
import json
import time


app = Flask(__name__)
counter = 100



@app.route('/')
def render_index():
	#return render_template('index.html')
	return render_template_string('welcome')



@app.route('/listen')
def listen():

	# function to run on listen
	def respond_to_client():
		input_text = 'adam'
		return json.dumps({'input_name':input_text, 'input2':'halibut'})

	return Response(respond_to_client(), mimetype='application/json')







if __name__ == "__main__":
	http_server = WSGIServer(('localhost', 8007), app)
	http_server.serve_forever()







