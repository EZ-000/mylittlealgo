class Solution {
    private double getSlope(double x1, double y1, double x2, double y2) {
        return (y1 - y2) / (x1 - x2);
    }
    
    public int solution(int[][] dots) {
        int answer = 0;
        
        double[] slopes = new double[6];
        int index = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = i + 1; j < 4; j++) {
                double x1 = dots[i][0];
                double y1 = dots[i][1];
                double x2 = dots[j][0];
                double y2 = dots[j][1];
                slopes[index] = getSlope(x1, y1, x2, y2);
                index++;
            }
        }
        
        for (int i = 0; i < 3; i++) {
            if (slopes[i] == slopes[5 - i]) {
                answer = 1;
                break;
            }
        }
        
        return answer;
    }
}