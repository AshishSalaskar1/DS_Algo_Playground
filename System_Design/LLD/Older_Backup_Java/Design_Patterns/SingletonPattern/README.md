## Singleton Design Pattern
- Create one and only one object

- Eager
    
    ```java
    class DBConnection {
         private static DBConnection conn = new DBConnection();
    
         private  DBConnection(){}
    
        public static DBConnection getConn() {
             return  conn;
        }
    }
    ```
    
- Lazy
    
    ```java
    class DBConnection {
         private static DBConnection conn;
    
         private  DBConnection(){}
    
        public static DBConnection getConn() {
             if(conn == null){
                 conn = new DBConnection();
             }
             return  conn;
        }
    }
    
    ```
    
- Synchronized
    
    ```java
    class DBConnection {
         private static DBConnection conn;
         private  DBConnection(){}
    
        synchronized static DBConnection getConn() {
             if(conn == null){
                 conn = new DBConnection();
             }
             return  conn;
        }
    }
    ```
    
- Double Locking
    
    ```java
    class DBConnection {
         private static DBConnection conn;
         private  DBConnection(){}
    
        public static DBConnection getConn() {
             if(conn == null){
                 synchronized (DBConnection.class){
                     if(conn==null){
    	                 conn = new DBConnection();
    	               }
                 }
             }
             return  conn;
        }
    }
    ```