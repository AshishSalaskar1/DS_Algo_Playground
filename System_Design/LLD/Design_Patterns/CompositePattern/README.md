## Composite Pattern
> Composite is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects.
<br> <br> https://refactoring.guru/design-patterns/composite

- Whenever you can Tree like object tree use Composite Pattern. You need to have a heirarchy such that
  1. Object can contain itself
  2. Object can contain List<Object> (_List of itself_)
  3. Some operation `op` can be performed both on `Object` and `List<Object>` 
  
### Imp Notes
- **Composite**: The `List<Object>` object which stores the list of objects
- Create two classes ->
  1. **Single Atomic Object**
  2. **Composite** ( `List <SingleAtomicObject>`)
- Both these need to have `op` function. Composite will just call `op` of each of its `SingleAtomicObject`)
- 💡: You dont create `List<Object>` -> You create `List<SingleAtomicObject>`. **Both of them implement the base interface** ( _so both have the same method_ )


### Example
- Use Case: Design `ls()` function. Normally you have to implement a `ls()` function in which you first check if its file, then print file name else iterate through that directory and print
- But, we want to eliminate that check logic

#### Solution
1. `FileSystem` is our base interface
2. `File` -> SingleAtomicObject
3. `Directory` -> Composite or `List <SingleAtomicObject>`
4. Both `File` and `Directory` implement `FileSystem` and have an `ls()` method

- You dont need to check anything, it will automatically handling ls