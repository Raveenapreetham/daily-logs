from aps import add,sub,mul,div
def values(num1,num2):
    res=add(num1,num2)
    return res

def valued(num1,num2):
    res=sub(num1,num2)
    return res

def val(num1,num2):
    res=mul(num1,num2)
    return res


def value(num1,num2):
    res=div(num1,num2)
    return res

def start():
    print('values:',values(20,30))
    print('valued',valued(20,30))
    print('val',val(20,30))
    print('value',value(20,30))


if __name__=='__main__':
    start()
