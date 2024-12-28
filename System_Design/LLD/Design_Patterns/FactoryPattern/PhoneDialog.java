package FactoryPattern;

import FactoryPattern.Button.AndroidButton;
import FactoryPattern.Button.Button;

public class PhoneDialog extends Dialog{
    @Override
    public Button createButton() {
        // You can use switch to create what type of button you need also
        return new AndroidButton();
    }

}
