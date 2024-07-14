def f(*args, **kwargs):
    #kwargs are named arguments such as money=0,
    #whereas args are just arguments like 0
    #kwargs passes out a dict
    if args:
        print("Positional:", args)
    else:
        print("Named:", kwargs)


f(100, 50, 25)
f(galleons=100, sickles=50, knuts=25)