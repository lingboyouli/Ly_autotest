import string

# 方法1
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits

lowercase_flag = False
uppercase_flag = False
digits_flag = False

while True:
    pwd1 = input('请输入密码')
    if pwd1 == '':
        print('密码不可为空')
        break
    else:
        for word in pwd1:
            if word in lowercase:
                lowercase_flag = True
            elif word in uppercase:
                uppercase_flag = True
            elif word in digits:
                digits_flag = True

    if lowercase_flag == True and uppercase_flag == True and digits_flag == True and len(pwd1) > 10:
        pwd2 = input('请再次输入密码')
        if pwd1 != pwd2:
            print('密码更新失败')
            exit()
        else:
            print('密码更新成功')
            exit()
    elif lowercase_flag == False:
        print('密码缺少小写字母')
    elif uppercase_flag == False:
        print('密码缺少大写字母')
    elif digits_flag == False:
        print('密码缺少数字')
    elif len(pwd1) < 10:
        print('密码长度需大于10')


# 方法2
dict={'小写字母' : False,'大写字母' : False,'数字' : False}

while True:
    pwd1 = input('请输入密码')
    if pwd1 == '':
        print('密码不可为空')
        break
    else:
        for word in pwd1:
            if word.islower():
                dict['小写字母'] = True
            elif word.isupper():
                dict['大写字母'] = True
            elif word.isdigit():
                dict['数字'] = True

    dict_false={key for key in dict.keys() if dict[key] == False}
    if len(dict_false) == 0 and len(pwd1) > 10:
        pwd2 = input('请再次输入密码')
        if pwd1 != pwd2:
            print('两次密码输入不一致，密码更新失败')
            exit()
        else:
            print('密码更新成功')
            exit()
    elif len(pwd1) < 10:
        print('密码长度需大于10')
    else:
        print(f'密码缺少{dict_false}')