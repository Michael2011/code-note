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
		
		// Pattern p = Pattern.compile("(\"qualities\":)(.*)(,\"reporting\")");
        // String s = "\"qualities\":{\"auto\":[{\"typ:},\"reporting\"";
	
		// common regular
		// Pattern p = Pattern.compile("http[^\\s\"\'\\?]*\\.(mp3\\?|mp4\\?|flv\\?)[^\\s\"\'>]*");
		// String s = "class=\"jsD1CommentCount\" value=\"0\"/>                <input type=\"hidden\" class=\"jsD1TrackCount\" value=\"0\"/>                <input type=\"hidden\" class=\"jsD1WaveformUrl\" value=\"http://dc722.4shared.com/img/V2kgaWQNce/b1019eac/dlink__2Fdownload_2FV2kgaWQNce_2FCL_5F-_5FHello_5FBitches.mp3_3Fsbsr_3Da47fc8f2a33259d0006f04b46bd47117977_26lgfp_3D7200/preview.waveform\" />                <input type=\"hidden\" class=\"jsD1TrackNumber\" value=\"1\"/>              </div>            <div class=\"brn_scroller__bar\"></div>          </div>  class=\"jsD1CommentCount\" value=\"0\"/>                <input type=\"hidden\" class=\"jsD1TrackCount\" value=\"0\"/>                <input type=\"hidden\" class=\"jsD1WaveformUrl\" value=\"http://dc722.4shared.com/img/V2kgaWQNce/b1019eac/dlink__2Fdownload_2FV2kgaWQNce_2FCL_5F-_5FHello_5FBitches.mp3?3Fsbsr_3Da47fc8f2a33259d0006f04b46bd47117977_26lgfp_3D7200/preview.waveform\" />                <input type=\"hidden\" class=\"jsD1TrackNumber\" value=\"1\"/>              </div>            <div class=\"brn_scroller__bar\"></div>          </div>  ";
		



		// vimeo.com
		// Pattern p = Pattern.compile("data-config-url=\"(.*?config)");
		// String s = "class=\"player js-player widescreen uwidescreen\" data-config-url=\"https://player.vimeo.com/video/169711576/config?autoplay=0&amp;badge=0&amp;byline=0&amp;color=3298DA&amp;context=Vimeo%5CController%5COnDemandController.main&amp;default_to_hd=1&amp;portrait=0&amp;thumbset_id=574546129&amp;title=0&amp;s=f9d80d84a642ba5b452dbbdf1ade6deba07c15a7_1466087715\" data-fallback-url";

		
		// facebook.com
		// Pattern p = Pattern.compile("[\"\'](http[^\\s\"\']*\\.(mp4\\?)[^\\s\"\']*)[\'\"]");
		// String s = "sd_src_no_ratelimit\":\"https://video-lax3-1.xx.fbcdn.net/v/t42.1790-2/13431218_1144619268894890_1984873462_n.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InFmXzQyNndfY3JmXzIzX21haW5fMy4wX3AxaGNtdjRfc2QifQ\u00253D\u00253D&oh=32adbd80a6070226018546231a305022&oe=576235ED\",\"hd_src\":null,\"sd_src\":\"https://video-lax3-1.xx.fbcdn.net/v/t42.1790-2/13431218_1144619268894890_1984873462_n.mp4?efg=eyJybHIiOjMwMCwicmxhIjo1MTIsInZlbmNvZGVfdGFnIjoicWZfNDI2d19jcmZfMjNfbWFpbl8zLjBfcDFoY212NF9zZCJ9&rl=300&vabr=151&oh=32adbd80a6070226018546231a305022&oe=576235ED\",\"hd_tag\":\"\",\"sd_tag\":\"qf_426w_crf_23_main_3.0_p1hcmv4_sd\",\"stream_type\":\"dash\",\"live_routing_token\":\"\",\"projection\":\"flat\",\"subtitles_src\":null,\"dash_manifest\":\"\u003C?xml version=\"1.0\"?>\n\u003CMPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" minBufferTime=\"PT1.500S\" type=\"static\" mediaPresentationDuration=\"PT0H1M28.816S\" maxSegmentDuration=\"PT0H0M2.039S\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011,http://dashif.org/guidelines/dash264\">\u003CPeriod duration=\"PT0H1M28.816S\">\u003CAdaptationSet segmentAlignment=\"true\" maxWidth";

		// tumblr.com
		// Pattern p = Pattern.compile("<source\\s.*?src=[\"\'](.*?)[\"\'>]");
		// String s = "<source src=\"https://www.tumblr.com/video_file/145027430437/tumblr_o7pz1bd6Cv1uzgpfq\" type=\"video/mp4\">";
		
		// ted.com
		Pattern p = Pattern.compile("<script>q\\(\"talkPage\\.init\",(.*?)\\)</script>");
		String s = "<script>q(\"talkPage.init)\",{\"talks\":[{dasdadadad)</script>";

        Matcher m = p.matcher(s);
        while(m.find()){
            System.out.println(m.group(1));
        }
	}
}

