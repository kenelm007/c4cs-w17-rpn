import rpn
result = rpn.calculate("1 1 +")
assert(2, result)
result = rpn.calculate("2 0 -")
assert(2, result)
result = rpn.calculate("2 3 ^")
assert(8, result)
result = rpn.calculate("2 3 *")
assert(6, result)
result = rpn.calculate("9 3 /")
assert(3, result)
