package DecoratorPattern.Wrappers;

import DecoratorPattern.Notifier;

public abstract class NotifierWrapper extends Notifier {
    Notifier notifier;

    public NotifierWrapper(Notifier notifier){
        this.notifier = notifier;
    }

    @Override
    public abstract void notifyOthers();
}
