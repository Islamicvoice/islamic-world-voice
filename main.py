import requests, random, os, sys
PAGE_ID = "61594930868337"
PAGE_TOKEN = os.environ.get("FB_PAGE_TOKEN")
print("TOKEN CHECK:", "FOUND" if PAGE_TOKEN else "MISSING")
DAILY_CONTENT = [
    ("Allah ke zikr se dilon ko sukoon milta hai. #IslamicWorldVoice", "https://images.pexels.com/photos/36704/pexels-photo-36704.jpeg"),
    ("Tum me sab se behtar wo hai jo Quran seekhe aur sikhaye. #Hadith", "https://images.pexels.com/photos/2108831/pexels-photo-2108831.jpeg"),
]
REELS = [("Durood Shareef ki fazilat #Reels", "https://cdn.pixabay.com/video/2023/10/22/186115-877653483_large.mp4")]
def post_photo(img, cap):
    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/photos"
    r = requests.post(url, data={"url": img, "caption": cap, "access_token": PAGE_TOKEN})
    print("PHOTO RESPONSE:", r.status_code)
    print(r.text)
def post_reel(vid, desc):
    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/video_reels"
    r = requests.post(url, data={"video_url": vid, "description": desc, "access_token": PAGE_TOKEN})
    print("REEL RESPONSE:", r.status_code)
    print(r.text)
mode = sys.argv[1]
print("MODE:", mode)
if mode == "morning":
    t,i = random.choice(DAILY_CONTENT); post_photo(i, "Subah ki Ayat\n\n"+t)
elif mode == "afternoon":
    t,i = random.choice(DAILY_CONTENT); post_photo(i, "Dopahar Hadith\n\n"+t)
elif mode == "evening":
    d,v = random.choice(REELS); post_reel(v, d)
