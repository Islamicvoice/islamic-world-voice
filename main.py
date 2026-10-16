import requests, random, os, sys
PAGE_ID = "61594930868337"
PAGE_TOKEN = os.environ.get("FB_PAGE_TOKEN")
DAILY_CONTENT = [
    ("بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيْمِ\n\nاللہ کے ذکر سے دلوں کو سکون ملتا ہے۔\n\n#IslamicWorldVoice", "https://images.pexels.com/photos/36704/mosque.jpg"),
    ("رسول اللہ ﷺ نے فرمایا: تم میں سب سے بہتر وہ ہے جو قرآن سیکھے اور سکھائے۔\n\n#Hadith", "https://images.pexels.com/photos/2108831/mosque2.jpg"),
]
REELS = [("درود شریف کی فضیلت ✨\n#Reels", "https://cdn.pixabay.com/video/2023/10/22/186115-877653483_large.mp4")]
def post_photo(img, cap):
    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/photos"
    requests.post(url, data={"url": img, "caption": cap, "access_token": PAGE_TOKEN})
def post_reel(vid, desc):
    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/video_reels"
    requests.post(url, data={"video_url": vid, "description": desc, "access_token": PAGE_TOKEN})
mode = sys.argv[1]
if mode == "morning":
    t,i = random.choice(DAILY_CONTENT); post_photo(i, "🌅 صبح کی آیت\n\n"+t)
elif mode == "afternoon":
    t,i = random.choice(DAILY_CONTENT); post_photo(i, "☀️ دوپہر کی حدیث\n\n"+t)
elif mode == "evening":
    d,v = random.choice(REELS); post_reel(v, d)
