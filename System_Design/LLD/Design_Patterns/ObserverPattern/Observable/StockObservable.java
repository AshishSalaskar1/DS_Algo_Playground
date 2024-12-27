package ObserverPattern.Observable;

import ObserverPattern.Observer.NotificationAlertObserver;

public interface StockObservable {
    public void subscribe(NotificationAlertObserver observer);

    public void unsubscribe(NotificationAlertObserver observer);

    public void notifySubscribers();

    public void setStockCount(int stockIncrement);

    public int getStockCount();

    public String getProductName();
}
