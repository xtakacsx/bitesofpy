def generate_affiliation_link(url):
    affiliate_url = url.split("dp/")[-1].split("/")[0]
    return f"http://www.amazon.com/dp/{affiliate_url}/?tag=pyb0f-20"

    # split_url = url.split("/")
    # for affiliate_url in split_url:
    #     try:
    #         if affiliate_url[0].isnumeric():
    #             return f"http://www.amazon.com/dp/{affiliate_url}/?tag=pyb0f-20"
    #     except IndexError:
    #         pass
