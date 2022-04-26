import casbin

e = casbin.Enforcer("./to/model.conf", "./to/policy.csv")

sub = "alice"  # 想要访问资源的用户
obj = "data1"  # 将要被访问的资源
act = "read"  # 用户对资源进行的操作


if e.enforce(sub, obj, act):
    # 允许alice读取data1
    print("can")
    pass
else:
    raise BaseException("not can")
    # 拒绝请求，抛出异常
    pass

