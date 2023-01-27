import java.util.ArrayList;

public class ThreadChecker extends Thread{

    private ArrayList<FileThread> threads;

    public ThreadChecker(ArrayList<FileThread> threads) {
        this.threads = threads;
    }

    @Override
    public synchronized void run() {
        // wait for a thread to signal it's done
        // stop all threads and clean up

        boolean finished = false;

        while (!finished) {
            for (FileThread t : threads) {
                if (t.isFoundPassword()) {
                    stopThreads();
                    finished = true;
                } else {
                    try {
                        sleep(500);
                    } catch (InterruptedException e) {
                        System.out.println(e);
                    }
                }
            }
        }

        System.out.println("Cleaning up extra files.");
        for (FileThread t : threads) t.deleteFile();
    }
    public void stopThreads() {
        for (FileThread t: threads) t.interrupt();
    }
}
