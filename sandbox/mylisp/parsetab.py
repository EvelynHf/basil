
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '3\xf1\xf6E\xfa\x14\xc3\x8dP\xb2\x98\x95#\xa3\xa2H'
    
_lr_action_items = {'RPAREN':([1,2,3,5,6,7,10,11,13,14,15,16,18,19,20,21,22,23,24,25,26,27,29,30,31,],[-19,-3,-7,-20,-18,-2,-17,-6,-4,-1,-16,-5,-8,-11,-16,-10,27,-16,-15,-9,27,-13,-14,31,-12,]),'STRING':([0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,23,25,27,28,31,],[1,-19,-3,-7,1,-20,-18,-2,-17,-6,1,-4,-1,1,-5,1,-8,-11,1,-10,1,-9,-13,1,-12,]),'INT':([0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,23,25,27,28,31,],[10,-19,-3,-7,10,-20,-18,-2,-17,-6,10,-4,-1,10,-5,10,-8,-11,10,-10,10,-9,-13,10,-12,]),'QUOTE':([0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,23,25,27,28,31,],[4,-19,-3,-7,4,-20,-18,-2,-17,-6,4,-4,-1,4,-5,4,-8,-11,4,-10,4,-9,-13,4,-12,]),'SYMBOL':([0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,23,25,27,28,31,],[5,-19,-3,-7,5,-20,-18,-2,-17,-6,5,-4,-1,5,-5,5,-8,-11,5,-10,5,-9,-13,5,-12,]),'FLOAT':([0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,23,25,27,28,31,],[6,-19,-3,-7,6,-20,-18,-2,-17,-6,6,-4,-1,6,-5,6,-8,-11,6,-10,6,-9,-13,6,-12,]),'COMMA_AT':([0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,23,25,27,28,31,],[8,-19,-3,-7,8,-20,-18,-2,-17,-6,8,-4,-1,8,-5,8,-8,-11,8,-10,8,-9,-13,8,-12,]),'COMMA':([0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,23,25,27,28,31,],[12,-19,-3,-7,12,-20,-18,-2,-17,-6,12,-4,-1,12,-5,12,-8,-11,12,-10,12,-9,-13,12,-12,]),'LPAREN':([0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,23,25,27,28,31,],[15,-19,-3,-7,15,-20,-18,-2,20,-17,-6,15,-4,-1,15,-5,15,-8,-11,15,-10,15,-9,-13,15,-12,]),'BACKQUOTE':([0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,23,25,27,28,31,],[17,-19,-3,-7,17,-20,-18,-2,-17,-6,17,-4,-1,17,-5,17,-8,-11,17,-10,17,-9,-13,17,-12,]),'DOT':([1,2,3,5,6,7,10,11,13,14,15,16,18,19,21,22,23,24,25,27,29,31,],[-19,-3,-7,-20,-18,-2,-17,-6,-4,-1,-16,-5,-8,-11,-10,28,-16,-15,-9,-13,-14,-12,]),'$end':([1,2,3,5,6,7,9,10,11,13,14,16,18,19,21,25,27,31,],[-19,-3,-7,-20,-18,-2,0,-17,-6,-4,-1,-5,-8,-11,-10,-9,-13,-12,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'quoted':([0,4,12,15,17,20,23,28,],[2,2,2,2,2,2,2,2,]),'dotted_list':([0,4,12,15,17,20,23,28,],[3,3,3,3,3,3,3,3,]),'sexps':([15,20,23,],[22,26,29,]),'list':([0,4,8,12,15,17,20,23,28,],[7,7,19,7,7,7,7,7,7,]),'sexp':([0,4,12,15,17,20,23,28,],[9,18,21,23,25,23,23,30,]),'spliced':([0,4,12,15,17,20,23,28,],[11,11,11,11,11,11,11,11,]),'qquoted':([0,4,12,15,17,20,23,28,],[13,13,13,13,13,13,13,13,]),'atom':([0,4,12,15,17,20,23,28,],[14,14,14,14,14,14,14,14,]),'unquoted':([0,4,12,15,17,20,23,28,],[16,16,16,16,16,16,16,16,]),'empty':([15,20,23,],[24,24,24,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sexp","S'",1,None,None,None),
  ('sexp -> atom','sexp',1,'p_sexp','lisp_parser.py',16),
  ('sexp -> list','sexp',1,'p_sexp','lisp_parser.py',17),
  ('sexp -> quoted','sexp',1,'p_sexp','lisp_parser.py',18),
  ('sexp -> qquoted','sexp',1,'p_sexp','lisp_parser.py',19),
  ('sexp -> unquoted','sexp',1,'p_sexp','lisp_parser.py',20),
  ('sexp -> spliced','sexp',1,'p_sexp','lisp_parser.py',21),
  ('sexp -> dotted_list','sexp',1,'p_sexp','lisp_parser.py',22),
  ('quoted -> QUOTE sexp','quoted',2,'p_quoted','lisp_parser.py',27),
  ('qquoted -> BACKQUOTE sexp','qquoted',2,'p_qquoted','lisp_parser.py',31),
  ('unquoted -> COMMA sexp','unquoted',2,'p_unquoted','lisp_parser.py',35),
  ('spliced -> COMMA_AT list','spliced',2,'p_spliced','lisp_parser.py',39),
  ('dotted_list -> LPAREN sexps DOT sexp RPAREN','dotted_list',5,'p_dotted_list','lisp_parser.py',43),
  ('list -> LPAREN sexps RPAREN','list',3,'p_list','lisp_parser.py',47),
  ('sexps -> sexp sexps','sexps',2,'p_sequence','lisp_parser.py',51),
  ('sexps -> empty','sexps',1,'p_atoms_empty','lisp_parser.py',55),
  ('empty -> <empty>','empty',0,'p_empty','lisp_parser.py',58),
  ('atom -> INT','atom',1,'p_atom_int','lisp_parser.py',61),
  ('atom -> FLOAT','atom',1,'p_atom_float','lisp_parser.py',64),
  ('atom -> STRING','atom',1,'p_atom_string','lisp_parser.py',67),
  ('atom -> SYMBOL','atom',1,'p_atom_symbol','lisp_parser.py',70),
]
