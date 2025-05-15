public class ValidPalindrome {
    public static boolean isPalindrome(String word) {
        int left = 0;
        int right = word.length() - 1;
        while(left < right) {
            if(word.charAt(left) == word.charAt(right)) {
                left++;
                right--;
            }
            else {
                return false;
            }
        }
        return true;
    }
    public static void main(String[]args) {
        System.out.println(isPalindrome("racecar"));
		System.out.println(isPalindrome("madam"));
        System.out.println(isPalindrome("noon"));
        System.out.println(isPalindrome("soon"));
    }
}
