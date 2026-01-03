package DecoratorPattern.Wrappers;

import DecoratorPattern.Notifier;

public class PhoneWrapper extends NotifierWrapper{
    public PhoneWrapper(Notifier notifier) {
        super(notifier);
    }

    @Override
    public void notifyOthers() {
        System.out.println("NOTIFYING VIA PHONE STEPS...");
        this.notifier.notifyOthers();
    }
}
