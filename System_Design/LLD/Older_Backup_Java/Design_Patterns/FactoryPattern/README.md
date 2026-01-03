## FACTORY PATTERN

> **Factory method** is a creational design pattern which solves the problem of creating product objects without specifying their concrete classes.
>
>
> The Factory Method defines a method, which should be used for creating objects instead of using a direct constructor call (`new` operator). Subclasses can override this method to change the class of objects that will be created.
>
> https://refactoring.guru/design-patterns/factory-method/java/example
>
> 
- Basically, you Main object needs some other objects for carrying out its tasks. These sub-objects maybe differently create based on the use case
- You have a `factory` method within the main class, which creates the objects needed for you based on the implementation. ( *Conctrete subclasses can directly create it else you pass what kind of object you want to the factory method* )

## Example
1. We have a `Button` interface which has 2 types - `HTMLButton` and `AndroidButton`
2. These 2 buttons are needed in out `Dialog` implementations
3. The `Dialog` implementation has a `createButton()` method which acts like a `Button-Factory` 