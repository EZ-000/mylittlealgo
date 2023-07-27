class Solution {
    public String solution(String myString, int num1, int num2) {
        StringBuilder answer = new StringBuilder();
        
        for (int index = 0; index < myString.length(); index++) {
            if (index == num1) answer.append(myString.charAt(num2));
            else if (index == num2) answer.append(myString.charAt(num1));
            else answer.append(myString.charAt(index));
        }
        return answer.toString();
    }
}