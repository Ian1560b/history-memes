import b0t

while b0t.active:
    try:
        for post in b0t.subreddit.new(limit = 5):
            print(post.title, post.url)
            statuses = b0t.history_api.user_timeline(
                count = 20,
                include_rts = False,
                exclude_replies = True,
                screen_name = "ThomasPepeson",
                tweet_mode = "extended",
            )
            if hasattr(post, "is_gallery"):
                print("[+] Gallery post, sleeping.")
                b0t.time.sleep(300)
            else:
                tweet_list = []
                print(
                    f"[+] Fetched {len(statuses)} statuses for checking post duplicate"
                )
                for status in statuses:
                    splitted_status = status.full_text.lower().split("\n")
                    parts = [phrase for phrase in splitted_status]
                    final_part = parts[0]
                    tweet_list.append(final_part)
                print(tweet_list)
                if post.title.lower() in tweet_list:
                    print("[+] Already tweeted that")
                    b0t.time.sleep(201)
                else:
                    try:
                        print("[+] Posting")
                        url = post.url
                        r = b0t.requests.get(url, allow_redirects=True)
                        print(r)
                        open("sample1.jpg", "wb").write(r.content)
                        shortened_link = b0t.gib_url2(post.id)
                        b0t.history_api.update_status_with_media(
                            status = post.title +"\n" + "#meme #history " + shortened_link,
                            filename = "sample1.jpg",
                        )
                        print("[+] Posted")
                        b0t.os.remove("sample1.jpg")
                        b0t.time.sleep(2400)
                        print("[+] Sleeping")
                    except Exception as bruh_moment:
                        print(bruh_moment)
                        print("[+] Sleeping")
                        b0t.time.sleep(69)

    except Exception as flag:
        print(f"{flag} \n [+] Stopping")
        b0t.active = False

b0t.time.sleep(3600)
print("[+] Restarting")
b0t.active = True
