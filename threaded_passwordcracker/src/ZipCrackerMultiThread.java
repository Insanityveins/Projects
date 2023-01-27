import net.lingala.zip4j.core.*;
import net.lingala.zip4j.exception.*;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;

public class ZipCrackerMultiThread {

    public static void main(String[] args) throws InterruptedException {

        long start = System.currentTimeMillis();

        try {
            ZipFile zipFile5 = new ZipFile("./src/protected5.zip");

            int numThreads = 6;
            int letterChunk = 26 / numThreads; // num of letters in alphabet
            //ArrayList<FileThread> threads = new ArrayList<>();
            ArrayList<FileThread> threads = new ArrayList<>();

            File src;
            File dest;
            for (int i = 0; i < numThreads - 1; i++) {
                // start adding threads to the list of threads
                // give them a range of letters to be in charge of
                try {
                    src = new File("./src/protected5.zip");
                    dest = new File("./src/protected5_" + (i + 1) + ".zip");
                    Files.copy((src.toPath()), (dest.toPath()));
                    threads.add(new FileThread(new ZipFile(dest), dest.getName(), (i * letterChunk + 97), (i + 1) * letterChunk + 96));
                } catch (IOException ie) {
                    System.out.println("Couldn't get those copies for you boss man.");
                    System.exit(0);
                }
            }
            // add the last thread
            // *use numThreads for right file number
            try {
                src = new File("./src/protected5.zip");
                dest = new File("./src/protected5_" + (numThreads) + ".zip");
                Files.copy((src.toPath()), (dest.toPath()));
                threads.add(new FileThread(new ZipFile(dest), dest.getName(), ((numThreads - 1) * letterChunk + 97), 122));
            } catch (IOException ie2) {
                System.out.println("Copies either couldn't be made, or already exists.");
            }

            // ThreadChecker to see when password cracking is done
            ThreadChecker checker = new ThreadChecker(threads);
            checker.start();

            for (FileThread t : threads) t.start();
            for (FileThread t : threads) System.out.println(t);;

            // main try-catch
        } catch (ZipException ze3) {
            System.out.println("File not found");
        }
    }
}