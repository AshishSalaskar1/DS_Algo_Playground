package StrategyDesignPattern.WithPattern.Strategy;

public class OffRoadDriveStrategy implements DriveStrategy{
    @Override
    public void drive() {
        System.out.println("This uses OFF-ROAD drive capability");
    }
}
