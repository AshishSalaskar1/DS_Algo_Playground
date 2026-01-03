package DecoratorPattern;

public class NotifierImpl extends Notifier {

    @Override
    public void notifyOthers() {
        System.out.println("NOTIFYING OTHER USERS...Normally");
    }
}
