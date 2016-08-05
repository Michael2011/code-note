import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class demo {
	public static void main(String[] args) {
		/*
		String str1 = "123time=12:12:12dasda";	
	
		Pattern timePattern = Pattern.compile("[a-z]");
		
		Matcher m = timePattern.matcher(str1);
		// System.out.println(m.matches());
		
		System.out.println(str1.findAll("\\d+"));
		*/		
		
		// Pattern p = Pattern.compile("(\"qualities\":)(.*)(,\"reporting\")");
        // String s = "\"qualities\":{\"auto\":[{\"typ:},\"reporting\"";
	
		// common regular
		// Pattern p = Pattern.compile("(http(.*?\\.[mp3|mp4|flv])(\\?)?(.*?))[\'\"]");
		// Pattern p = Pattern.compile("http[^\\s\"\'\\?]*\\.(mp3|mp4|flv)[^\\s\"\'>]*");

		// String s = "     <img src=\"http://static.4shared.com/images/no-cover-d1-music.png?ver=-1418850330\" class=\"jsTooltipCoverUrl jsSrcNoCover\" alt=\"\" no-cover=\"http://static.4shared.com/images/no-cover-d1-music.png?ver=-1418850330\"/>        </div>      </div>      <div id=\"d1_playPauseButton\" class=\"musicPlay\"></div>      <div id=\"d1_progressBarContainer\" class=\"musicWaveformHolder jsD1WaveForm\" data-url=\"http://dc372.4shared.com/img/V2kgaWQNce/b1019eac/dlink__2Fdownload_2FV2kgaWQNce_2FCL_5F-_5FHello_5FBitches.mp3?_3Fsbsr_3Da47fc8f2a33259d0006f04b46bd47117977_26lgfp_3D1000/preview.waveform\">        <div class=\"progressHover\"></div>  <div class=\"progressCurrent\"></div>  </div>   <div class=\"jsD1Artist\" style=\"display:none\">CL</div>                <input type=\"hidden\" class=\"jsD1Duration\" value=\"178000\" />                <input type=\"hidden\" class=\"jsD1PreviewUrl\" value=\"http://dc722.4shared.com/img/V2kgaWQNce/b1019eac/dlink__2Fdownload_2FV2kgaWQNce_2FCL_5F-_5FHello_5FBitches.mp3_3Fsbsr_3Da47fc8f2a33259d0006f04b46bd47117977_26lgfp_3D7200/preview.mp3\" />   <div class=\"jsD1Artist\" style=\"display:none\">CL</div>                <input type=\"hidden\" class=\"jsD1Duration\" value=\"178000\" />                <input type=\"hidden\" class=\"jsD1PreviewUrl\" value=\"http://dc722.4shared.com/img/V2kgaWQNce/b1019eac/dlink__2Fdownload_2FV2kgaWQNce_2FCL_5F-_5FHello_5FBitches.mp3_3Fsbsr_3Da47fc8f2a33259d0006f04b46bd47117977_26lgfp_3D7200/preview.mp3?dasdaddasdads\" />     <div class=\"jsD1Artist\" style=\"display:none\">CL</div>                <input type=\"hidden\" class=\"jsD1Duration\" value=\"178000\" />                <input type=\"hidden\" class=\"jsD1PreviewUrl\" value=\"http://dc722.4shared.com/img/V2kgaWQNce/b1019eac/dlink__2Fdownload_2FV2kgaWQNce_2FCL_5F-_5FHello_5FBitches.mp3_3Fsbsr_3Da47fc8f2a33259d0006f04b46bd47117977_26lgfp_3D7200/preview.mp3_ddasdadaddasd\" />    ";

		// vimeo.com
		Pattern p = Pattern.compile("\"config_url\":\"(.*?config)|\"data-config-url\":\"(.*?config)");
		String s = "player\":{\"config_url\":\"https://player.vimeo.com/video/145937066/config?autoplay=0&byline=0&collections=1&context=Vimeo%5CController%5CClipController.main_beta&default_to_hd=1&outro=beginning&portrait=0&share=1&title=0&watch_trailer=0&s=8e5d54c0e7ab0368e56465c8f9709aa9402db7d6_1466060636\",player\":{\"data-config-url\":\"https://player.vimeo.com/video/145937066/config?autoplay=0&byline=0&collections=1&context=Vimeo%5CController%5CClipController.main_beta&default_to_hd=1&outro=beginning&portrait=0&share=1&title=0&watch_trailer=0&s=8e5d54c0e7ab0368e56465c8f9709aa9402db7d6_1466060636\"";

        Matcher m = p.matcher(s);
        while(m.find()){
            System.out.println(m.group());
			System.out.println(123);
        }

		String dd = "dasdad\\/dasda";
		System.out.println(dd.replaceAll("\\\\", ""));

	}
}

