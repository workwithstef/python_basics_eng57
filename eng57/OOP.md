# All things Object-Oriented

### 4 Pillars of OOP
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

#### Abstraction
- only show essential operators, hiding complexity.
- Not revealing the specific mechanisms which allow to object to operate
- E.g having a coffee machine which has flashing lights and makes noises, BUT is operable by the simple push of a button.
- E.g Like a smartphone. It is ergonomic and has straight-forward user options, but you don't need to know exactly how each mechanism works

- in OOP you should create the class, its methods & attributes in a separate file. Then create and use the instance(s) in another file

#### Polymorphism
- the ability to redefine and override parent class methods


#### Inheritance
- The ability to adopt methods and attributes from a previously made 'parent' class.
- super().method() prevents sub-class from completely overriding method. Instead 'includes' parent method's features

#### Encapsulation
- making attributes/methods no longer accessible externally, using underscore. Made accessible internally using 'getter' method
- usually encapsulate attributes which should not be easily changed i.e. age/name/national ID/etc



### Key Words
- super() - used to include parent class's method without overriding the functionality
- __init__() - used to initiate class features the moment it is called, automatically implementing attributes/methods
- (self) - self is reference to the instance the class is tied to