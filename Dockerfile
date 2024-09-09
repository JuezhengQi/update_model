# 使用官方 Python 镜像作为基础镜像
FROM ubuntu:20.04

# 维护者信息
LABEL maintainer="qijuezheng@openloong.net"

# 设置环境变量
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# 更新包列表并安装依赖
RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    && apt-get clean

COPY miniconda.sh .

# 下载并安装 Miniconda
RUN bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh

# 设置 PATH 环境变量
ENV PATH=/opt/conda/bin:$PATH

# 设置工作目录
WORKDIR /app

# 复制环境文件到容器
COPY environment.yml .

# 创建 Conda 环境
#RUN conda env create -f environment.yml && \
#    conda clean -a
    
# 设置默认环境
ENV PATH=/opt/conda/envs/RL/bin:$PATH

# 复制当前目录的内容到容器内的 /app 目录
COPY . /app


# 暴露端口（如果你的应用需要）
# EXPOSE 5000

# 设置默认命令
# CMD ["python", "slot_logic.py"]
# CMD ["while true;do echo hello docker;sleep 1;done"]
