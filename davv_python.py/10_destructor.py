class Sample:
    i=10
    def __init__(self):
        print('object has been create')
    def __del__(self):
        print('object has been destroyed')

obj=Sample()            