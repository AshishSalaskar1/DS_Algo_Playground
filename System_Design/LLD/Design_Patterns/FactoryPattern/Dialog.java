package FactoryPattern;

import FactoryPattern.Button.Button;

public abstract class Dialog {
    public abstract Button createButton();

    public void renderDialog(){
        System.out.println("CODE FOR RENDERING DIALOG...");
        createButton().render();
    }
}
