
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x84H\x92\xbd\xbf<\xfc\xe7n\x16\x91J\xe0\xc1p\t'
    
_lr_action_items = {'RPAREN':([1,2,3,5,6,7,9,10,11,12,13,14,15,16,],[-11,-3,-9,-12,-10,-2,-8,-1,-4,15,-8,-7,-5,-6,]),'STRING':([0,1,2,3,4,5,6,7,9,10,11,13,15,],[1,-11,-3,-9,1,-12,-10,-2,1,-1,-4,1,-5,]),'INT':([0,1,2,3,4,5,6,7,9,10,11,13,15,],[3,-11,-3,-9,3,-12,-10,-2,3,-1,-4,3,-5,]),'QUOTE':([0,1,2,3,4,5,6,7,9,10,11,13,15,],[4,-11,-3,-9,4,-12,-10,-2,4,-1,-4,4,-5,]),'SYMBOL':([0,1,2,3,4,5,6,7,9,10,11,13,15,],[5,-11,-3,-9,5,-12,-10,-2,5,-1,-4,5,-5,]),'FLOAT':([0,1,2,3,4,5,6,7,9,10,11,13,15,],[6,-11,-3,-9,6,-12,-10,-2,6,-1,-4,6,-5,]),'LPAREN':([0,1,2,3,4,5,6,7,9,10,11,13,15,],[9,-11,-3,-9,9,-12,-10,-2,9,-1,-4,9,-5,]),'$end':([1,2,3,5,6,7,8,10,11,15,],[-11,-3,-9,-12,-10,-2,0,-1,-4,-5,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'quoted':([0,4,9,13,],[2,2,2,2,]),'sexps':([9,13,],[12,16,]),'list':([0,4,9,13,],[7,7,7,7,]),'sexp':([0,4,9,13,],[8,11,13,13,]),'atom':([0,4,9,13,],[10,10,10,10,]),'empty':([9,13,],[14,14,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sexp","S'",1,None,None,None),
  ('sexp -> atom','sexp',1,'p_sexp','./lisp_parser.py',16),
  ('sexp -> list','sexp',1,'p_sexp','./lisp_parser.py',17),
  ('sexp -> quoted','sexp',1,'p_sexp','./lisp_parser.py',18),
  ('quoted -> QUOTE sexp','quoted',2,'p_quoted','./lisp_parser.py',23),
  ('list -> LPAREN sexps RPAREN','list',3,'p_list','./lisp_parser.py',27),
  ('sexps -> sexp sexps','sexps',2,'p_sequence','./lisp_parser.py',31),
  ('sexps -> empty','sexps',1,'p_atoms_empty','./lisp_parser.py',35),
  ('empty -> <empty>','empty',0,'p_empty','./lisp_parser.py',38),
  ('atom -> INT','atom',1,'p_atom_int','./lisp_parser.py',41),
  ('atom -> FLOAT','atom',1,'p_atom_float','./lisp_parser.py',44),
  ('atom -> STRING','atom',1,'p_atom_string','./lisp_parser.py',47),
  ('atom -> SYMBOL','atom',1,'p_atom_symbol','./lisp_parser.py',50),
]
