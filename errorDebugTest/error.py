import logging


def testError():
    try:
        print('try...')
        r = 10 / 2
        print('result=', r)

    except ZeroDivisionError as e:
        print('except...', e)
        print(e.args)
    finally:
        print('finally...')
        print('end')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')
