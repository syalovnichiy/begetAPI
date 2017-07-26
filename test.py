class A(object):
    def request(self, fn_name, **args):
        print 'curl {}//"{}"'.format(fn_name, args)

    def __getattr__(self, fn_name):
        return lambda **args: self.request(fn_name, **args)

a = A()

a.hello_world(k=42,b='blabla')

print a.__name__