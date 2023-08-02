import java.util.Arrays;

class Solution {
    public String solution(String polynomial) {
        String[] terms = polynomial.split("\\s\\+\\s");
        int coefficient = 0;
        int constant = 0;
        for (String term : terms) {
            if (term.charAt(term.length() - 1) == 'x') {
                String k = term.substring(0, term.length() - 1);
                coefficient = (k.equals("")) ? coefficient + 1 : coefficient + Integer.parseInt(k);
            } else constant += Integer.parseInt(term);
        }
        
        String answer = "";
        if (coefficient != 0 & constant != 0) {
            answer = (coefficient == 1) ? "x + " + constant : coefficient + "x + " + constant;
        }
        else if (coefficient != 0 & constant == 0) {
            answer = (coefficient == 1) ? "x" : coefficient + "x";
        }
        else if (coefficient == 0 & constant != 0) answer = String.valueOf(constant);
        else answer = "0";
        
        return answer;
    }
}