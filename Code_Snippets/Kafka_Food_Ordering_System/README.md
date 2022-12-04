## Architecture of the System

1. Frontend System to take orders
    -  User places his order using this Frontend
2. Order Backend
    - Frontend sends the data to this system. It adds some additional information along with whatever information was passed and needed to place the order like - order details, customer details, address and banking details
    - It writes a record for each order to a Kafka topic - `order_details`
3. Transaction Backend
 - This is usually a Web server which is subsribed to the `order_details` kafka topics. Whenever the orders are added onto the Kafka topic, it receives it and processes it
 - It may do stuff like online banking transactions and other stuff needed to process the order
 - Once everything is successful and order has been placed, it then writes back to a Kafka topic `order_confirmed`
4. Analytics Backend 
    - It reads from the `order_confirmed` kafka topic. 
    - Analytics backend uses the data about the transaction/order made for analytical purposes like ad campaigns and future customer targetting
5. Email Backend
    - Reads from the `order_confirmed` kafka topic and then send out a mail to the user informing about the status of the order along with available status like estimated time of delivery, billing and payment details and any other information that needs to be provided to the user in the form of a mail.