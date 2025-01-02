package Patterns.ProxyPattern;

public class EmployeeDaoProxy implements EmployeeDao{
    EmployeeDao employeeDaoObject;

    EmployeeDaoProxy(EmployeeDao employeeDaoObject){
        this.employeeDaoObject = employeeDaoObject;
    }

    private boolean checkAccess(String role, String operation){
        if(operation.equals("READ")){
            return true;
        }

        if (operation.equals("WRITE") && role.equals("ADMIN")){
            return true;
        }

        return false;
    }

    @Override
    public void readData(String client, String emp) throws Exception {
        if(this.checkAccess(client, "READ")){
          this.employeeDaoObject.readData(client, emp);
        }
        else{
            throw new Exception("USER "+emp+" DOESNT HAVE READ ACCESS");
        }
    }

    @Override
    public void writeData(String client, String emp) throws Exception {
        if(this.checkAccess(client, "WRITE")){
            this.employeeDaoObject.writeData(client, emp);
        }
        else{
            throw new Exception("USER "+emp+" DOESNT HAVE WRITE ACCESS");
        }
    }
}
