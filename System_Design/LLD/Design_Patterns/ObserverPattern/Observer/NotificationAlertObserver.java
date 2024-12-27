package ObserverPattern.Observer;

import ObserverPattern.Observable.StockObservable;

public interface NotificationAlertObserver {
    public void update(StockObservable publisher);
}
