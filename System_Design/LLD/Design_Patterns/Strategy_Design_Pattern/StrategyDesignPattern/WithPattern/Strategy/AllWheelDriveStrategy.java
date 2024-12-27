package StrategyDesignPattern.WithPattern.Strategy;

public class AllWheelDriveStrategy implements DriveStrategy{
    @Override
    public void drive() {
        System.out.println("This uses ALL-WHEEL drive capability");
    }
}
