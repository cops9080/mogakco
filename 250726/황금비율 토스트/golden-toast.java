import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        LinkedList<Character> l = new LinkedList<>();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        String s = br.readLine();
        
        for (int i=0; i<s.length(); i++) {
            l.add(s.charAt(i));
        }

        ListIterator<Character> it = l.listIterator(l.size());

        for (int i = 0; i < m; i++) {
            String command = br.readLine();
            
            if (command.equals("L")) {
                if (it.hasPrevious()) {
                    it.previous();
                }
            }
            if (command.equals("R")) {
                if (it.hasNext()) {
                    it.next();
                }
            }
            if (command.equals("D")) {
                if (it.hasNext()) {
                    it.next();
                    it.remove();   
                }
            }
            if (command.startsWith("P")) {
                char sP = command.charAt(2);
                it.add(sP);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (char c : l) {
            sb.append(c);
        }
        System.out.println(sb.toString());
        
    }
}