## Builder Pattern

### References
-  https://medium.com/@vinodkumarbheel61/builder-design-pattern-in-java-a-practical-guide-8a9aaf3d51a3
- https://gitlab.com/shrayansh8/interviewcodingpractise/-/tree/main/src/LowLevelDesign/DesignPatterns/BuilderDesignPattern
- https://refactoring.guru/design-patterns/builder

### Concepts
- Why? You might need lot of constructors and that is hard to mantain
- In builder pattern you have these entities
  1. **Product**: This is the complex object that needs to be created. It often has numerous optional parameters.
  2. **Builder**: This interface defines the steps to construct the product. Each step is typically represented by a method in the interface.
  3. **ConcreteBuilder**: This class implements the Builder interface and provides the specific implementations for each step of the construction process.
  4. **Director**: This class orchestrates the construction process by invoking the methods on the builder interface. It is not required, but it helps in providing a more fluent and consistent way to construct objects.
  5. **Client**: The client is responsible for creating the director and configuring it with a specific concrete builder to construct the product.
- **Important Notes**
  - **Builder**: methods needed to build, **Director**: in what sequence will those steps get called
  - In `ConcreteBuilder` 
    1. On creation, initialize an object of `Product` ( _you will set the paramters later_ ) 
    2. Each method/operation step, return `this`. So that you can chain the steps
    3. Final `build()` step, that returns the actual product - `this.productObject`

### Example
#### Problem
- You need to build a Computer. But you have various options for its configurations.

#### Solution
- Matching with Builder pattern
  1. **Product**: `Computer`
  2. **Builder**:  `ComputerBuilder`
  3. **ConcreteBuilder**: `DesktopComputerBuilder`
  4. **Director**: `ComputerDirector`
  5. **Client**: `Main`
  
- In case you have to make a `GamingComputer`
  1. In `ComputerDirector` add a new `constructGamingComputer` method, in which you can change the sequence and add a better GPU if needed