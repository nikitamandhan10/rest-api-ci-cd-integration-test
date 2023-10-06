from flask import Flask, Response
import mysql.connector

app = Flask(__name__)
print('Initializing app')

@app.route('/healthz', methods=['GET'])
def check_db_connection():
    print("Inside  get request")
    try:
        con = mysql.connector.connect(host='localhost', user= 'root', password = 'root')
        return create_response(status=200)
    except Exception as e:
        print("Exception: ", e)
        return create_response(status=503)

@app.route('/healthz', methods=['PUT', 'DELETE', 'PATCH', 'POST'])
def other_methods():
    return create_response(status=405)

def create_response(status):
    response = Response(status=status)
    response.headers['Cache-control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
    print('Running on port 8080')