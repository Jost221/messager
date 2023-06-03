def create(mod, **qwargs):
    object = mod(**qwargs)
    object.save()
    return object