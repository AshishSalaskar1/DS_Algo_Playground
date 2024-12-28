package FactoryPattern;

import FactoryPattern.Button.Button;
import FactoryPattern.Button.HtmlButton;

public class WebDialog extends Dialog{
    @Override
    public Button createButton() {
        return new HtmlButton();
    }
}
