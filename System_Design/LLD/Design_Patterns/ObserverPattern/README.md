### **OBSERVER PATTERN**

  > **Observer** is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

  https://refactoring.guru/design-patterns/observer

- Very similar to PUBLISHER → SUBSCRIBER model
- **Observable → Publisher**
    - Methods: `subsribe()`, `unsubscribe()` , `setData(int count)`, `notifyAll()`
    - `setData()` refers to any change → this will trigger `notifyAll()` → will call update(this) method of the observer
- **Observer → Subscriber**
    - Objects of Observer get added to the subscribers list when you call `Observable.subsribe(obj)`

### Example
- Users visit an ecommerce platform and clicks on `NOTIFY ME` button on that product
- The users need to get notified (Email, Phone) in case the stock of that product changes

#### Solution
- Observable/Publisher: `StockObservable`
- Observer/Subscriber: `NotificationAlertObserver`
- **Note**
  1. These 2 are Interfaces that we implement for our classes for each use case
  2. The `StockObservable` Interface should be an `Class` since here we couldn't define the `subsribers` arraylist ( we did that in the implementation which is not good according to SOLID principles)