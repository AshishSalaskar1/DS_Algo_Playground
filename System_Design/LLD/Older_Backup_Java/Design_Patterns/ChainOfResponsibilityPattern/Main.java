package ChainOfResponsibilityPattern;

public class Main {
    public static void main(String[] args) {
        LogProcessor logProcessor = new ErrorLogProcessor(new InfoLogProcessor(new DebugLogProcessor(null)));

        logProcessor.log("error","This is an error message which is being printed");
        logProcessor.log("info","This is an info message which is being printed");
        logProcessor.log("debug","This is an debug message which is being printed");

        logProcessor.log("ashish","This is an debug message which is being printed");
    }
}

/*

ERROR: This is an error message which is being printed
INFO: This is an info message which is being printed
DEBUG: This is an debug message which is being printed
NO HANDLERS LEFT TO HANDLE REQUEST

 */