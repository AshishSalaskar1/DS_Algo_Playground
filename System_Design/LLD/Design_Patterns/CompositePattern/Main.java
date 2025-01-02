package Patterns.CompositePattern;

public class Main {
    public static void main(String[] args) {
        Directory root = new Directory("root");

        Directory docs = new Directory("documents");
        docs.add(new File("doc1.pdf"));docs.add(new File("doc2.pdf"));

        Directory apps = new Directory("applications");
        Directory mediaApps = new Directory("media_apps");
        mediaApps.add(new File("vlc.exe")); mediaApps.add(new File("kmp.exe"));
        Directory officeApps = new Directory("office_apps");
        officeApps.add(new File("slack.exe")); officeApps.add(new File("teams.exe"));

        apps.add(mediaApps);
        apps.add(officeApps);

        root.add(docs);
        root.add(apps);


        root.ls();
    }
}

/*
In the directory root
In the directory documents
Printing file name: doc1.pdf
Printing file name: doc2.pdf
In the directory applications
In the directory media_apps
Printing file name: vlc.exe
Printing file name: kmp.exe
In the directory office_apps
Printing file name: slack.exe
Printing file name: teams.exe
 */