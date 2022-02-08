def test_var_args(f__arg, *argv) :
    print ("first normal arg:", f__arg)
    for arg in argv :
        print ( " another arg through *argv:", arg)

test_var_args(' yasoob',' python',' eggs' ,' test' )



def greet_me (f__arg, *argv, **kwargs) :
    for key, value in kwargs. items () :
        print("{0} == {1}". format (key, value) )

greet_me(1,[1,2,3],name="yasoob")