# 使用 klakegg/hugo 镜像作为基础镜像
FROM klakegg/hugo

WORKDIR /src

# 将当前目录的内容复制到工作目录中
COPY ./blog/ .

EXPOSE 1313