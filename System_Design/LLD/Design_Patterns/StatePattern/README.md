## State Pattern

> **State** is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

https://refactoring.guru/design-patterns/state

- Consider this as **Finite State Machine**

**Steps for Implementing**

1. `State` interface/abstract class will contain all the possible methods any state can have.
2. Concrete Implementations of `State` interface/ABC will implement only the methods that they can offer in that state on the object ( *Other methods can raise some Exception or print saying that this operation is not allowed in this current state* )
3. **Each state will also have a object on which state changes are caused** ( *Ex: `AtmMachine` object in case of an ATM* )

### Sample of ATM ( Simpler version )
![ATM Pattern](https://i.imgur.com/v8OKuTv.png)
