package ChainOfResponsibilityPattern;

public abstract class LogProcessor {
    public static String INFO = "info";
    public static String DEBUG = "debug";
    public static String ERROR = "error";

    LogProcessor nextLogProcessor;

    LogProcessor(LogProcessor nextLogProcessor){
        this.nextLogProcessor = nextLogProcessor;
    }

    public abstract void log(String logLevel, String message);
}
