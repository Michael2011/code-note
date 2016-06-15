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
		
		
		Pattern p = Pattern.compile("(\"qualities\":)(.*)(,\"reporting\")");
        String s = "\"qualities\":{\"auto\":[{\"typ:},\"reporting\"";
		*/
	
		// Pattern p = Pattern.compile("[\'\"](http.*\\.mp3.*?)[\'\"]");
		// Pattern p = Pattern.compile("<title>(.*?)</title>");
        // String s = "<title>Little Girl Says Her Final Goodbyes To Her Favorite Toilet - Video Dailymotion</title>";


		// vimeo.com
		Pattern p = Pattern.compile("\"config_url\":\"(.*?)\"");
		String s = "player\":{\"config_url\":\"https://player.vimeo.com/video/145937066/config?autoplay=0&byline=0&collections=1&context=Vimeo%5CController%5CClipController.main_beta&default_to_hd=1&outro=beginning&portrait=0&share=1&title=0&watch_trailer=0&s=8e5d54c0e7ab0368e56465c8f9709aa9402db7d6_1466060636\",";

        Matcher m = p.matcher(s);
        while(m.find()){
            System.out.println(m.group(1));
			
        }
		
	
	}
}

