from flask import Flask, request, jsonify
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/id', methods=['POST'])
@cross_origin()
def get_id():
    req_data = request.get_json()

    area = req_data.get("area")
    birthday = req_data.get("birthday")
    birthday = birthday.replace('-', '')
    sex = req_data.get("sex")
    if sex == "male":
        sex = "1"
    else:
        sex = "2"

    id_ = area + birthday + "05" + sex
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    sum_ = 0
    for i in range(len(id_)):
        sum_ += int(id_[i]) * weight[i]
    check_code = sum_ % 11
    dict_ = {0: "1", 1: "0", 2: "X", 3: "9", 4: "8", 5: "7", 6: "6", 7: "5", 8: "4", 9: "3", 10: "2"}
    id_ += dict_[check_code]
    res = jsonify(id=id_)
    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0")
