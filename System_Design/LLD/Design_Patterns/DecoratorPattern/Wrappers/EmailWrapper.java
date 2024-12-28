package DecoratorPattern.Wrappers;

import DecoratorPattern.Notifier;

public class EmailWrapper extends NotifierWrapper{
    public EmailWrapper(Notifier notifier) {
        super(notifier);
    }

    @Override
    public void notifyOthers() {
        System.out.println("NOTIFYING VIA EMAIL STEPS...");
        this.notifier.notifyOthers();
    }
}
