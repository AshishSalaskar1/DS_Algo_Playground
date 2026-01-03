package StrategyDesignPattern.WithPattern;

import StrategyDesignPattern.WithPattern.Strategy.DriveStrategy;

public class Vehicle {

    DriveStrategy driveStrategy;

    public Vehicle(DriveStrategy ds){
        this.driveStrategy = ds;
    }

    public void drive(){
        this.driveStrategy.drive();
    }
}
