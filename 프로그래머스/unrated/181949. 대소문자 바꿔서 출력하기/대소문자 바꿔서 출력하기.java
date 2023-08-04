import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String res = "";
        int tmp;
        
        for(int i = 0; i<a.length(); i++){
            tmp = (int)a.charAt(i);
            if((65 <= tmp) && (tmp <= 90)){
                res += (char)(tmp + 32);
            } else{
                res += (char)(tmp-32);
            }
        }
        
        System.out.println(res);
    }
}