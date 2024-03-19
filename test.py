from user import user_service, user_repository

def usernameValidateTest():
    result1 = user_service.validateUsername("test_name")
    result2 = user_service.validateUsername("validate_name")
    if result1 is False:
        print("중복케이스 성공")
    else:
        print("중복케이스 실패ㅜ")

    if result2 is True:
        print("비 중복케이스 성공")
    else:
        print("비 중복케이스 실패ㅜ")


def loginTest():
    id = "test_id"
    pw = "testpassword123!"
    login_form = dict()
    login_form["id_receive"] = id
    login_form["pw_receive"] = pw
    user_service.login()
    if result1 is False:
        print("중복케이스 성공")
    else:
        print("중복케이스 실패ㅜ")

    if result2 is True:
        print("비 중복케이스 성공")
    else:
        print("비 중복케이스 실패ㅜ")
usernameValidateTest()