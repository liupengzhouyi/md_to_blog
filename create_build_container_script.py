
# 新的数组包字典的数据格式
infos_dict = [
    {
        "blog_name": "financial_blog",
        "markdown_dir": "content_financial",
        "config_file": "conf_financial.config.toml",
        "port": "2001",
        "baseURL": "http://43.138.87.70"
    },
    {
        "blog_name": "technology_blog",
        "markdown_dir": "content_technology",
        "config_file": "conf_technology.config.toml",
        "port": "2002",
        "baseURL": "http://43.138.87.70"
    },
    {
        "blog_name": "The_First_Half_of_My_Life",
        "markdown_dir": "content_The_First_Half_of_My_Life",
        "config_file": "conf_The_First_Half_of_My_Life.config.toml",
        "port": "2003",
        "baseURL": "http://43.138.87.70"
    },
    {
        "blog_name": "The_Second_Half_Of_My_Life",
        "markdown_dir": "content_The_Second_Half_Of_My_Life",
        "config_file": "conf_The_Second_Half_Of_My_Life.config.toml",
        "port": "2004",
        "baseURL": "http://43.138.87.70"
    }
]


def generate_docker_commands(infos):
    for info in infos:
        name = info["blog_name"]
        dir = info["markdown_dir"]
        conf_file = info["config_file"]
        port = info["port"]
        base_url = info["baseURL"]
        
        shell_info = f"docker run -itd --name {name} -p {port}:{port} -v $(pwd)/{dir}:/src/content -v $(pwd)/{conf_file}:/src/config.toml liupeng0/markdown2blog:latest server -D --baseURL {base_url} --port {port}"
        print(shell_info)
        gen_shell = f"docker exec -it $(docker ps | grep '{name}' | awk '{{print $1}}') hugo -F --cleanDestinationDir"
        print(gen_shell)

def main():
    generate_docker_commands(infos_dict)

# 程序的入口点
if __name__ == "__main__":
    main()
