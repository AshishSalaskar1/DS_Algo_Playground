package StrategyDesignPattern.WithPattern;

import StrategyDesignPattern.WithPattern.Strategy.OffRoadDriveStrategy;

public class OffRoadVehicle extends Vehicle {
    public OffRoadVehicle(){
        super(new OffRoadDriveStrategy());
    }
}
