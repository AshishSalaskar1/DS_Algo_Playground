package ObserverPattern.Observer;

import ObserverPattern.Observable.StockObservable;

public class PhoneAlertObserver implements NotificationAlertObserver{
    @Override
    public void update(StockObservable publisher) {
        System.out.println("PHONE ALERT SUBSCRIBER => The count of "+ publisher.getProductName() + " is " + publisher.getStockCount()+" was notified to PHONE ALERTER");
    }
}
