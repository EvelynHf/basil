import ast
from basil.lang.mython import myfront_ast, mybuiltins

def myast_to_pyast (node, attr_name = None):
    if isinstance(node, myfront_ast.AST):
        node_type_name = type(node).__name__
        pynode_type = getattr(ast, node_type_name)
        ret_val = pynode_type(**myast_to_pyast(node.__dict__))
    elif isinstance(node, list):
        ret_val = [myast_to_pyast(elem) for elem in node]
    elif isinstance(node, dict):
        ret_val = dict((key, myast_to_pyast(val, key))
                       for key, val in node.items())
    else:
        if node is None and attr_name in ('lineno', 'col_offset'):
            ret_val = -1
        else:
            ret_val = node
    return ret_val

def main (*args):
    env = mybuiltins.initial_environment()
    for arg in args:
        text, env = mybuiltins._load_file(arg, env)
        myast, env = env['myfrontend'](text, env)
        pyast = myast_to_pyast(myast)
        pyast.lineno = pyast.col_offset = 0
        co = compile(pyast, 'xxx', 'exec')
        exec co in env

if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
