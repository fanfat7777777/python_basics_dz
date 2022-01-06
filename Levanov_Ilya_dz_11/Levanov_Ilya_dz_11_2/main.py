class AlternativeEx(Exception):
    
    @staticmethod
    def check(err_str):
        if err_str == 'ZeroDivisionError':
            print('Делить на ноль нельзя')


try:
    1/0
except Exception as e:
    AlternativeEx().check(e.__class__.__name__)
