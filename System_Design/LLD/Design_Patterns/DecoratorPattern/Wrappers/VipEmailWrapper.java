package DecoratorPattern.Wrappers;

import DecoratorPattern.Notifier;

public class VipEmailWrapper extends EmailWrapper{
    private EmailWrapper emailWrapper;
    public VipEmailWrapper(EmailWrapper emailWrapper) {
        super(emailWrapper.notifier);
        this.emailWrapper = emailWrapper;
    }

    @Override
    public void notifyOthers() {
        System.out.println("NOTIFYING SPECIAL VIP EMAILS.....");
        emailWrapper.notifyOthers(); // call notify of EmailWrapper
    }
}
