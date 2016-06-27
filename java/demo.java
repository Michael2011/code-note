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
		// Pattern p = Pattern.compile("magnet:\\?.*?[\"\'>]");
		// String s = "<a href=\"magnet:?xt=urn:btih:FB9CE5FB309C3E2577EE6978831AA0CB90811340&dn=The+Vet+Life+S01E01+Hello+Houston+HDTV+x264-%5BNY2%5D&tr=udp%3A%2F%2Fglotorrents.pw%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce\" rel=\"nofollow\" class=\"csprite_dltorrent\" title=\"Download The Vet Life S01E01 Hello Houston HDTV x264-[NY2] magnet\"></a><p><a href=\"magnet:?xt=urn:btih:FB9CE5FB309C3E2577EE6978831AA0CB90811340&dn=The+Vet+Life+S01E01+Hello+Houston+HDTV+x264-%5BNY2%5D&tr=udp%3A%2F%2Fglotorrents.pw%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce\" rel=\"nofollow\">Magnet Link</a></p></div></div>";
		



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
		// Pattern p = Pattern.compile("<script>q\\(\"talkPage\\.init\",(.*?)\\)</script>");
		// String s = "<script>q(\"talkPage.init)\",{\"talks\":[{dasdadadad)</script>";

		// tune.pk
		// Pattern p = Pattern.compile("file: [\"\'](http[^\\s\"\']*\\.(mp4)[^\\s\"\']*)[\'\"]", Pattern.CASE_INSENSITIVE | Pattern.DOTALL);
		//String s = "var video_files = [ {" 
		//	  + "file: 'http:qeqweq'"
        //      + "file: 'http://cw003.tunefiles.com/files/videos/2016/02/29/1456741746d80b6-720.mp4', "
        //      + "width: \"100%\","
        //      + "height: \"100%\", "
        //      + "label : \"720p\","
        //      + "file: \'http://cw003.tunefiles.com/files/videos/2016/02/29/1456741746d80b6-720.mp4\', "
        //      + "bitrate : \"720\",];";
		// Pattern p = Pattern.compile("href=[\'\"](http[^\\s\"\']*\\.(mp4))[\'\"]");
		// String s = "<a class=\"btn\" download=\"awargi love games promo video song.mp4\" href=\"http://dl.hdking.mobi/media/x4/awargi_love_games_promo_video_song_1649.mp4\">Download</a>href=\"http://dl.hdking.mobi/media/x4/awargi_love_games_promo_video_song_1649.mp4312\">Download</a>";

        Matcher m = p.matcher(s);
        while(m.find()){
            System.out.println(m.group());
        }
	}
}

