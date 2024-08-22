class A:
    a = 10
    
class B:
    b = 20

class C:
    c = 30
    
class SimpleInheritance(A):
    simple = 5


simple_inheritance = SimpleInheritance()

print(simple_inheritance.a)

class MultilevelInheritance(SimpleInheritance):
    pass

multi_level_inheritance = MultilevelInheritance()

#Have access to a from class A
print(multi_level_inheritance.a)
# Have access to simple from class SimpleInheritance
print(multi_level_inheritance.simple)




# Multiple Inheritance class ABC inheriting for Class A, B, and C
class ABC(A, B, C):
    pass

abc = ABC()

print(abc.a, abc.b, abc.c)

