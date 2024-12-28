package DecoratorPattern;

import DecoratorPattern.Wrappers.EmailWrapper;
import DecoratorPattern.Wrappers.PhoneWrapper;
import DecoratorPattern.Wrappers.VipEmailWrapper;

public class Main {

    public static void startNotifying(Notifier notifier){
        notifier.notifyOthers();
    }
    public static void main(String[] args) {
        // Direct implementation of Notifier
        NotifierImpl notifier = new NotifierImpl();
        startNotifying(notifier);
        System.out.println("BASIC IMPLEMENTATION DONE...\n");

        // First level wrapper
        EmailWrapper emailWrapper = new EmailWrapper(new NotifierImpl());
        startNotifying(emailWrapper);

        PhoneWrapper phoneWrapper = new PhoneWrapper(new NotifierImpl());
        startNotifying(phoneWrapper);
        System.out.println("FIRST LEVEL WRAPPER DONE...\n");

        // second level wrapper
        VipEmailWrapper vipEmailWrapper = new VipEmailWrapper(new EmailWrapper(new NotifierImpl()));
        startNotifying(vipEmailWrapper);
    }
}

/*
NOTIFYING OTHER USERS...Normally
BASIC IMPLEMENTATION DONE...

NOTIFYING VIA EMAIL STEPS...
NOTIFYING OTHER USERS...Normally
NOTIFYING VIA PHONE STEPS...
NOTIFYING OTHER USERS...Normally
FIRST LEVEL WRAPPER DONE...

NOTIFYING SPECIAL VIP EMAILS.....
NOTIFYING VIA EMAIL STEPS...
NOTIFYING OTHER USERS...Normally

Process finished with exit code 0
 */