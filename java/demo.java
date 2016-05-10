import java.util.regex.Matcher;
import java.util.regex.Pattern;

class demo {
	public static void main(String[] args) {
		/*
		String str1 = "123time=12:12:12dasda";	
	
		Pattern timePattern = Pattern.compile("[a-z]");
		
		Matcher m = timePattern.matcher(str1);
		// System.out.println(m.matches());
		
		System.out.println(str1.findAll("\\d+"));
		*/
		
		Pattern p = Pattern.compile("time=(\\d{2}:\\d{2}:\\d{2}\\.\\d{2})");
        String s = "dasdtime=13:23:31.12";
        Matcher m = p.matcher(s);
		
        while(m.find()){
            System.out.println(m.group());
			
        }
		
	
	}
}

