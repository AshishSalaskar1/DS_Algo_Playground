package ChainOfResponsibilityPattern;

public class InfoLogProcessor extends LogProcessor{

    InfoLogProcessor(LogProcessor nextLogProcessor){
        super(nextLogProcessor);
    }

    @Override
    public void log(String logLevel, String message) {
        if(logLevel.equals(INFO)){
            System.out.println("INFO: "+ message);
        }
        else if(super.nextLogProcessor == null){
            System.out.println("NO HANDLERS LEFT TO HANDLE REQUEST");
        }
        else{
            super.nextLogProcessor.log(logLevel, message);
        }
    }
}
