package StrategyDesignPattern.WithPattern;

import StrategyDesignPattern.WithPattern.Strategy.AllWheelDriveStrategy;

public class SportsVehicle extends Vehicle {
    public SportsVehicle(){
        super(new AllWheelDriveStrategy());
    }
}
