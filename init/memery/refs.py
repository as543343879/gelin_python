import objgraph

a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
b.append(a)

refs = objgraph.show_refs([a])

print(refs)

backrefs = objgraph.show_backrefs([a])

print(backrefs)