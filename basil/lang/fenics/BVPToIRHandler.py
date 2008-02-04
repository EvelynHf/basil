#! /usr/bin/env python
# ______________________________________________________________________
"""Module BVPToIRHandler

NOTE: A lot of this was automatically generated by pgen2handler.py.

Jonathan Riehl

$Id$
"""
# ______________________________________________________________________
# Module imports

import token

# FIXME: The handler base class should be moved out of Mython.
from basil.lang.mython.Handler import *
from bvpir import *

if __debug__:
    import pprint

from ..mython import ASTUtils

# ______________________________________________________________________
# Module data

ALE_VALUE_TYPE = "ALE::Mesh::real_section_type::value_type"

# ______________________________________________________________________
# Utility functions

bvpir_to_tuple = ASTUtils.mk_ast_to_tuple(AST)

# ______________________________________________________________________
# Class definitions

class BVPToIRHandlerError (Exception):
    """Class BVPToIRHandlerError

    Exception subclass used to signal some sanity check failed in the
    course of converting a BVP parse tree into the BVP intermediate
    representation."""

# ______________________________________________________________________

class BVPToIRHandler (Handler):
    """Class BVPToIRHandler

    Visitor class that walks a BVP concrete parse tree, constructing
    an intermediate representation (BVP IR)."""
    # ____________________________________________________________
    def __call__ (self, cst):
        """BVPToIRHandler.__call__()

        Translate from the input BVP concrete parse tree to the BVP
        intermeidate representation."""
        if __debug__:
            import pprint
            pprint.pprint(cst)
        self.init_bvp()
        ret_val = self.handle_node(cst)
        if __debug__:
            pprint.pprint(bvpir_to_tuple(ret_val))
        return ret_val

    # ____________________________________________________________
    def get_fresh (self):
        """BVPToIRHandler.get_fresh()

        Get a fresh intermediate variable."""
        ret_val = Var("intermediate%d" % self.intermediate_count)
        self.intermediate_count += 1
        return ret_val

    # ____________________________________________________________
    def init_bvp (self):
        """BVPToIRHandler.init_bvp()

        Initialize the BVP state variables."""
        self.stack = []
        self.identifiers = {}
        self.decl_ty = None
        self.intermediate_count = 0
        self.ir_env = {}

    # ____________________________________________________________
    def get_line_no (self, elem):
        """BVPToIRHandler.get_line_no(elem)

        Return a line number, if possible, for the input concrete
        parse tree element (may either be a tree node or a token).
        Returns the first line number it finds, or None, if none is
        found."""
        ret_val = None
        # First check to see if this is a 2-tuple
        if type(elem) == tuple:
            if len(elem) == 2:
                if self.is_token(elem):
                    ret_val = elem[0][2][0]
                else:
                    for child in elem[1]:
                        ret_val = self.get_line_no(child)
                        if ret_val is not None:
                            break
            elif len(elem) == 5:
                # XXX Warning: this is based on a property of the tokenizer.
                ret_val = elem[2][0]
        return ret_val

    # ____________________________________________________________
    def fail_unless (self, predicate, message, location_help = None):
        if not predicate:
            line_num = None
            if location_help is not None:
                line_num = get_line_no(location_help)
            if line_num is None:
                raise BVPToIRHandlerError(message)
            else:
                raise BVPToIRHandlerError("At line %d: %s" % (line_num,
                                                              message))

    # ____________________________________________________________
    def get_children (self, node):
        return [] if self.is_token(node) else node[1]

    # ____________________________________________________________
    def get_nonterminal (self, node):
        return node[0]

    # ____________________________________________________________
    def is_token (self, node):
        return type(node[0]) == tuple

    # ____________________________________________________________
    def make_node (self, node_id, children):
        return (node_id, children)

    # ____________________________________________________________
    def handle_arith_expr (self, node):
        children = self.get_children(node)
        if len(children) == 1:
            ret_val = self.handle_node(children[0])
        else:
            raise NotImplementedError("FIXME")
        return ret_val

    # ____________________________________________________________
    def handle_atom (self, node):
        children = self.get_children(node)
        self.fail_unless(self.is_token(children[0]), "Ill formed atom.", node)
        first_tok = children[0][0]
        if first_tok[0] == token.NAME:
            tok_id = first_tok[1]
            self.fail_unless(tok_id in self.identifiers,
                             "Unknown variable '%s'." % tok_id, node)
            ret_val = []
        elif first_tok[0] == token.OP:
            # Tensor contraction.
            self.fail_unless(first_tok[1] == "<", "Unexpected operation, '%s'."
                             % first_tok[1], node)
            self.crnt_basis_index = "f"
            expr0 = self.handle_node(children[1])
            # FIXME: Make sure expr0 is a tensor.
            self.crnt_basis_index = "g"
            expr1 = self.handle_node(children[3])
            # FIXME: Make sure expr1 is a tensor.
            del self.crnt_basis_index
            self.fail_unless(type(expr0) == type(expr1),
                             "Mismatched types in contraction.", node)
            intermediate = self.get_fresh()
            intermediate_init = []
            if type(expr0) == tuple:
                expr0_mult = Index(expr0[0], Var("dim_index"))
                expr0_init = [expr0[1]]
                expr1_mult = Index(expr1[0], Var("dim_index"))
                expr1_init = [expr1[1]]
                intermediate_init.append(Assign(LVar(intermediate.vid),
                                                Const("0.0")))
                intermediate_rhs = Sum("dim_index", "dim",
                                       Mult([expr0_mult, expr1_mult]))
            else:
                expr0_mult = Index(Var("basis"), Add([
                    Mult([Var("quad"), Var("numBasisFuncs")]), Var("f")]))
                expr0_init = []
                expr1_mult = Index(Var("basis"), Add([
                    Mult([Var("quad"), Var("numBasisFuncs")]), Var("g")]))
                expr1_init = []
                intermediate_rhs = Mult([expr0_mult, expr1_mult])
            self.ir_env[intermediate] = (ALE_VALUE_TYPE, None)
            elem_mat_lhs = LIndex(LVar("elemMat"),
                                  Add([Mult([Index(Var("indicies"), Var("f")),
                                             Var("numBasisFuncs")]),
                                       Index(Var("indicies"), Var("g"))]))
            ret_val = Loop("f", "numBasisFuncs",
                           expr0_init +
                           [Loop("g", "numBasisFuncs",
                                 expr1_init +
                                 intermediate_init +
                                 [Assign(LVar(intermediate.vid),
                                         intermediate_rhs),
                                  Assign(elem_mat_lhs,
                                         Mult([intermediate,
                                               Index(Var("quadWeights"),
                                                     Var("quad")),
                                               Var("detJ")]))])])
        else:
            raise NotImplementedError("FIXME")
        return ret_val

    # ____________________________________________________________
    def handle_bounds (self, node):
        raise NotImplementedError("FIXME")

    # ____________________________________________________________
    def handle_constraint (self, node):
        children = self.get_children(node)
        if len(children) == 1:
            child_output = self.handle_node(children[0])
            ret_val = [
                Special("init"),
                Loop("cell", "cells",
                     [Special("compute_geometry"),
                      Loop("field", "fields",
                           [Special("get_disc"),
                            Loop("quad", "quads",
                                 [child_output])])]),
                Special("deinit")
                ]
        else:
            raise NotImplementedError("FIXME")
        return ret_val

    # ____________________________________________________________
    def handle_decl (self, node):
        children = self.get_children(node)
        decl_ty_tok = children[0][0]
        self.decl_ty = decl_ty_tok[1]
        self.fail_unless(len(children) == 2, "Ill formed declaration.", node)
        ret_val = self.handle_node(children[1])
        self.decl_ty = None
        if __debug__:
            print self.identifiers
        return ret_val

    # ____________________________________________________________
    def handle_expr (self, node):
        children = self.get_children(node)
        if len(children) == 1:
            ret_val = self.handle_node(children[0])
        else:
            raise NotImplementedError("FIXME")
        return ret_val

    # ____________________________________________________________
    def handle_factor (self, node):
        children = self.get_children(node)
        if len(children) == 1:
            ret_val = self.handle_node(children[0])
        else:
            self.fail_unless((len(children) == 2) and
                             (self.is_token(children[0])),
                             "Ill formed factor node.", node)
            rhs_result = self.handle_node(children[1])
            prefix = children[0][0][1]
            if prefix == "grad":
                intermediate = self.get_fresh()
                self.ir_env[intermediate] = (ALE_VALUE_TYPE, "dim")
                intermediate_lval = LVar(intermediate.vid)
                intermediate_init = Assign(
                    LIndex(intermediate_lval, Var("i1")),
                    Const(0.0))
                inv_j = Index(Var("invJ"),
                              Add([Mult([Var("i1"), Var("dim")]),
                                   Var("i2")]))
                basis_der = Index(Var("basisDer"),
                                  Add([Mult([Add([Mult([Var("quad"),
                                                        Var("numBasisFuncs")]),
                                                  Var(self.crnt_basis_index)]),
                                             Var("dim")]),
                                       Var("i2")]))
                    
                ret_val = (intermediate,
                           Loop("i1", "dim",
                                [intermediate_init,
                                 Loop("i2", "dim",
                                      [SumAssign(LIndex(intermediate_lval,
                                                        Var("i1")),
                                                 Mult([inv_j, basis_der]))])]))
            else:
                raise NotImplementedError("FIXME")
        return ret_val

    # ____________________________________________________________
    def handle_id_list (self, node):
        self.fail_unless(self.decl_ty is not None,
                         "Unexpected identifier list.", node)
        children = self.get_children(node)
        for child_index in xrange(0, len(children), 2):
            child = children[child_index]
            self.identifiers[child[0][1]] = self.decl_ty
        return None

    # ____________________________________________________________
    def handle_line (self, node):
        children = self.get_children(node)
        self.fail_unless((len(children) == 2) and (self.is_token(children[1])),
                         "Ill formed line.", node)
        return self.handle_node(children[0])

    # ____________________________________________________________
    def handle_power (self, node):
        children = self.get_children(node)
        if len(children) == 1:
            ret_val = self.handle_node(children[0])
        else:
            self.fail_unless(len(children) == 3,
                             "Ill formed power expression.", node)
            raise NotImplementedError("FIXME")
        return ret_val

    # ____________________________________________________________
    def handle_start (self, node):
        children = self.get_children(node)
        module_body = []
        for child in children[:-1]:
            child_result = self.handle_node(child)
            if child_result is not None:
                self.fail_unless(type(child_result) == list,
                                 "Internal code generation error!", child)
                module_body.extend(child_result)
                if __debug__:
                    print module_body
        self.fail_unless(len(module_body) > 0, "No code to generate!",
                         children[-1])
        intermediates = [(i_var.vid, i_ty, i_dim)
                         for (i_var, (i_ty, i_dim)) in self.ir_env.items()]
        intermediates.sort()
        decs = []
        for i_name, i_ty, i_dim in intermediates:
            decs.append(VDec(i_name, i_ty, i_dim))
        return BVPClosure(decs, module_body)

    # ____________________________________________________________
    def handle_term (self, node):
        children = self.get_children(node)
        if len(children) == 1:
            ret_val = self.handle_node(children[0])
        else:
            raise NotImplementedError("FIXME")
        return ret_val

    # ____________________________________________________________
    def handle_vec_op (self, node):
        raise NotImplementedError("FIXME")

# ______________________________________________________________________
# Main routine

def main (*args):
    pass

# ______________________________________________________________________

if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])

# ______________________________________________________________________
# End of BVPToIRHandler.py
