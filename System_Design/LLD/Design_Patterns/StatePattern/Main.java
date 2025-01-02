package Patterns.StatePattern;

public class Main {
    public static void main(String[] args) {
        ATMMachine atm = new ATMMachine(1000);

        atm.insertCard();
        atm.enterPin(1234);
        atm.withdrawCash(500);

        atm.insertCard();
        atm.enterPin(1234);
        atm.withdrawCash(600);

        atm.insertCard();
    }
}
