import functools

def check_rom_factory(checklist: list):
    def check_rom(fc):
        @functools.wraps(fc)
        def _(*args, **kwargs):
            for el in checklist:
                if el == 'len':
                    if len(kwargs.get('content')) > len(args[0].memory):
                        raise ValueError(f"ROM is too large {len (kwargs.get('content'))}bytes")
            
            return fc(*args, **kwargs)
        return _
    return check_rom