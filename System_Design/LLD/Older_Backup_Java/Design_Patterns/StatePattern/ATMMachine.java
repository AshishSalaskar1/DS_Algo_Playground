package Patterns.StatePattern;

import Patterns.StatePattern.States.*;

public class ATMMachine {
    private ATMState noCardState;
    private ATMState hasCardState;
    private ATMState hasCorrectPinState;
    private ATMState outOfCashState;

    private ATMState currentState;
    private int cash;

    public ATMMachine(int cash) {
        this.cash = cash;

        noCardState = new NoCardState(this);
        hasCardState = new HasCardState(this);
        hasCorrectPinState = new HasCorrectPinState(this);
        outOfCashState = new OutOfCashState(this);

        // Initial State -> either noCard or outOfCash state
        currentState = (cash > 0) ? noCardState : outOfCashState;
    }

    public void insertCard() {
        currentState.insertCard();
    }

    public void ejectCard() {
        currentState.ejectCard();
    }

    public void enterPin(int pin) {
        currentState.enterPin(pin);
    }

    public void withdrawCash(int amount) {
        currentState.withdrawCash(amount);
    }

    // Getters and Setters for states and cash
    public void setState(ATMState state) {
        currentState = state;
    }

    public ATMState getNoCardState() {
        return noCardState;
    }

    public ATMState getHasCardState() {
        return hasCardState;
    }

    public ATMState getHasCorrectPinState() {
        return hasCorrectPinState;
    }

    public ATMState getOutOfCashState() {
        return outOfCashState;
    }

    public int getCash() {
        return cash;
    }

    public void setCash(int cash) {
        this.cash = cash;
    }
}