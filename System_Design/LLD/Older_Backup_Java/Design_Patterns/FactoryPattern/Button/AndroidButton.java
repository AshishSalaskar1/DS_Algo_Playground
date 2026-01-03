package FactoryPattern.Button;

public class AndroidButton implements Button{
    @Override
    public void render() {
        System.out.println("<HTML_BUTTON> Click here <HTML_BUTTON>");
    }

    @Override
    public void oncliick() {
        System.out.println("HTML Button clicked");
    }
}
