class Solution {
    public String solution(String newId) {
        return new KakaoId(newId)
                .replaceToLowerCase()
                .filter()
                .toSingleDot()
                .noStartEndDot()
                .noBlank()
                .noGreaterThan16()
                .noLessThan2()
                .getResult();
    }

    private static class KakaoId {
        private String s;

        KakaoId(String s) {
            this.s = s;
        }

        private KakaoId replaceToLowerCase() {
            s = s.toLowerCase();
            return this;
        }

        private KakaoId filter() {
            s = s.replaceAll("[^a-z0-9._-]","");
            return this;
        }
        
        private KakaoId toSingleDot() {
            s = s.replaceAll("[.]{2,}",".");
            return this;
        }
        
        private KakaoId noStartEndDot() {
            s = s.replaceAll("^\\.|\\.$","");
            return this;
        }
        
        private KakaoId noBlank() {
            s = s.isEmpty() ? "a" : s;
            return this;
        }
        
        private KakaoId noGreaterThan16() {
            if (16 <= s.length()) {
                s = s.substring(0, 15);
                s = s.replaceAll("[.]$","");
            }
            return this;
        }
        
        private KakaoId noLessThan2() {
            while (s.length() < 3) {
                s += s.charAt(s.length() - 1);
            }
            return this;
        }
        
        private String getResult() {
            return s;
        }
    }
}