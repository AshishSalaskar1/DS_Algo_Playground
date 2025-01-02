package Patterns.ProxyPattern;

public class Main {
    public static void main(String[] args) {
        EmployeeDaoImpl employeeDaoUser = new EmployeeDaoImpl();

        EmployeeDaoProxy employeeDaoProxy = new EmployeeDaoProxy(employeeDaoUser);
        try{
            employeeDaoProxy.readData("USER","Ashish");
            employeeDaoProxy.writeData("ADMIN","Harry");
            employeeDaoProxy.writeData("USER", "RON");
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }
}

/*
READ INFO FOR EMPLOYEE: Ashish
UPDATED INFO FOR EMPLOYEE: Harry
java.lang.Exception: USER RON DOESNT HAVE WRITE ACCESS
	at Patterns.ProxyPattern.EmployeeDaoProxy.writeData(EmployeeDaoProxy.java:38)
	at Patterns.ProxyPattern.Main.main(Main.java:11)

 */