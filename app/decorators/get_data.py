import functools

def get_data_factory(mode="rb"):
    def get_data(fc):
        @functools.wraps(fc)
        def _(*args, **kwargs):
            if 'path' in kwargs:
                path = kwargs.get('path')
                with open(file=path, mode=mode) as fp:
                    data = fp.read()
                kwargs['content'] = data
            return fc(*args, **kwargs)
        return _
    return get_data