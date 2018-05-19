import java.io.*;
import java.net.*;

public class Server {

	// Returns a String that is the reverse of the parameter s
	public static String reverse(String s) {
		String result = "";
		int length = s.length();

		for (int i = length - 1; i >= 0; i--) {
			result = result + s.charAt(i);
		}

		return result;
	}

	public static void main(String[] args) throws Exception {
		// Create server socket listening on port
		int port = 3333;
		ServerSocket serverSocket = new ServerSocket(port);

		// Declare client socket
		Socket clientSocket;

		while (true) { // Provide service continuously
			clientSocket = serverSocket.accept();

			ObjectOutputStream out = new ObjectOutputStream(clientSocket.getOutputStream());
			ObjectInputStream in = new ObjectInputStream(clientSocket.getInputStream());

			String s = (String) in.readObject();

			String result = reverse(s);

			out.writeObject(result);
			out.flush();
			
			out.close();
			in.close();
			clientSocket.close();
		}
	}

}
