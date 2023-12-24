- Memory allocation is automatically handled by garbage collector

### new() vs make()

1. new()
   - Allocates memory but doesnt initialize it
   - You get the memory address as return
   - zeroed storage: you cant put anything in it 
2. make()
   - Allocates memory and initialize it
   - You get the memory address as return
   - non-zeroed storage: you can put data 