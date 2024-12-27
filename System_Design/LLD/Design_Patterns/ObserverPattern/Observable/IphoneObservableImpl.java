package ObserverPattern.Observable;

import ObserverPattern.Observer.NotificationAlertObserver;

import java.util.ArrayList;
import java.util.List;

public class IphoneObservableImpl implements StockObservable{

    List<NotificationAlertObserver> subscribers;
    int stockCount = 0;
    public String name;


    public IphoneObservableImpl(){
        this.subscribers = new ArrayList<>();
        this.stockCount = 0;
        this.name = "Iphone_16_Pro_Max";
    }

    @Override
    public void subscribe(NotificationAlertObserver observer) {
        System.out.println("IPHONE PUBLISHER => Added new subscriber : "+ observer.getClass().getName());
        this.subscribers.add(observer);
    }

    @Override
    public void unsubscribe(NotificationAlertObserver observer) {
        System.out.println("IPHONE PUBLISHER => Removed subscriber : "+ observer.getClass().getName());
        this.subscribers.remove(observer);
    }

    @Override
    public void notifySubscribers() {
        for(NotificationAlertObserver subscriber: this.subscribers){
            subscriber.update(this);
        }
    }

    @Override
    public void setStockCount(int stockIncrement) {
        this.stockCount += stockIncrement;
        System.out.println("IPHONE PUBLISHER => Updated the stocks for "+this.name);
        notifySubscribers();
    }

    @Override
    public int getStockCount() {
        return this.stockCount;
    }

    @Override
    public String getProductName() {
        return this.name;
    }
}
