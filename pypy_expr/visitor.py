import ast
from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code

class PyPySExprVisitor(ast.NodeVisitor):

    def __call__(self, node: ast.AST = None, source: str = ""):
        if not node:
            self._source = source
            self._ast = ast.parse(source)
        else:
            self._ast = node
        return self.visit(self._ast)

    def visit_Module(self, node: ast.Module) -> SExpr:
        return block(*map(self.visit, node.body))

    def visit_Num(self, node: ast.Num) -> SExpr:
        return const(node.n)

    def visit_Bool(self, node: ast.Num) -> SExpr:
        return const(node.n)

    def visit_Str(self, node: ast.Str) -> SExpr:
        return const(node.s)

    def visit_Name(self, node: ast.Name) -> SExpr:
        return var(node.id)

    def visit_BinOp(self, node: ast.BinOp) -> SExpr:
        return binop(self.visit(node.left), self.visit(node.op), self.visit(node.right))

    def visit_Call(self, node: ast.Call) -> SExpr:
        return call(self.visit(node.func), *map(self.visit, node.args))

    def visit_Expr(self, node: ast.Expr) -> SExpr:
        return self.visit(node.value)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> SExpr:
        # TODO: use ann assign.
        return assign_star(node.target.id, self.visit(node.value))

    def visit_Assign(self, node: ast.Assign) -> SExpr:
        targets = node.targets
        value = node.value

        if len(targets) == 1:
            return assign_star(targets[0].id, self.visit(value))
        # TODO: use assign if has var. support tuple as left value.
        # return block(
        #     *(assign_star(target_item.id, self.visit(value_item)) for target_item in targets for value_item in value))

    def visit_Tuple(self, node: ast.Tuple) -> SExpr:
        return mktuple(*(self.visit(item) for item in node.elts))

    def visit_Assert(self, node: ast.Assert) -> SExpr:
        raise NotImplementedError()

    def visit_For(self, node: ast.For) -> SExpr:
        return for_in(n=node.target.id, obj=self.visit(node.iter), body=block(*map(self.visit, node.body)))

    def visit_List(self, node: ast.List) -> SExpr:
        raise NotImplementedError()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> SExpr:
        return define(
            func_name=node.name,
            args=[arg.arg for arg in node.args.args],
            body=block(*map(self.visit, node.body)),
            defaults=block(*map(self.visit, node.args.defaults))
        )

    def visit_Return(self, node: ast.Return) -> SExpr:
        raise NotImplementedError()

    def visit_Dict(self, node: ast.Dict) -> SExpr:
        kv = {}
        for index in range(0, len(node.keys)):
            k = node.keys[index]
            v = node.values[index]
            kv[k.id] = self.visit(v)
        return record(**kv)

    # operators
    def visit_Add(self, node: ast.Add) -> SExpr:
        return BinOp.ADD

    def visit_Sub(self, node: ast.Sub) -> SExpr:
        return BinOp.SUBTRACT

    def visit_Div(self, node: ast.Div) -> SExpr:
        return BinOp.TRUE_DIVIDE

    def visit_Mult(self, node: ast.Mult) -> SExpr:
        return BinOp.MULTIPLY

    def visit_Mod(self, node: ast.Mod) -> SExpr:
        return BinOp.MODULO

    def visit_FloorDiv(self, node: ast.FloorDiv) -> SExpr:
        return BinOp.FLOOR_DIVIDE

    def visit_LShift(self, node: ast.LShift) -> SExpr:
        return BinOp.LSHIFT

    def visit_RShift(self, node: ast.RShift) -> SExpr:
        return BinOp.RSHIFT

    def visit_MatMult(self, node: ast.MatMult) -> SExpr:
        return BinOp.MATRIX_MULTIPLY

    def visit_And(self, node: ast.And) -> SExpr:
        return BinOp.AND

    def visit_Or(self, node: ast.Or) -> SExpr:
        return BinOp.OR

    def visit_BitXor(self, node: ast.BitXor) -> SExpr:
        return BinOp.XOR

    def visit_Subscript(self, node: ast.Subscript) -> SExpr:
        return BinOp.SUBSCR

    def visit(self, node) -> SExpr:
        return super().visit(node)
