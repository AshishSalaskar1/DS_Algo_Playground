package FactoryPattern;

public class Main {
    public static void main(String[] args) {
        Dialog webDialog = new WebDialog();
        Dialog phoneDialog = new PhoneDialog();

        webDialog.renderDialog();
        phoneDialog.renderDialog();
    }
}

/*

CODE FOR RENDERING DIALOG...
<HTML_BUTTON> Click here <HTML_BUTTON>
CODE FOR RENDERING DIALOG...
<HTML_BUTTON> Click here <HTML_BUTTON>

 */