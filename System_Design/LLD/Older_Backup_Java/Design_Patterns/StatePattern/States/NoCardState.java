package Patterns.StatePattern.States;

import Patterns.StatePattern.ATMMachine;

public class NoCardState implements ATMState {
    private ATMMachine atm;

    public NoCardState(ATMMachine atm) {
        this.atm = atm;
    }

    @Override
    public void insertCard() {
        System.out.println("Card inserted.");
        atm.setState(atm.getHasCardState());
    }

    @Override
    public void ejectCard() {
        System.out.println("No card to eject.");
    }

    @Override
    public void enterPin(int pin) {
        System.out.println("Insert a card first.");
    }

    @Override
    public void withdrawCash(int amount) {
        System.out.println("Insert a card first.");
    }
}