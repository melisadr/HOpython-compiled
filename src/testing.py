import ctypes as C
import sys

math = C.CDLL('./libaddarrays.so')
print "-------------------"
print "Probando add_float"
print "-------------------"
print "  " 
a=10
b=-4
math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]
sumados=math.add_float(a,b)

if sumados ==6.0:
    print "Paso el test caso 1"
else:
    print "No paso el test"
 
a=10.0
b=-4.0
math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]
sumados=math.add_float(a,b)

if sumados ==6.0:
    print "Paso el test caso 2"
else:
    print "No paso el test"
       
print "  "   
print "-------------------"
print "Probando add_int"
print "-------------------"
print "  " 
a=10
b=-4
math.add_int.restype = C.c_int
math.add_int.argtypes = [C.c_int, C.c_int]
sumados=math.add_int(a,b)

if sumados ==6:
    print "Paso el test"
else:
    print "No paso el test"
    
# TODO no funciona float_ref 
print "  "   
print "----------------------"
print "Probando add_float_ref"
print "----------------------"
print "  " 
a = C.c_float(10.0)
b = C.c_float(-4.0)
c = C.c_float() #tengo que inicializar esta var con algo?
try:
    math.add_float_ref.argtypes = [C.c_void_p, C.c_void_p, C.c_void_p]
    math.add_float_ref(C.byref(a),C.byref(b),C.byref(c))
    
    if c.value ==6.0:
        print "Paso el test"
    else:
        print "No paso el test"
except:
    e=sys.exc_info()
    print "No paso el test, revisar esta funcion (python)"     
    print e   


"""

int add_float_ref(float *a, float *b, float *c) {
  *c = *a + *b;
  return 0;
}
"""
# TODO no funciona add_int_ref 
print "  "   
print "----------------------"
print "Probando add_int_ref"
print "----------------------"
print "  " 

a = C.c_int(10)
b = C.c_int(-4)
c = C.c_int()
#try:
math.add_int_ref.argtypes = [C.c_void_p, C.c_void_p, C.c_void_p]
math.add_int_ref(C.byref(a),C.byref(b),C.byref(c))

if c.value ==6:
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
print "  "   
print "----------------------"
print "Probando add_int_array"
print "----------------------"
print "  " 

a = C.c_int(10)
b = C.c_int(-4)
c = C.c_int()
n = C.c_int(1)
try:
    math.add_int_array.argtypes = [C.c_void_p, C.c_void_p, C.c_void_p,C.c_int]
    math.add_int_array(C.byref(a),C.byref(b),C.byref(c),n)
    
    if c.value ==6:
        print "Paso el test"
    else:
        print "No paso el test"
except:
    e=sys.exc_info()
    print "No paso el test, revisar esta funcion (python)"     
    print e


"""
int add_int_array(int *a, int *b, int *c, int n) {
  int i;
  for (i = 0; i < n; i++) {
    c[i] = a[i] + b[i];
  }
  return 0;
}

float dot_product(float *a, float *b, int n) {
  float res;
  int i;
  res = 0;
  for (i = 0; i < n; i++) {
    res = res + a[i] * b[i];
  }
  return res;
}


"""