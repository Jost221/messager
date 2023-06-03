def create(mod, **qwargs):
    object = mod(**qwargs)
    object.save()
    return object

def to_dict(items):
    res_dict = {}
    if not hasattr(items, '__len__'):
        items = [items]
    for i in range(len(items)):
        object_dict = {}
        for name, value in items[i].__dict__.items():
            if name[0] == '_': continue
            object_dict[name] = value
        if len(items) == 1:
            return object_dict
        res_dict[i] = object_dict
    return res_dict