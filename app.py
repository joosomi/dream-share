from user import user_service
from flask import Flask, jsonify ,request

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
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    login_form = dict()
    login_form['id_receive'] = request.form['id_give']
    login_form['pw_receive'] = request.form['pw_give']

    user_service.login(login_form)

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰 생성
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/')
def home():
   return 'This is Home!'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)