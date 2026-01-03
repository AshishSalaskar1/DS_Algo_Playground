package Patterns.StatePattern.States;

import Patterns.StatePattern.ATMMachine;

public class HasCardState implements ATMState {
    private ATMMachine atm;

    public HasCardState(ATMMachine atm) {
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
        if (pin == 1234) {
            System.out.println("PIN correct.");
            atm.setState(atm.getHasCorrectPinState());
        } else {
            System.out.println("Incorrect PIN.");
        }
    }

    @Override
    public void withdrawCash(int amount) {
        System.out.println("Enter PIN first.");
    }
}
