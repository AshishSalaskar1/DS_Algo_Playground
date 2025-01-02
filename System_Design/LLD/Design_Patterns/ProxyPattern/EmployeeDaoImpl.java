package Patterns.ProxyPattern;

public class EmployeeDaoImpl implements EmployeeDao{
    @Override
    public void readData(String client, String emp) throws Exception {
        System.out.println("READ INFO FOR EMPLOYEE: "+emp);
    }

    @Override
    public void writeData(String client, String emp) throws Exception {
        System.out.println("UPDATED INFO FOR EMPLOYEE: "+emp);
    }
}
