from privilegios import Privilegios
from admin import Admin

privilegios = Admin(['Pode adicionar postagem', 'Pode apagar postagem', 'Pode banir usuario'])
privilegios.mostrar_privilegios()
