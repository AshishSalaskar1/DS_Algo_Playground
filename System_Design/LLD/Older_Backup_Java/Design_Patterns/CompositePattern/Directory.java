package Patterns.CompositePattern;

import java.util.ArrayList;
import java.util.List;

public class Directory implements FileSystem{
    private List<FileSystem> fileSystemList;
    private String directoryName;

    public Directory(String name){
        this.directoryName = name;
        this.fileSystemList = new ArrayList<>();
    }

    public void add(FileSystem fs){
        this.fileSystemList.add(fs);
    }

    @Override
    public void ls() {
        System.out.println("In the directory "+this.directoryName);
        for(FileSystem fs: this.fileSystemList){
            fs.ls();
        }
    }
}
