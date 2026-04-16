class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        
        // Length mismatch
        if (pattern.length() != words.length) {
            return false;
        }

        java.util.HashMap<Character, String> map1 = new java.util.HashMap<>();
        java.util.HashMap<String, Character> map2 = new java.util.HashMap<>();

        for (int i = 0; i < pattern.length(); i++) {
            char p = pattern.charAt(i);
            String w = words[i];

            // If mapping doesn't exist, create it
            if (!map1.containsKey(p) && !map2.containsKey(w)) {
                map1.put(p, w);
                map2.put(w, p);
            } 
            // Check consistency
            else {
                if (!w.equals(map1.get(p))) {
                    return false;
                }
            }
        }
        return true;
    }
}