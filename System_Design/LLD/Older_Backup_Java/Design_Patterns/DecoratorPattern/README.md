## Decorator Pattern
> **Decorator** is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

https://refactoring.guru/design-patterns/decorator

- Basically → Creating Wrappers over the classes ( *but replicating same methods as the base class* )


- The `Wrapper` **is-a** and **has-a** relationship with the `BaseClass`
    1. **IS-A** → The `Wrapper` extends/implements the `BaseClass` → hence it has all the methods of base class
    2. **HAS-A** → The `Wrapper` also stores a instance of `BaseClass` , this object is used to call methods of that base class if needed
    - Has-A relationship is also referred to as **Aggregate** ( *Wrapper class is aggregate of BaseClass* )



- So the `Wrapper` is also ideally an object of type `BaseClass`


- You can keep on nesting Wrapper(Wrapper(Wrapper(BaseClass))) and so on. BUT, each wrapper must have is-a and has-a relationship with the class its wrapping and have same methods as its parent.

- **Why is this needed?**
    1. Sometimes creating subclasses might lead to too many subclasses.
    2. These subclasses are dynamic, sometimes you want to manually add functionality on top of the existing base class implementations


### Example
1. We have `Notifier` abstract class -> Implementing it you get `NotifierImpl`
2. We create a `NotifierWrapper` abstract class which implements `Notifier`. This also stores a object of `Notifier` object which gets passed as Constructor parameter
3. `EmailWrapper` and `PhoneWrapper` are implementations of the wrapper class
4. `VipEmailWrapper` is a wrapper over a wrapper.
#### Note
- Each wrapper implementation has the same methods as the base class. 
- You also an object of the base class within the Wrapper, this can be used to call the parrent class objects in case its needed
