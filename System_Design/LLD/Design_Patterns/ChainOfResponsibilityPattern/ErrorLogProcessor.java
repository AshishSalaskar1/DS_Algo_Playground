package ChainOfResponsibilityPattern;

public class ErrorLogProcessor extends LogProcessor{

    ErrorLogProcessor(LogProcessor nextLogProcessor){
        super(nextLogProcessor);
    }

    @Override
    public void log(String logLevel, String message) {
        if(logLevel.equals(ERROR)){
            System.out.println("ERROR: "+ message);
        }
        else if(super.nextLogProcessor == null){
            System.out.println("NO HANDLERS LEFT TO HANDLE REQUEST");
        }
        else{
            super.nextLogProcessor.log(logLevel, message);
        }
    }
}
