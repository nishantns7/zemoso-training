varA='hello'
varB='world'

if type(varA) and type(varB) is int:
    if varA>varB:
        print("bigger")
    elif varA==varB:
        print("equal")
    else:
        print("smaller")
else:
    print("string involved")
