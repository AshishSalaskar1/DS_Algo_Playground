package Patterns.ProxyPattern;

public interface EmployeeDao {
    public void readData(String client, String emp) throws Exception;
    public void writeData(String client, String emp) throws Exception;
}
