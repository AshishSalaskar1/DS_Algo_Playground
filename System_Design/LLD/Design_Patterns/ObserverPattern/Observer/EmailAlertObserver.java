package ObserverPattern.Observer;

import ObserverPattern.Observable.StockObservable;

public class EmailAlertObserver implements NotificationAlertObserver{
    @Override
    public void update(StockObservable publisher) {
        System.out.println("EMAIL ALERT SUBSCRIBER => The count of " + publisher.getProductName() + " is " + publisher.getStockCount()+" was notified to EMAIL ALERTER");
    }
}
