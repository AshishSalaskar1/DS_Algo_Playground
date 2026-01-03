package ChainOfResponsibilityPattern;

public class DebugLogProcessor extends LogProcessor{

    DebugLogProcessor(LogProcessor nextLogProcessor){
        super(nextLogProcessor);
    }

    @Override
    public void log(String logLevel, String message) {
        if(logLevel.equals(DEBUG)){
            System.out.println("DEBUG: "+ message);
        }
        else if(super.nextLogProcessor == null){
            System.out.println("NO HANDLERS LEFT TO HANDLE REQUEST");
        }
        else{
            super.nextLogProcessor.log(logLevel, message);
        }
    }
}
