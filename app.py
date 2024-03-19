from user import user_service
from flask import Flask, jsonify ,request

app = Flask(__name__)

# ========================= user controller =========================

# 회원가입
@app.route('/user/sign-up', methods=['POST'])
def api_register():
    user = dict()
    user['id_receive'] = request.form['id_give']
    user['pw_receive'] = request.form['pw_give']
    user['username_receive'] = request.form['username']

    result = user_service.sign_up(user)

    if result is True:
        return jsonify({'result': 'success', 'msg': '회원가입이 완료되었습니다.'})
    else:
        return jsonify({'result': 'fail'})

@app.route('/user/username/validate', methods=['GET'])
def api_register():
    username= request.form['username']

    result = user_service.validateUsername(username)

    if result is True:
        return jsonify({'result': 'success', 'msg': '사용할 수 있는 닉네임입니다.'})
    else:
        return jsonify({'result': 'fail', 'msg': '이미 존재하는 닉네임입니다!'})

@app.route('/')
def home():
   return 'This is Home!'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)