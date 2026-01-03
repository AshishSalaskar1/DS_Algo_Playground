package Patterns.StatePattern.States;

import Patterns.StatePattern.ATMMachine;

public class OutOfCashState implements ATMState {
    private ATMMachine atm;

    public OutOfCashState(ATMMachine atm) {
        this.atm = atm;
    }

    @Override
    public void insertCard() {
        System.out.println("Machine out of cash.");
    }

    @Override
    public void ejectCard() {
        System.out.println("Machine out of cash.");
    }

    @Override
    public void enterPin(int pin) {
        System.out.println("Machine out of cash.");
    }

    @Override
    public void withdrawCash(int amount) {
        System.out.println("Machine out of cash.");
    }
}
