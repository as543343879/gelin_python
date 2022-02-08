def test_a(a):
    def inner_test_a(ctl_cls):
        print(a)
        print(ctl_cls)

    return inner_test_a

print(test_a(2)(123))