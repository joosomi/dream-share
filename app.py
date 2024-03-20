from user import user_service
from board import board_service
from security import security_service
from reservation import reservation_service
from flask import Flask, jsonify ,request, render_template, redirect, url_for
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def render_home():
    return render_template('index.html')


@app.route('/user/login')
def render_login():
    #쿠키에서 저장된 토큰 받아오기 
    receive_token = request.cookies.get('access-token') 
    #토큰 유효성 검사 
    given_token = security_service.validateToken(receive_token)
    print(given_token)
    if given_token["result"]:
        return jsonify({'result':  given_token['data'] })
    else:
        return redirect(url_for('render_home'))

@app.route('/user/sign-up')
def render_signup():
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


#토큰 유효성 확인 - 수정 필요 미완성
@app.route('/user/validate', methods=["GET"])
def validate_token():
    #쿠키에서 저장된 토큰 받아오기 
    receive_token = request.cookies.get('access-token') 
    #토큰 유효성 검사 
    given_token = security_service.validateToken(receive_token)
    print(given_token)
    if given_token["result"]:
        return jsonify({'result':  given_token['data'] })
    else:
        return jsonify({'result': given_token['msg']})



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
def api_write_post_page():
    receive_token = request.cookies.get('access-token')
    owner = security_service.getIdWithValidation(receive_token)

    post_receive = dict()
    params = request.get_json()

    post_receive['owner_id'] = owner['id']
    post_receive['category'] = params['category']
    post_receive['content'] = params['content']
    post_receive['location'] = params['location']
    post_receive['status'] = params['status']

    result = board_service.write_a_post(post_receive)

    if result is True:
        return jsonify({'result': 'success', 'msg': '게시글 작성이 완료되었습니다.'})
    else:
        return jsonify({'result': 'fail', 'msg': '다시 시도해주세요.'})

#게시글 수정 - status update 
@app.route('/board/update_status', methods=['POST'])
def api_update_post_status():
    receive_token = request.cookies.get('access-token') 
    token_validation_result = security_service.validateToken(receive_token)

    # 유효하지 않은 토큰인 경우 처리
    if not token_validation_result["result"]:
        return jsonify({"result": "fail", "msg": token_validation_result["msg"] })

    # 유효한 토큰인 경우 사용자 ID 가져오기
    current_user_id = token_validation_result['data']
    print(current_user_id)
    return current_user_id
    # post["post_id"] = post["post_id"]
    # post["status"]= post["status"]
    

    # result = board_service.edit_a_post(post)


#게시글 삭제 - 거래 완료 버튼 누르는 경우
@app.route('/board/delete', methods=["POST"])
def api_delete_post():
    post = request.get_json()
    post_id = post["post_id"]

    result = board_service.delete_a_post(post_id)
    
    if result is True:
        return jsonify({'result': 'success', 'msg': '게시글 삭제가 완료되었습니다.'})
    else:
        return jsonify({'result': 'fail', 'msg': '다시 시도해주세요.'})
    


# ========================= reservation controller =========================

#예약 신청(테스트 X)
@app.route('/reservation/write', methods=['POST'])
def api_write_a_resv():
    receive_token = request.cookies.get('access-token')
    user = security_service.getIdWithValidation(receive_token)
    post_id= request.args.get('id')
    
    resv_receive = dict()
    params = request.get_json()

    resv_receive['user_id'] = user['id']
    resv_receive['post_id'] = post_id
    resv_receive['contact-information'] = params['contect_infomation']
    resv_receive['status'] = 0

    result = reservation_service.write_a_resv(resv_receive)

    if result is True:
        board_service.change_status_to_1(post_id)
        return jsonify({'result': 'success', 'msg': '예약신청이 완료되었습니다.'})
    else:
        return jsonify({'result': 'fail', 'msg': '다시 시도해주세요.'})
    
@app.route('/reservation', methods=['GET'])
def api_get_reservations():
    post_id= request.args.get('id')
    
    result = reservation_service.get_reservation_list(post_id)

    if result:
        return jsonify({'msg': 'success', 'data': result})
    else:
        return jsonify({'msg': '예약정보를 불러올 수 없습니다.'})

if __name__ == '__main__':  
    app.run('0.0.0.0',port=5001,debug=True)
