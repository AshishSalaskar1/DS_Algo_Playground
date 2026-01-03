## **PROXY PATTERN**

  > **Proxy** is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.
  https://refactoring.guru/design-patterns/proxy

- Proxy acts like a Wrapper around your actual class object. This can be used like a PRE-PROCESSING and POST-PROCESSING logic layer
- Use Cases → Post/Pre Authentication, Access Checks before doing a Database operation

### Example
- Use case: You need to authenticate DB access based on user roles before performing operations
- **Note**: Your Proxy Class has a `IS-A` and `HAS-A` relationship (_Just like Decorator pattern_)
  1. `EmployeeDao` is the interface and `EmployeeDaiImpl` is its concrete implementation
  2. `EmployeeDaoProxy` implements `EmployeeDao` as well stores an object of the `EmployeeDao` interface implementations. It has extra methods for authentication as pre-process logic
  3. Why?
     1. `IS-A` --> You need to be able to **replace the `object` with its `proxy-object`**
     2. `HAS-A` --> You need an object to perform the actual methods ( PRE_PROCESS -> ACTUAL METHOD CALLS -> POST_PROCESS)