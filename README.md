# Download_KM_Book
> 技术不难，难的是你能不能想到

根据链接下载图片并合成 PDF

同事在群里推荐内网 KM 上书籍时抱怨无法下载。我遂分析了其网页结构，发现虽然没有提供下载链接，但是每一页的图片链接却是可以抓取到的，并且有规律可循

直接写了个简单的脚本，把书籍的每一页图片抓取下来；为了提供优质的服务体验，我下载后专门生成一个 markdown，markdown 中的每一行都是一个图片的本地链接，然后利用其转 PDF，这样一本 pdf 格式的书籍就获取到了，丢到群里，赞不绝口