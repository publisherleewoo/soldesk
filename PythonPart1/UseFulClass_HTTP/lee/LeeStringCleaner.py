class LeeStringCleaner:
    @staticmethod
    def clean(txt):
        txt = txt.replace("<b>", "")
        txt = txt.replace("</b>", "")
        txt = txt.replace("&quot;", "")
        return txt


# library vs framework
# library
#  자주 쓸것 같은 기능 따로 정리
#  파일 통째로 가져다니면서 필요할때마다 쓰기 편하게

# framework
# library + 자체개발툴