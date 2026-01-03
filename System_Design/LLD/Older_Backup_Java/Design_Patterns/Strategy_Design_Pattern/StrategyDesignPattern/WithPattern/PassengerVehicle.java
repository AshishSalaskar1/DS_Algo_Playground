package StrategyDesignPattern.WithPattern;

import StrategyDesignPattern.WithPattern.Strategy.AllWheelDriveStrategy;

public class PassengerVehicle extends Vehicle {
    public PassengerVehicle(){
        super(new AllWheelDriveStrategy());
    }
}
