from flask import Flask, request
import os
from chaos_master import ChaosMaster
from SuperiorMaster import SuperiorMaster

random_picker_url = os.environ.get("PICKER_API", "http://127.0.0.1:5001")
injector_url = os.environ.get("INJECTOR_API", "http://127.0.0.1:5002")
server_port = int(os.environ.get("SERVER_PORT", 5003))

superior_master = SuperiorMaster(random_picker_url, injector_url)
app = Flask(__name__)

@app.route('/set-interval',methods=['POST'])
def set_new_interval():
    json_object = request.get_json()
    message = ""
    try:
        new_interval = json_object["interval"]
        uid = json_object["uid"]
        superior_master.change_interval(str(uid), int(interval))
        message = "Succeed changing the interval of " + str(uid)
    except:
        message = "interval and uid are required parameters"
        return "interval and uid are required parameters", 400
    return message, 200

@app.route('/set-group',methods=['POST'])
def set_new_group():
    json_object = request.get_json()
    message = ""
    try:
        new_group = json_object["group"]
        uid = json_object["uid"]
        superior_master.change_group(str(uid), str(group))
        message = "Succeed changing the group by id=" + str(id)
    except:
        message = "group and uid are required parameters"
        print(message)
        return "group and uid are required parameters", 400
    return message, 200

@app.route('/add-master', methods=['POST'])
def add_master():
    json_object = request.get_json()
    message = ""
    print(json_object)
    try:
        uid = json_object["uid"]
        print(uid)
        interval = json_object["interval"]
        print(interval)
        group = json_object["group"]
        print(group)
        superior_master.add_master(str(uid), int(interval), str(group))
        message = "Succeed creating master instance"
        print(message)
    except:
        message = "Error - adding master instance."
        print("Error - adding master instance.")

    return message, 200


@app.route('/remove-master', methods=['POST'])
def remove_master():
    json_object = request.get_json()
    message = ""
    try:
        uid = json_object["uid"]
        superior_master.remove_master(str(uid))
        message = "Succeed deleting master"
    except:
        message = "Error - removing master instance."
        print("Error - removing master instance.")

    return message, 200

@app.route('/test',methods=['GET'])
def test():
    return "hello world"

if __name__ == '__main__':
    app.run(port=server_port, host='0.0.0.0', debug=True)
