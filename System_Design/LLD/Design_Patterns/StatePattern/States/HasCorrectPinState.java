package Patterns.StatePattern.States;

import Patterns.StatePattern.ATMMachine;

public class HasCorrectPinState implements ATMState {
    private ATMMachine atm;

    public HasCorrectPinState(ATMMachine atm) {
        this.atm = atm;
    }

    @Override
    public void insertCard() {
        System.out.println("Card already inserted.");
    }

    @Override
    public void ejectCard() {
        System.out.println("Card ejected.");
        atm.setState(atm.getNoCardState());
    }

    @Override
    public void enterPin(int pin) {
        System.out.println("PIN already entered.");
    }

    @Override
    public void withdrawCash(int amount) {
        if (atm.getCash() >= amount) {
            System.out.println("Cash dispensed: " + amount);
            atm.setCash(atm.getCash() - amount);

            if (atm.getCash() == 0) {
                atm.setState(atm.getOutOfCashState());
            } else {
                atm.setState(atm.getNoCardState());
            }
        } else {
            System.out.println("Not enough cash.");
            atm.setState(atm.getNoCardState());
        }
    }
}