# md_to_blog

I want to share my markdown note as blogs on web, Use docker tools.

## build docker image

```shell
docker build -t markdown2blog .
```

## build container by image

--name HugoBlog

### test

```shell
docker run -itd -p 1313:1313 markdown2blog server -D --baseURL http://43.138.87.70 --port 1313
```

### set your blog path

```shell
docker run -itd -p 1313:1313 -v $(pwd)/test:/src/content markdown2blog server -D --baseURL http://43.138.87.70 --port 1313
```

### gen you blog

```shell
docker exec -it $(docker ps | grep "markdown2blog" | awk '{print $1}') hugo -F --cleanDestinationDir


```

# Last but noy lest:

This code include other code in gothub: https://github.com/barklan/hugo-dead-simple.git

This code noly for IP:43.138.87.70,if  your code was not this, your need rebuild docker images.
