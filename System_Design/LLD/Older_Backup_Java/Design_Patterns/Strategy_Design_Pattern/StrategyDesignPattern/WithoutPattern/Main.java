package StrategyDesignPattern.WithoutPattern;

public class Main {
    public static void main(String[] args) {
        // WITH STRATEGY
        OffRoadVehicle offRoadVehicle = new OffRoadVehicle();
        PassengerVehicle passengerVehicle = new PassengerVehicle();

        offRoadVehicle.drive();
        passengerVehicle.drive();

    }
}