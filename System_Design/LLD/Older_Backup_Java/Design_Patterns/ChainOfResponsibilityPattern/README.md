##  **CHAIN OF RESPONSIBILITY PATTERN**

  > **Chain of Responsibility** is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.
  https://refactoring.guru/design-patterns/chain-of-responsibility
  
- You have a sequence of handlers, the current handler doesnt know anything. It just checks if it can handle it else directly calls the nextHandler ( *no knowledge about other handlers, just focuses on themselves* )
- **Use Cases** → Logging, ATM Withdrawl ( you have steps to follow in order for one transaction )