# DownIMG.ML eCommerce Toolbox

I developed an eCommerce toolset that makes migrating from platform to platform very easy. 

Get a preview by visiting [DownIMG.ML](https://downimg.ml)

This toolset is developed in **Python** with a **Django Web FrameWork** as a front end, it uses async processes in **Celery** with a **Redis** backed.

On the front end it uses *HTML*, *CSS*, *Javascript*, *Bootstrap 4* and *Font Awsome*.

This toolset includes:

- [Batch Image Downloader](https://downimg.ml/download/)
Many e-commerce platforms will not allow you to import product photos from some suppliers because they have special protection to prevent image url from being downloaded. This is often a pain in the neck when it come to quickly importing products into a new e-commerce platform. Our solution works like a charm. It uses python to defeat what it's called "CURL REQUEST BLOCK", those requests are used by that many e-commerce platforms in order to import product images.

- [Excel File Splitter](https://downimg.ml/split/)
Many e-commerce platforms have limitations in terms of how many products can be imported at one time, if you have tens of thousands of products and your platform crashes after more than a few thousands, you'll need to split that big Excel File into multiple distinct files, this can be a pain and it can take you a whole day (speaking from experience) to split a big table. Our solution can split your table in seconds, yes, seconds.

- [Key Value to Excel Converter](https://downimg.ml/keyv/)
When migrating from one e-commerce platform to another you'll sometimes find yourself in a situation where you have a column of keys and a column of values and you need to transpose this so the key is the column header and the value stays on the same row. It's easier just to show you, but trust me this will tool save your bottom when it comes to migrations.






