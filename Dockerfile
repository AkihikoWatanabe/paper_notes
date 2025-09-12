FROM python:3.10-slim-bullseye
RUN apt-get update && apt-get install -y git ruby-full curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev libffi-dev graphviz graphviz-dev
RUN pip install requests tqdm pygraphviz networkx Pillow
RUN export GEM_HOME="$HOME/gems"
RUN export PATH="$HOME/gems/bin:$PATH"
WORKDIR /project
RUN gem install jekyll bundler
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
RUN source ~/.bashrc
RUN nvm install --lts 
