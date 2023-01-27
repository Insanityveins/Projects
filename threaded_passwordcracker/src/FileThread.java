import net.lingala.zip4j.core.ZipFile;
import net.lingala.zip4j.exception.ZipException;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class FileThread extends Thread {

    private ZipFile zipFile;
    private String fileName;
    private int start;
    private int end;
    private boolean foundPassword = false;

    public FileThread(ZipFile zipFile, String fileName, int start, int end) {
        this.zipFile = zipFile;
        this.fileName = fileName;
        this.start = start;
        this.end = end;
    }

    public synchronized void run() {
        // https://stackoverflow.com/questions/16282368/concatenate-chars-to-form-string-in-java
        // use string builder to build string out of chars
        StringBuilder sb = new StringBuilder();
        String password;

        // use characters to iterate through lower case letters
        // to concatenate them together
        char a;
        char b;
        char c;
        char d;
        char e;

        // start to end on first char to limit
        // i.e. a-d
        // rest of char should be a-z to loop through all possible passwords
        for (int i = start; i <= end; i++) {
            a = (char) i;
            for (int j = 97; j < 123; j++) {
                b = (char) j;
                for (int k = 97; k < 123; k++) {
                    c = (char) k;
                    for (int l = 97; l < 123; l++) {
                        d = (char) l;
                        for (int m = 97; m < 123; m++) {
                            e = (char) m;
                            password = sb.append(a).append(b).append(c).append(d).append(e).toString();
                            try {
                                zipFile.setPassword(password);
                                zipFile.extractAll(fileName + "_contents");
                                foundPassword = true;
                                System.out.println("The password was: " + password);
                                return;
                            } catch (ZipException ze) {
                                if (this.isInterrupted()) return;
                                sb.delete(0, sb.length());
                            }

                        }
                    }
                }
            }
        }

        System.out.println("Couldn't find the password.");
    }

    public boolean isFoundPassword() {
        return foundPassword;
    }

    public void deleteFile() {
        try {
            // "./src/" needed to get to folder of file
            Files.delete(Path.of("./src/" + fileName));
            if (this.isInterrupted() && !foundPassword) {
                Files.delete(Path.of(fileName + "_contents/message.txt"));
                Files.delete(Path.of(fileName + "_contents"));
            }
        } catch (IOException ie) {
            System.out.println("Couldn't delete the file.");
            System.out.println(ie);
        }
    }

    @Override
    public String toString() {
        return String.format("This thread is responsible for %c to %c", (char)start, (char)end);
    }
}
