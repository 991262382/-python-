class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f'字典对象没有{key}属性')

    def __setattr__(self, key, value):
        self[key] = value


import unittest


class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = '值'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], '值')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):  # ??
            value = d['empty']  # 通过d['empty']访问不存在的key时，断言会抛出KeyError

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty  # 通过d.empty访问不存在的key时，我们期待抛出AttributeError：


if __name__ == '__main__':
    unittest.main()