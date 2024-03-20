from user import user_service
from board import board_service
from flask import Flask, jsonify ,request, render_template


app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('testlogin.html')

@app.route('/sign-up')
def sign_up_page():
    return render_template('testsignup.html')


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
        return jsonify({'result': 'fail', 'msg': '중복을 확인해 주세요.'})

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



# ========================= board controller =========================
#전체 게시글 가져오기 
@app.route('/board', methods=['GET'])
def api_get_posts():
    result = board_service.get_all_posts()

    if result:
        return jsonify({'msg': 'success', 'data': result})
    else:
        return jsonify({'msg': '게시글이 존재하지 않습니다.'})

#특정 게시글 가져오기 
@app.route('/article', methods=['GET'])
def api_get_a_post():
    post_id= request.args.get('id')
    
    result = board_service.get_a_post(post_id)

    if result:
        return jsonify({'result': 'success', 'data': result})
    else:
        return jsonify({'result': 'fail', 'msg': '해당 게시글이 존재하지 않습니다. '})


#게시글 등록
@app.route('/board/write', methods=['POST'])
def api_write_post():
    post_receive = dict()
    params = request.get_json()

    post_receive['owner_id'] = params['owner_id']
    post_receive['category'] = params['category']
    post_receive['content'] = params['content']
    post_receive['location'] = params['location']
    post_receive['status'] = params['location']
    post_receive['user_id'] = params['user_id']


    result = board_service.write_a_post(post_receive)

    if result is True:
        return jsonify({'result': 'success', 'msg': '게시글 작성이 완료되었습니다.'})
    else:
        return jsonify({'result': 'fail', 'msg': '다시 시도해주세요.'})

#게시글 수정


#게시글 삭제


if __name__ == '__main__':  
    app.run('0.0.0.0',port=5001,debug=True)
