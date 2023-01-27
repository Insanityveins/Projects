import net.lingala.zip4j.core.*;
import net.lingala.zip4j.exception.*;

public class ZipCrackerSingleThread {

    public static void main(String[] args) {

        try {
            ZipFile zipFile = new ZipFile("./src/protected3.zip");
            long start = System.currentTimeMillis();
            findPassword3(zipFile);
            long end = System.currentTimeMillis();
            System.out.printf("It took %dms to crack the password.\n", (end - start));
        } catch (ZipException ze) {
            System.out.println("File not found.");
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public static void findPassword3(ZipFile zipFile) {
        // https://stackoverflow.com/questions/16282368/concatenate-chars-to-form-string-in-java
        // use string builder to build string out of chars
        StringBuilder sb = new StringBuilder();
        String password;

        char a;
        char b;
        char c;

        for (int i = 97; i < 123; i++) {
            a = (char) i;
            for (int j = 97; j < 123; j++) {
                b = (char) j;
                for (int k = 97; k < 123; k++) {
                    c = (char) k;
                    try {
                        password = sb.append(a).append(b).append(c).toString();
                        zipFile.setPassword(password);
                        zipFile.extractAll("protected3_contents");
                        System.out.println("The password was: " + password);
                        return;
                    } catch (ZipException ze) {
                        sb.delete(0, sb.length());
                    }
                }
            }
        }
    }

}
