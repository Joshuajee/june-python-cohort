import lib.hello
import lib.lib
import simplemath
import greetings
import lib
from lib import hello
from lib.hello import say_hello

from simplemath import PI, add as name


#importing with alias simplemath- this will change the name of simplemath to sm 
import simplemath as sm


print(simplemath.PI)

print(simplemath.add(10, 30))

print(simplemath.sub(10, 3879))


print(PI)

print(name(7, 8))

print(sm.add(4,5))

print(greetings.goodmorning("Joe"))

print(hello.say_hello())

print(lib.hello.say_hello())

lib.lib.do_something()