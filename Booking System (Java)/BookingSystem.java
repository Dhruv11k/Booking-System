import java.io.*;
import java.util.Scanner;

class BookingSystem {

    static final String FILE_NAME = "bookings.txt";

    static void addBooking() throws IOException {
        Scanner sc = new Scanner(System.in);
        FileWriter fw = new FileWriter(FILE_NAME, true);

        System.out.print("Booking ID: ");
        String id = sc.nextLine();
        System.out.print("Customer Name: ");
        String name = sc.nextLine();
        System.out.print("Date (DD-MM-YYYY): ");
        String date = sc.nextLine();
        System.out.print("Time Slot: ");
        String time = sc.nextLine();

        fw.write(id + "," + name + "," + date + "," + time + "\n");
        fw.close();

        System.out.println("Booking added successfully!");
    }

    static void viewBookings() throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(FILE_NAME));
        String line;
        System.out.println("\n--- All Bookings ---");
        while ((line = br.readLine()) != null) {
            System.out.println(line);
        }
        br.close();
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n1. Add Booking\n2. View Bookings\n3. Exit");
            choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1 -> addBooking();
                case 2 -> viewBookings();
                case 3 -> System.out.println("Exiting...");
                default -> System.out.println("Invalid choice");
            }
        } while (choice != 3);
    }
}
