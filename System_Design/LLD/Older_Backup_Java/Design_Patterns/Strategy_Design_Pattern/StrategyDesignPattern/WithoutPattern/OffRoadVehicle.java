package StrategyDesignPattern.WithoutPattern;

public class OffRoadVehicle extends Vehicle{
    @Override
    public void drive() {
        System.out.println("This uses OFF-ROAD drive capability");
    }
}
