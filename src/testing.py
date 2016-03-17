import ctypes as C
import sys

Mathlib = C.CDLL('./libaddarrays.so')
print "-------------------"
print "Probando add_float"
print "-------------------"
print ""
numa = 10.0
numb = -4.0
Mathlib.add_float.restype = C.c_float
Mathlib.add_float.argtypes = [C.c_float, C.c_float]
sumados = Mathlib.add_float(numa, numb)
if sumados == 6.0:
    print "Paso el test caso 1"
else:
    print "No paso el test"
NUMA = 10
NUMB = -4
Mathlib.add_float.restype = C.c_float
Mathlib.add_float.argtypes = [C.c_float, C.c_float]
sumados = Mathlib.add_float(NUMA, NUMB)
if sumados == 6.0:
    print "Paso el test caso 2"
else:
    print "No paso el test"
print ""
print "-------------------"
print "Probando add_int"
print "-------------------"
print ""
NUMA = 10
NUMB = -4
Mathlib.add_int.restype = C.c_int
Mathlib.add_int.argtypes = [C.c_int, C.c_int]
sumados = Mathlib.add_int(NUMA, NUMB)

if sumados == 6:
    print "Paso el test"
else:
    print "No paso el test"
print " "
print "----------------------"
print "Probando add_float_ref"
print "----------------------"
print " "
numa = C.c_float(10.0)
numb = C.c_float(-4.0)
numc = C.c_float()
try:
    Mathlib.add_float_ref.argtypes = [C.c_void_p, C.c_void_p, C.c_void_p]
    Mathlib.add_float_ref(C.byref(numa), C.byref(numb), C.byref(numc))
    if numc.value == 6.0:
        print "Paso el test"
    else:
        print "No paso el test"
except:
    e = sys.exc_info()
    print "No paso el test, revisar esta funcion (python)"
    print e


"""

int add_float_ref(float *a, float *b, float *c) {
  *c = *a + *b;
  return 0;
}
"""
# TODO no funciona add_int_ref
print " "
print "----------------------"
print "Probando add_int_ref"
print "----------------------"
print " "

a = C.c_int(10)
b = C.c_int(-4)
c = C.c_int()
#try:
Mathlib.add_int_ref.argtypes = [C.c_void_p, C.c_void_p, C.c_void_p]
Mathlib.add_int_ref(C.byref(a), C.byref(b), C.byref(c))

if c.value == 6:
    print "Paso el test"
else:
    print "No paso el test"
#except:
#    e=sys.exc_info()
#    print "No paso el test, revisar esta funcion (python)"
#    print e



"""

int add_int_ref(int *a, int *b, int *c) {
  *c = *a + *b;
  return 0;
"""
# TODO no funciona add_int_array
print " "
print "----------------------"
print "Probando add_int_array"
print "----------------------"
print " "

a = (C.c_int * 3)(10, 5, 2)
b = (C.c_int * 3)(1, -5, 3)
c = (C.c_int * 3)()
n = C.c_int(4)
try:
    Mathlib.add_int_array.argtypes = [C.c_void_p, C.c_void_p, C.c_void_p, C.c_int]
    Mathlib.add_int_array(C.byref(a), C.byref(b), C.byref(c), n)

    if (c[0], c[1], c[2])==(11, 0, 5):
        print "Paso el test"
    else:
        print "No paso el test: c=",c.value
except:
    e = sys.exc_info()
    print "No paso el test, revisar esta funcion (python)"
    print e

print " "
print "----------------------"
print "Probando dot_product  "
print "----------------------"
print " "

a = (C.c_float * 3)(10, 5, 2)
b = (C.c_float * 3)(1, -5, 3)
#res =  C.c_float 
n = C.c_int(3)
try:
    Mathlib.dot_product.restype = C.c_float
    Mathlib.dot_product.argtypes = [C.c_void_p, C.c_void_p, C.c_int]
    hola=Mathlib.dot_product(C.byref(a), C.byref(b), n)

    if hola==-9:
        print "Paso el test"
    else:
        print "No paso el test: c=",c.value
except:
    e = sys.exc_info()
    print "No paso el test, revisar esta funcion (python)"
    print e


