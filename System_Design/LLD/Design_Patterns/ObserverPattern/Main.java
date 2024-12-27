package ObserverPattern;

import ObserverPattern.Observable.IphoneObservableImpl;
import ObserverPattern.Observer.EmailAlertObserver;
import ObserverPattern.Observer.PhoneAlertObserver;

public class Main {
    public static void main(String[] args) {

        EmailAlertObserver emailAlertObserver = new EmailAlertObserver();
        PhoneAlertObserver phoneAlertObserver = new PhoneAlertObserver();

        IphoneObservableImpl iphoneObservable = new IphoneObservableImpl();

        // subscribe to the publisher
        iphoneObservable.subscribe(emailAlertObserver);
        iphoneObservable.subscribe(phoneAlertObserver);

        iphoneObservable.setStockCount(10);
        iphoneObservable.setStockCount(1);

        // Unsubscribe the PhoneAlert from the publisher
        iphoneObservable.unsubscribe(phoneAlertObserver);

        iphoneObservable.setStockCount(10);

    }
}

/*
OUTPUT:

IPHONE PUBLISHER => Added new subscriber : ObserverPattern.Observer.EmailAlertObserver
IPHONE PUBLISHER => Added new subscriber : ObserverPattern.Observer.PhoneAlertObserver
IPHONE PUBLISHER => Updated the stocks for Iphone_16_Pro_Max
EMAIL ALERT SUBSCRIBER => The count of Iphone_16_Pro_Max is 10 was notified to EMAIL ALERTER
PHONE ALERT SUBSCRIBER => The count of Iphone_16_Pro_Max is 10 was notified to PHONE ALERTER
IPHONE PUBLISHER => Updated the stocks for Iphone_16_Pro_Max
EMAIL ALERT SUBSCRIBER => The count of Iphone_16_Pro_Max is 11 was notified to EMAIL ALERTER
PHONE ALERT SUBSCRIBER => The count of Iphone_16_Pro_Max is 11 was notified to PHONE ALERTER
IPHONE PUBLISHER => Removed subscriber : ObserverPattern.Observer.PhoneAlertObserver
IPHONE PUBLISHER => Updated the stocks for Iphone_16_Pro_Max
EMAIL ALERT SUBSCRIBER => The count of Iphone_16_Pro_Max is 21 was notified to EMAIL ALERTER

 */
