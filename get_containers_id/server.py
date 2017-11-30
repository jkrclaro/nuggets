import json
from subprocess import Popen, PIPE

from flask import Flask, Response, request

app = Flask(__name__)

def docker(*args):
    cmd = ['docker']
    for sub in args:
        cmd.append(sub)
    process = Popen(cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    if stderr.startswith('Error'):
        print 'Error: {0} -> {1}'.format(' '.join(cmd), stderr)
    return stderr + stdout


def docker_ps_to_array(output):
    all = []
    for c in [line.split() for line in output.splitlines()[1:]]:
        each = {}
        each['id'] = c[0]
        each['image'] = c[1]
        each['name'] = c[-1]
        each['ports'] = c[-2]
        all.append(each)
    return all

@app.route('/containers/<container_id>', methods=['GET'])
def containers(container_id=None):
    output = docker('inspect', container_id)
    resp = json.dumps(json.loads(output))
    return Response(response=resp, mimetype="application/json")

app.run(port=8080, debug=True)