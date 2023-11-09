# 1) >>> int(123.987)
# 2) 123
# 3) >>> int(10+5j)
# 4) TypeError: can't convert complex to int
# 5) >>> int(True)
# 6) 1
# 7) >>> int(False)
# 8) 0
# 9) >>> int("10")
# 10) 10
# 11) >>> int("10.5")
# 12) ValueError: invalid literal for int() with base 10: '10.5'
# 13) >>> int("ten")
# 14) ValueError: invalid literal for int() with base 10: 'ten'
# 15) >>> int("0B1111")
# 16) ValueError: invalid literal for int() with base 10: '0B1111'


##############################################################################
# 1. We can convert from any type to int except complex type.
# 2. If we want to convert str type to int type, compulsary str should contain only integral
# value and should be specified in base-10