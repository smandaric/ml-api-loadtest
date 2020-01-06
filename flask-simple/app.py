from flask import Flask
import time

app = Flask(__name__)

# 1 sec
@app.route('/cpu')
def hello_world_cpu_bound():
    a = 2
    for i in range (30000000):
        a += 500
    return 'Hello, World!'

# 1 sec
@app.route('/sleep')
def hello_world_io_bound():
    time.sleep(1)
    return 'Hello, World!'


# By default flask runs threaded
# Threaded may perform worse due to GIL
if __name__ == "__main__":
    app.run(threaded=False)