import sys
print(sys.version)
#from flask import Flask, jsonify, render_template, request
def application(environ, start_response):
    status = '200 OK'
    output = b'Hello Udacity!'

    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
