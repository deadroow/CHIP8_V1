import functools
import os  # Importe os ici directement
from utils import display_msg # Assure-toi que l'import est correct

def check_path(fc):
    @functools.wraps(fc) # Correction de la faute de frappe ici
    def _(*args, **kwargs):
        if 'path' in kwargs:
            path_to_check = kwargs.get('path')
            if not os.path.exists(path_to_check): # Plus besoin de import_module ici
                display_msg(f"path {path_to_check} does not exist", "danger")
                return
        return fc(*args, **kwargs)
    return _