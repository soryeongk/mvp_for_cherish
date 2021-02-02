import random


'''
text = 동전 str(i)
i는 10, 50, 100, 500
'''


def vm(text):
    if '동전 100' == text:
        reply = '100원을 넣었습니다.'
    elif '잔액' == text:
        reply = '잔액은 0원입니다.'
    else:
        reply = None
    return reply


def answer(text):
    if "소령" in text:
        reply = "넴"
    # elif 'UBDCWMFND' in text:
    #     reply = "이제부터 @ahlum cho님을 따라다녀요 :dait_happy:"
    # elif 'UBDN90RJQ' in text:
    #     reply = "@miningful님 방토는여? :angry:"
    # elif '짬뽕' in text:
    #     reply = "짬뽕?! :soso:"
    # elif 'UBDRWU3GT' in text:
    #     reply = "차가운 예원님.. :sob:"
    elif '주사위' == text:
        reply = str(random.randint(1, 6))
    else:
        reply = 'None'
    return reply
