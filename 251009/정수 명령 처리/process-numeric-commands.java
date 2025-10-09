import java.io.*;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        Stack<Integer> s = new Stack<>();

        while (n-- > 0) {
            String cmd = br.readLine();
            if (cmd.startsWith("push ")) {
                int num = Integer.parseInt(cmd.substring(5));
                s.push(num);
            } else if (cmd.startsWith("pop")) {
                sb.append(s.pop()).append("\n");
            } else if (cmd.startsWith("size")) {
                sb.append(s.size()).append("\n");
            } else if (cmd.startsWith("empty")) {
                sb.append(s.isEmpty() ? 1 : 0).append("\n");
            } else if (cmd.startsWith("top")) {
                sb.append(s.peek()).append("\n");
            }
        }
        System.out.println(sb);

    }
}