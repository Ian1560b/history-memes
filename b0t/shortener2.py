def post_id(permalink):
    segment1 = permalink.split("/comments/")
    segment2 = segment1[1]
    segment3 = segment2.split("/")
    segment4 = segment3[0]
    full_url = "redd.it/" + segment4 
    return full_url	#post.id lol

def gib_url2(postId):
    short_url = "redd.it/"+postId
    return short_url