package StrategyDesignPattern.WithoutPattern;

public class PassengerVehicle extends Vehicle{
    @Override
    public void drive() {
        System.out.println("This uses ALL-WHEEL drive capability");
    }
}
