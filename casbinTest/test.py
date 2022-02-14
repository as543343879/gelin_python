import casbin

e = casbin.Enforcer("./to/model.conf", "./to/policy.csv")