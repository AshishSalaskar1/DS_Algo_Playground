### **STRATEGY PATTERN**

  > **Strategy** is a behavioral design pattern that lets you define a family of **algorithms/capabilities**, put each of them into a separate class, and make their objects interchangeable.

  https://refactoring.guru/design-patterns/strategy

- **What is it?**
    - Lets say you have one base class and you keep on creating subclasses. Now whatever new functionality you want to add that you will add into the new subclasses and use common ones from the Base Classes.
    - Now, it may happen that you see a functionalities not present in base class, but most of its derived classes are implementing it → this causes code duplication. (*Same utilities implemented across levels in the inheritance tree* )
    - Solution
        - Use a `Strategies` interface which has a set of all the functionalities stored
        - In your base class, you just set this `stratergy` variable with required stratergy that the sub-clases will need in its constructor ( **Constructor Injection** )
- **Where to use?**
    - When you see that you sub-classes ( *can be at various depths* ) are implementing some extra functionality that can be easily shared across them


### Problem
- `Vehicle` base classes is implemented by 3 classes `OffRoadVehicle`,`PassengerVehicle` and `SportsVehicle`
- Each of these ovveride the `drive()` method from base class (**Note**: 2 subclasses define the same functionality using a ALL-WHEEL-Drive)

### Solution
- Create a `DriveStrategy` interface and create `AllWheelDriveStrategy` and `OffRoadDriveStrategy`
- `Vehicle` base class takes object of `DriveStrategy` as input to its constructor. The drive() method will just call the drive() in this 
- Each subclass, will create an object of the `DriveStrategy` it wants and pass that as parameter to its parent class constructor (using `super` keyword)