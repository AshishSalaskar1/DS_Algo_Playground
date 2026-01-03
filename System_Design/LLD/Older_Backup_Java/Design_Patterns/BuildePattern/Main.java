package Patterns.BuildePattern;


public class Main {
    public static void main(String[] args) {
        ComputerBuilder desktopBuilder = new DesktopComputerBuilder();
        ComputerDirector director = new ComputerDirector(desktopBuilder);
        Computer desktop = director.constructComputer();

        // Access the constructed Computer object
        System.out.println(desktop);
    }
}
