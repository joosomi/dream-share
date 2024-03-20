from user import user_service
from flask import Flask, jsonify ,request, render_template

app = Flask(__name__)

# ========================= user controller =========================

# 회원가입
@app.route('/user/sign-up', methods=['POST'])
def api_register():
    user = dict()
    params = request.get_json()
    user['id_receive'] = params['id_give']
    user['pw_receive'] = params['pw_give']
    user['username_receive'] = params['username']

    result = user_service.sign_up(user)

    if result is True:
        return jsonify({'result': 'success', 'msg': '회원가입이 완료되었습니다.'})
    else:
        return jsonify({'result': 'fail'})

@app.route('/user/username/validate', methods=['GET'])
def validate_username():
    username= request.args.get('username')

    result = user_service.validateUsername(username)

    if result is True:
        return jsonify({'result': 'success', 'msg': '사용할 수 있는 닉네임입니다.'})
    else:
        return jsonify({'result': 'fail', 'msg': '이미 존재하는 닉네임입니다!'})


@app.route('/user/userid/validate', methods=['GET'])
def validate_userid():
    user_id= request.args.get('user_id')
    
    result = user_service.validateUserId(user_id)

    if result is True:
        return jsonify({'result': 'success', 'msg': '사용할 수 있는 아이디입니다.'})
    else:
        return jsonify({'result': 'fail', 'msg': '이미 존재하는 아이디입니다.'})


# 로그인
@app.route('/user/login', methods=['POST'])
def login():
    user = dict()
    params = request.get_json()
    user['id_receive'] = params['id_give']
    user['pw_receive'] = params['pw_give']

    token = user_service.login(user)

    if token is False:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})
    else : return jsonify({'result': 'success', 'token': token})


@app.route('/login')
def login_page():
    return render_template('testlogin.html')

@app.route('/sign-up')
def sign_up_page():
    return render_template('testsignup.html')

if __name__ == '__main__':  
    app.run('0.0.0.0',port=5001,debug=True)