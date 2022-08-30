package java;

import java.io.File;
import java.util.HashMap;
import java.util.Scanner;

public class ValidAnagram {
    public static void main(String args[]){
        File file = new File("ValidAnagramText.txt");
        Scanner sc = new Scanner(file);
        String input;
        while (sc.hasNextLine()){
            String input = input + sc.nextLine();
        }
        isAnagram()
    }

    public static boolean isAnagram(String args[]) {
        if (s.length() != t.length()) {

            return false;
        }
        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);
            sMap.put(sChar, sMap.getOrDefault(sChar, 0) + 1);
            tMap.put(tChar, tMap.getOrDefault(tChar, 0) + 1);
        }
        for (var entry : sMap.entrySet()) {
            if (entry.getValue() != tMap.getOrDefault(entry.getKey(), 0)) {
                System.out.println(
                        "key: " + entry.getKey() + entry.getValue() + " " + tMap.getOrDefault(entry.getKey(), 0));
                return false;
            }
        }

        return true;
        return false;
    }
}}
